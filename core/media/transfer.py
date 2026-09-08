"""
BGM Media Transfer Foundation
Black Gold Messenger

Lightweight transfer descriptor for bounded media transfer.
"""

from dataclasses import dataclass

from .chunk import DEFAULT_CHUNK_SIZE, validate_chunk_size
from .media import validate_media_size


@dataclass(frozen=True)
class BGMMediaTransfer:
    """Describe a media transfer without holding media bytes."""

    media_size: int
    chunk_size: int = DEFAULT_CHUNK_SIZE
    offset: int = 0

    def is_valid(self) -> bool:
        """Validate transfer boundaries."""

        return (
            isinstance(self.media_size, int)
            and self.media_size >= 0
            and isinstance(self.chunk_size, int)
            and 0 < self.chunk_size <= 1024 * 1024
            and isinstance(self.offset, int)
            and 0 <= self.offset <= self.media_size
        )


def create_media_transfer(
    media_size: int,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    offset: int = 0,
) -> BGMMediaTransfer:
    """Create a validated media transfer descriptor."""

    validate_media_size(media_size)
    validate_chunk_size(chunk_size)

    if not isinstance(offset, int):
        raise TypeError("offset must be an integer.")

    if offset < 0:
        raise ValueError("offset must not be negative.")

    if offset > media_size:
        raise ValueError("offset must not exceed media_size.")

    return BGMMediaTransfer(
        media_size=media_size,
        chunk_size=chunk_size,
        offset=offset,
    )
