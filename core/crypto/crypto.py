"""
BGM Cryptography
Black Gold Messenger

Cryptographic foundation and interfaces.
"""

from dataclasses import dataclass
import secrets


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

    The final nonce size will be determined by the selected
    authenticated-encryption construction.
    """

    if length <= 0:
        raise ValueError("Nonce length must be greater than zero.")

    return secrets.token_bytes(length)


def crypto_protocol_version() -> str:
    """Return the current BGM cryptography protocol version."""

    return CRYPTO_PROTOCOL_VERSION
