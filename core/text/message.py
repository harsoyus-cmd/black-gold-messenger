"""
BGM Text Message Builder
Black Gold Messenger

Builds encrypted text into a BGMMessage envelope.
"""

from core.protocol import (
    BGMMessage,
    MessageType,
    current_timestamp,
    generate_message_id,
)

from .text import encrypt_text
from .wire import encode_wire_payload


def create_text_message(
    sender_identity_id: str,
    sender_device_id: str,
    recipient_identity_id: str,
    text: str,
    session_key: bytes,
    key_id: str,
    associated_data: bytes | None = None,
) -> BGMMessage:
    """
    Create an encrypted BGM TEXT message.

    The resulting payload is a JSON + Base64 wire payload.
    """

    encrypted = encrypt_text(
        text=text,
        key=session_key,
        key_id=key_id,
        associated_data=associated_data,
    )

    payload = encode_wire_payload(encrypted)

    return BGMMessage(
        message_id=generate_message_id(),
        sender_identity_id=sender_identity_id,
        sender_device_id=sender_device_id,
        recipient_identity_id=recipient_identity_id,
        timestamp=current_timestamp(),
        message_type=MessageType.TEXT,
        payload=payload,
    )
