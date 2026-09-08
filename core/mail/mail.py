"""
BGM Mail
Black Gold Messenger

Lightweight peer-to-peer mail foundation.
"""

MAIL_PROTOCOL_VERSION = "0.1"


def mail_protocol_version() -> str:
    """Return the current BGM Mail protocol version."""

    return MAIL_PROTOCOL_VERSION


def validate_subject(subject: str) -> str:
    """Validate BGM Mail subject."""

    if not isinstance(subject, str):
        raise TypeError("Subject must be a string.")

    if not subject.strip():
        raise ValueError("Subject must not be empty.")

    return subject


def validate_body(body: str) -> str:
    """Validate BGM Mail body."""

    if not isinstance(body, str):
        raise TypeError("Body must be a string.")

    if not body.strip():
        raise ValueError("Body must not be empty.")

    return body


def create_mail_content(
    subject: str,
    body: str,
) -> dict:
    """Create validated BGM Mail content."""

    validate_subject(subject)
    validate_body(body)

    return {
        "subject": subject,
        "body": body,
    }
