"""
BGM Cryptography
Black Gold Messenger

Cryptographic foundation, key agreement,
key derivation, and digital signature primitives.
"""

from dataclasses import dataclass
import secrets

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ed25519, x25519
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.primitives.kdf.hkdf import HKDF


CRYPTO_PROTOCOL_VERSION = "0.1"


@dataclass(frozen=True)
class CryptoKey:
    """
    Represents public cryptographic key metadata.

    Private key material is intentionally not stored here.
    """

    key_id: str
    public_key: bytes

    def is_valid(self) -> bool:
        """Perform basic structural validation."""
        return bool(self.key_id and self.public_key)


def generate_key_id() -> str:
    """
    Generate a cryptographically secure key identifier.
    """

    return "KEY-" + secrets.token_hex(16)


def generate_nonce(length: int = 24) -> bytes:
    """
    Generate cryptographically secure random bytes.

    The E2EE payload layer defines its own nonce size
    according to the selected authenticated-encryption
    construction.
    """

    if length <= 0:
        raise ValueError("Nonce length must be greater than zero.")

    return secrets.token_bytes(length)


def generate_x25519_private_key() -> x25519.X25519PrivateKey:
    """
    Generate a new X25519 private key.
    """

    return x25519.X25519PrivateKey.generate()


def x25519_public_key(
    private_key: x25519.X25519PrivateKey,
) -> bytes:
    """
    Export an X25519 public key in raw format.
    """

    return private_key.public_key().public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw,
    )


def x25519_shared_secret(
    private_key: x25519.X25519PrivateKey,
    peer_public_key: bytes,
) -> bytes:
    """
    Derive a shared secret using X25519.

    The private key remains on the local device.
    """

    peer_key = x25519.X25519PublicKey.from_public_bytes(peer_public_key)

    return private_key.exchange(peer_key)


def derive_key(
    shared_secret: bytes,
    salt: bytes | None,
    info: bytes,
    length: int = 32,
) -> bytes:
    """
    Derive key material from a shared secret using HKDF-SHA256.

    The raw shared secret MUST NOT be used directly
    as an encryption key.
    """

    if not shared_secret:
        raise ValueError("Shared secret must not be empty.")

    if not info:
        raise ValueError("HKDF info must not be empty.")

    if length <= 0:
        raise ValueError("Derived key length must be greater than zero.")

    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=length,
        salt=salt,
        info=info,
    )

    return hkdf.derive(shared_secret)


def derive_encryption_key(
    shared_secret: bytes,
    salt: bytes | None,
    context: bytes,
) -> bytes:
    """
    Derive a 32-byte ChaCha20-Poly1305 encryption key.

    Domain separation is provided by the BGM context.
    """

    if not context:
        raise ValueError("Encryption context must not be empty.")

    info = b"BGM-E2EE-ENCRYPTION-V0.1|" + context

    return derive_key(
        shared_secret=shared_secret,
        salt=salt,
        info=info,
        length=32,
    )


def encrypt_data(
    plaintext: bytes,
    key: bytes,
    associated_data: bytes | None = None,
) -> tuple[bytes, bytes]:
    """
    Encrypt data using ChaCha20-Poly1305.

    Returns:
        (nonce, ciphertext)
    """

    if not plaintext:
        raise ValueError("Plaintext must not be empty.")

    nonce = secrets.token_bytes(12)
    cipher = ChaCha20Poly1305(key)
    ciphertext = cipher.encrypt(
        nonce,
        plaintext,
        associated_data,
    )

    return nonce, ciphertext


def decrypt_data(
    nonce: bytes,
    ciphertext: bytes,
    key: bytes,
    associated_data: bytes | None = None,
) -> bytes:
    """
    Decrypt and authenticate ChaCha20-Poly1305 data.
    """

    if len(nonce) != 12:
        raise ValueError("Nonce must be exactly 12 bytes.")

    if not ciphertext:
        raise ValueError("Ciphertext must not be empty.")

    cipher = ChaCha20Poly1305(key)

    return cipher.decrypt(
        nonce,
        ciphertext,
        associated_data,
    )


def generate_ed25519_private_key() -> ed25519.Ed25519PrivateKey:
    """
    Generate a new Ed25519 private key.
    """

    return ed25519.Ed25519PrivateKey.generate()


def ed25519_public_key(
    private_key: ed25519.Ed25519PrivateKey,
) -> bytes:
    """
    Export an Ed25519 public key in raw format.
    """

    return private_key.public_key().public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw,
    )


def ed25519_sign(
    private_key: ed25519.Ed25519PrivateKey,
    message: bytes,
) -> bytes:
    """
    Sign a message using Ed25519.
    """

    if not message:
        raise ValueError("Message must not be empty.")

    return private_key.sign(message)


def ed25519_verify(
    public_key: bytes,
    signature: bytes,
    message: bytes,
) -> bool:
    """
    Verify an Ed25519 signature.

    Returns False when verification fails.
    """

    if not public_key:
        raise ValueError("Public key must not be empty.")

    if not signature:
        raise ValueError("Signature must not be empty.")

    if not message:
        raise ValueError("Message must not be empty.")

    try:
        key = ed25519.Ed25519PublicKey.from_public_bytes(public_key)
        key.verify(signature, message)
        return True
    except Exception:
        return False


def crypto_protocol_version() -> str:
    """Return the current BGM cryptography protocol version."""

    return CRYPTO_PROTOCOL_VERSION
