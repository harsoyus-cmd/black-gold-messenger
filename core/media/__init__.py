"""
BGM Light Media package.
"""

from .media import (
    MEDIA_PROTOCOL_VERSION,
    MEDIA_IMAGE,
    MEDIA_FILE,
    MEDIA_AUDIO,
    MEDIA_VIDEO,
    MEDIA_TYPES,
    create_media_metadata,
    media_protocol_version,
    validate_media_type,
    validate_media_name,
    validate_media_size,
)

from .message import create_media_message

from .secure import (
    decrypt_media_metadata,
    encrypt_media_metadata,
)

__all__ = [
    "MEDIA_PROTOCOL_VERSION",
    "MEDIA_IMAGE",
    "MEDIA_FILE",
    "MEDIA_AUDIO",
    "MEDIA_VIDEO",
    "MEDIA_TYPES",
    "create_media_metadata",
    "media_protocol_version",
    "validate_media_type",
    "validate_media_name",
    "validate_media_size",
    "create_media_message",
    "encrypt_media_metadata",
    "decrypt_media_metadata",
]

from .chunk import (
    DEFAULT_CHUNK_SIZE,
    MAX_CHUNK_SIZE,
    iter_file_chunks,
    validate_chunk_size,
)

__all__ += [
    "DEFAULT_CHUNK_SIZE",
    "MAX_CHUNK_SIZE",
    "iter_file_chunks",
    "validate_chunk_size",
]

from .transfer import (
    BGMMediaTransfer,
    create_media_transfer,
)

__all__ += [
    "BGMMediaTransfer",
    "create_media_transfer",
]
