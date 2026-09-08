"""
BGM Service Layer
Black Gold Messenger

Lightweight orchestration layer between the BGM core
engine and the application layer.
"""

SERVICE_PROTOCOL_VERSION = "0.1"


def service_protocol_version() -> str:
    """Return the current BGM Service Layer version."""

    return SERVICE_PROTOCOL_VERSION


__all__ = [
    "SERVICE_PROTOCOL_VERSION",
    "service_protocol_version",
]

from .service import BGMService

__all__.append("BGMService")
