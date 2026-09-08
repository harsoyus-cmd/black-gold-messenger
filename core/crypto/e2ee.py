"""
BGM End-to-End Encryption
Black Gold Messenger

Authenticated encryption for BGM payloads.
"""

from dataclasses import dataclass
import secrets

from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305


E2EE_PROTOCOL_VERSION = "0.1"
NONCE_SIZE = 12


@dataclass(frozen=True)
class EncryptedPayload:
    """
    Represents an authenticated encrypted BGM message payload.
    """

    ciphertext: bytes
    nonce: bytes
    key_id: str
    protocol_version: str = E2EE_PROTOCOL_VERSION

    def is_valid(self) -> bool:
        """Perform basic structural validation."""
        return bool(
            self.ciphertext
            and len(self.nonce) == NONCE_SIZE
            and self.key_id
            and self.protocol_version
        )


def encrypt_payload(
    plaintext: bytes,
    key: bytes,
    key_id: str,
    associated_data: bytes | None = None,
) -> EncryptedPayload:
    """
    Encrypt plaintext using ChaCha20-Poly1305.
    """

    if not plaintext:
        raise ValueError("Plaintext must not be empty.")

    if not key_id:
        raise ValueError("Key ID must not be empty.")

    cipher = ChaCha20Poly1305(key)
    nonce = secrets.token_bytes(NONCE_SIZE)
    ciphertext = cipher.encrypt(nonce, plaintext, associated_data)

    return EncryptedPayload(
        ciphertext=ciphertext,
        nonce=nonce,
        key_id=key_id,
    )


def decrypt_payload(
    encrypted: EncryptedPayload,
    key: bytes,
    associated_data: bytes | None = None,
) -> bytes:
    """
    Decrypt and authenticate an encrypted BGM payload.
    """

    if not encrypted.is_valid():
        raise ValueError("Invalid encrypted payload.")

    cipher = ChaCha20Poly1305(key)

    return cipher.decrypt(
        encrypted.nonce,
        encrypted.ciphertext,
        associated_data,
    )


def e2ee_protocol_version() -> str:
    """Return the current BGM E2EE protocol version."""

    return E2EE_PROTOCOL_VERSION
