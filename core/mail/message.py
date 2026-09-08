"""
BGM Mail Message Builder
Black Gold Messenger

Builds validated mail content into a BGMMessage envelope.
"""

import json

from core.protocol import (
    BGMMessage,
    MessageType,
    current_timestamp,
    generate_message_id,
)

from .mail import create_mail_content


def create_mail_message(
    sender_identity_id: str,
    sender_device_id: str,
    recipient_identity_id: str,
    subject: str,
    body: str,
) -> BGMMessage:
    """
    Create a BGM MAIL message.

    Mail content is serialized as JSON inside the existing
    BGMMessage payload.
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

    content = create_mail_content(
        subject=subject,
        body=body,
    )

    payload = json.dumps(
        content,
        ensure_ascii=False,
        separators=(",", ":"),
    )

    return BGMMessage(
        message_id=generate_message_id(),
        sender_identity_id=sender_identity_id,
        sender_device_id=sender_device_id,
        recipient_identity_id=recipient_identity_id,
        timestamp=current_timestamp(),
        message_type=MessageType.MAIL,
        payload=payload,
    )


def create_secure_mail_message(
    sender_identity_id: str,
    sender_device_id: str,
    recipient_identity_id: str,
    subject: str,
    body: str,
    session_key: bytes,
    key_id: str,
    associated_data: bytes | None = None,
) -> BGMMessage:
    """
    Create an encrypted BGM MAIL message.

    Mail content is encrypted using the existing BGM E2EE layer
    and stored inside the existing BGMMessage payload.
    """

    from .secure import encrypt_mail
    from .wire import encode_wire_payload

    encrypted = encrypt_mail(
        subject=subject,
        body=body,
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
        message_type=MessageType.MAIL,
        payload=payload,
    )
