"""
BGM Media Chunk Foundation
Black Gold Messenger

Lightweight bounded file reading for media transfer.
"""

from collections.abc import Iterator


DEFAULT_CHUNK_SIZE = 64 * 1024
MAX_CHUNK_SIZE = 1024 * 1024


def validate_chunk_size(chunk_size: int) -> int:
    """Validate a bounded media chunk size."""

    if not isinstance(chunk_size, int):
        raise TypeError("chunk_size must be an integer.")

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero.")

    if chunk_size > MAX_CHUNK_SIZE:
        raise ValueError("chunk_size exceeds maximum allowed size.")

    return chunk_size


def iter_file_chunks(
    path: str,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
) -> Iterator[bytes]:
    """
    Read a file incrementally without loading the entire file into RAM.
    """

    validate_chunk_size(chunk_size)

    if not isinstance(path, str):
        raise TypeError("path must be a string.")

    if not path.strip():
        raise ValueError("path must not be empty.")

    with open(path, "rb") as file:
        while True:
            chunk = file.read(chunk_size)

            if not chunk:
                break

            yield chunk
