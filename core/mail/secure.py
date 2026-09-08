"""
BGM Secure Mail
Black Gold Messenger

Encrypted BGM Mail payload integration.
"""

import json

from core.crypto.e2ee import (
    EncryptedPayload,
    decrypt_payload,
    encrypt_payload,
)

from .mail import create_mail_content


def encrypt_mail(
    subject: str,
    body: str,
    key: bytes,
    key_id: str,
    associated_data: bytes | None = None,
) -> EncryptedPayload:
    """
    Validate and encrypt BGM Mail content.
    """

    content = create_mail_content(
        subject=subject,
        body=body,
    )

    plaintext = json.dumps(
        content,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")

    return encrypt_payload(
        plaintext=plaintext,
        key=key,
        key_id=key_id,
        associated_data=associated_data,
    )


def decrypt_mail(
    encrypted: EncryptedPayload,
    key: bytes,
    associated_data: bytes | None = None,
) -> dict:
    """
    Decrypt and validate BGM Mail content.
    """

    plaintext = decrypt_payload(
        encrypted=encrypted,
        key=key,
        associated_data=associated_data,
    )

    try:
        content = json.loads(plaintext.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("Invalid encrypted mail content.") from exc

    if not isinstance(content, dict):
        raise ValueError("Invalid mail content.")

    if "subject" not in content or "body" not in content:
        raise ValueError("Mail content is missing required fields.")

    create_mail_content(
        subject=content["subject"],
        body=content["body"],
    )

    return content
