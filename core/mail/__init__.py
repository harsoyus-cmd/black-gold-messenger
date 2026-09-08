"""
BGM Mail package.
"""

from .mail import (
    MAIL_PROTOCOL_VERSION,
    create_mail_content,
    mail_protocol_version,
    validate_body,
    validate_subject,
)

from .message import create_mail_message, create_secure_mail_message

from .secure import (
    decrypt_mail,
    encrypt_mail,
)

__all__ = [
    "MAIL_PROTOCOL_VERSION",
    "create_mail_content",
    "mail_protocol_version",
    "validate_body",
    "validate_subject",
    "create_mail_message",
    "create_secure_mail_message",
    "encrypt_mail",
    "decrypt_mail",
]
