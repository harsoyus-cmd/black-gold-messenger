"""
BGM End-to-End Encryption
Black Gold Messenger

E2EE interfaces and secure data primitives.
"""

from dataclasses import dataclass


E2EE_PROTOCOL_VERSION = "0.1"


@dataclass(frozen=True)
class EncryptedPayload:
    """
    Represents an encrypted BGM message payload.

    Actual encryption implementation will be provided
    by the selected audited cryptographic library.
    """

    ciphertext: bytes
    nonce: bytes
    key_id: str
    protocol_version: str = E2EE_PROTOCOL_VERSION

    def is_valid(self) -> bool:
        """Perform basic structural validation."""
        return bool(
            self.ciphertext
            and self.nonce
            and self.key_id
            and self.protocol_version
        )


def e2ee_protocol_version() -> str:
    """Return the current BGM E2EE protocol version."""

    return E2EE_PROTOCOL_VERSION
