"""
BGM Local Storage package.
"""

from .storage import (
    BGMStorage,
    MESSAGE_STATUSES,
    STORAGE_PROTOCOL_VERSION,
    storage_protocol_version,
)

__all__ = [
    "BGMStorage",
    "MESSAGE_STATUSES",
    "STORAGE_PROTOCOL_VERSION",
    "storage_protocol_version",
]
