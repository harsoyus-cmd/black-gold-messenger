"""
BGM Message Protocol
Black Gold Messenger

Core message protocol primitives.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
import secrets


class MessageType(str, Enum):
    """Supported BGM message types."""

    TEXT = "TEXT"
    MAIL = "MAIL"
    IMAGE = "IMAGE"
    FILE = "FILE"
    VIDEO = "VIDEO"
    AUDIO = "AUDIO"
    VOICE = "VOICE"
    SYSTEM = "SYSTEM"


@dataclass(frozen=True)
class BGMMessage:
    """
    Represents the basic BGM message envelope.

    Cryptographic encryption and authentication will be
    implemented in later BGM modules.
    """

    message_id: str
    sender_identity_id: str
    sender_device_id: str
    recipient_identity_id: str
    timestamp: str
    message_type: MessageType
    payload: str
    protocol_version: str = "0.1"

    def is_valid(self) -> bool:
        """Perform basic structural validation."""
        return all(
            (
                self.message_id,
                self.sender_identity_id,
                self.sender_device_id,
                self.recipient_identity_id,
                self.timestamp,
                self.payload,
                self.protocol_version,
            )
        )


def generate_message_id() -> str:
    """
    Generate a cryptographically secure unique message ID.
    """

    return "MSG-" + secrets.token_hex(32)


def current_timestamp() -> str:
    """
    Generate the current UTC timestamp in ISO 8601 format.
    """

    return datetime.now(timezone.utc).isoformat()
