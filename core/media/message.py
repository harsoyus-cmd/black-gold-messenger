"""
BGM Media Message Builder
Black Gold Messenger

Builds validated media metadata into a BGMMessage envelope.
"""

import json

from core.protocol import (
    BGMMessage,
    MessageType,
    current_timestamp,
    generate_message_id,
)

from .media import create_media_metadata


_MEDIA_MESSAGE_TYPES = {
    "IMAGE": MessageType.IMAGE,
    "FILE": MessageType.FILE,
    "AUDIO": MessageType.AUDIO,
    "VIDEO": MessageType.VIDEO,
}


def create_media_message(
    sender_identity_id: str,
    sender_device_id: str,
    recipient_identity_id: str,
    media_type: str,
    name: str,
    size: int,
) -> BGMMessage:
    """
    Create a BGM media message.

    Media metadata is serialized as JSON inside the existing
    BGMMessage payload. The BGMMessage envelope remains unchanged.
    """

    if not isinstance(sender_identity_id, str):
        raise TypeError("sender_identity_id must be a string.")

    if not sender_identity_id.strip():
        raise ValueError("sender_identity_id must not be empty.")

    if not isinstance(sender_device_id, str):
        raise TypeError("sender_device_id must be a string.")

    if not sender_device_id.strip():
        raise ValueError("sender_device_id must not be empty.")

    if not isinstance(recipient_identity_id, str):
        raise TypeError("recipient_identity_id must be a string.")

    if not recipient_identity_id.strip():
        raise ValueError("recipient_identity_id must not be empty.")

    metadata = create_media_metadata(
        media_type=media_type,
        name=name,
        size=size,
    )

    message_type = _MEDIA_MESSAGE_TYPES[media_type]

    payload = json.dumps(
        metadata,
        ensure_ascii=False,
        separators=(",", ":"),
    )

    return BGMMessage(
        message_id=generate_message_id(),
        sender_identity_id=sender_identity_id,
        sender_device_id=sender_device_id,
        recipient_identity_id=recipient_identity_id,
        timestamp=current_timestamp(),
        message_type=message_type,
        payload=payload,
    )
