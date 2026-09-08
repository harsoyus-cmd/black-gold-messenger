"""
BGM Light Media
Black Gold Messenger

Lightweight media metadata foundation.
"""

MEDIA_PROTOCOL_VERSION = "0.1"

MEDIA_IMAGE = "IMAGE"
MEDIA_FILE = "FILE"
MEDIA_AUDIO = "AUDIO"
MEDIA_VIDEO = "VIDEO"

MEDIA_TYPES = (
    MEDIA_IMAGE,
    MEDIA_FILE,
    MEDIA_AUDIO,
    MEDIA_VIDEO,
)


def media_protocol_version() -> str:
    """Return the current BGM Media protocol version."""

    return MEDIA_PROTOCOL_VERSION


def validate_media_type(media_type: str) -> str:
    """Validate a BGM media type."""

    if not isinstance(media_type, str):
        raise TypeError("media_type must be a string.")

    if media_type not in MEDIA_TYPES:
        raise ValueError("Invalid media type.")

    return media_type


def validate_media_name(name: str) -> str:
    """Validate a media file name."""

    if not isinstance(name, str):
        raise TypeError("name must be a string.")

    if not name.strip():
        raise ValueError("name must not be empty.")

    return name


def validate_media_size(size: int) -> int:
    """Validate media size in bytes."""

    if not isinstance(size, int):
        raise TypeError("size must be an integer.")

    if size < 0:
        raise ValueError("size must not be negative.")

    return size


def create_media_metadata(
    media_type: str,
    name: str,
    size: int,
) -> dict:
    """Create validated, language-neutral media metadata."""

    validate_media_type(media_type)
    validate_media_name(name)
    validate_media_size(size)

    return {
        "media_type": media_type,
        "name": name,
        "size": size,
        "protocol_version": MEDIA_PROTOCOL_VERSION,
    }
