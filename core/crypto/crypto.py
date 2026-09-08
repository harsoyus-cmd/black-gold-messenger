"""
BGM Cryptography
Black Gold Messenger

Cryptographic foundation and key agreement primitives.
"""

from dataclasses import dataclass
import secrets

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import x25519


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


def crypto_protocol_version() -> str:
    """Return the current BGM cryptography protocol version."""

    return CRYPTO_PROTOCOL_VERSION
