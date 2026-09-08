"""
BGM Message Protocol package.
"""

from .message import (
    BGMMessage,
    MessageType,
    current_timestamp,
    generate_message_id,
)

__all__ = [
    "BGMMessage",
    "MessageType",
    "current_timestamp",
    "generate_message_id",
]
