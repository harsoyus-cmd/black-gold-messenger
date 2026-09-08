"""
BGM Media Wire Payload
Black Gold Messenger

JSON representation for media metadata.
"""

import json
from dataclasses import dataclass

from ..media import (
    validate_media_name,
    validate_media_size,
    validate_media_type,
)


MEDIA_WIRE_PROTOCOL_VERSION = "0.1"


@dataclass(frozen=True)
class BGMMediaWirePayload:
    """Serializable BGM media metadata."""

    media_type: str
    name: str
    size: int
    protocol_version: str = MEDIA_WIRE_PROTOCOL_VERSION

    def is_valid(self) -> bool:
        """Perform structural and media validation."""

        try:
            validate_media_type(self.media_type)
            validate_media_name(self.name)
            validate_media_size(self.size)
        except (TypeError, ValueError):
            return False

        return bool(self.protocol_version)


def encode_wire_payload(
    metadata: dict,
) -> str:
    """Encode media metadata as compact JSON."""

    required = (
        "media_type",
        "name",
        "size",
        "protocol_version",
    )

    if not isinstance(metadata, dict):
        raise TypeError("Metadata must be a dictionary.")

    if not all(field in metadata for field in required):
        raise ValueError("Media metadata is missing required fields.")

    result = BGMMediaWirePayload(
        media_type=metadata["media_type"],
        name=metadata["name"],
        size=metadata["size"],
        protocol_version=metadata["protocol_version"],
    )

    if not result.is_valid():
        raise ValueError("Invalid media metadata.")

    return json.dumps(
        {
            "media_type": result.media_type,
            "name": result.name,
            "size": result.size,
            "protocol_version": result.protocol_version,
        },
        separators=(",", ":"),
        ensure_ascii=False,
    )


def decode_wire_payload(
    payload: str,
) -> BGMMediaWirePayload:
    """Decode and validate JSON media metadata."""

    if not isinstance(payload, str):
        raise TypeError("Payload must be a string.")

    if not payload:
        raise ValueError("Payload must not be empty.")

    try:
        data = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise ValueError("Invalid media wire JSON.") from exc

    if not isinstance(data, dict):
        raise ValueError("Invalid media wire payload.")

    required = (
        "media_type",
        "name",
        "size",
        "protocol_version",
    )

    if not all(field in data for field in required):
        raise ValueError(
            "Media wire payload is missing required fields."
        )

    result = BGMMediaWirePayload(
        media_type=data["media_type"],
        name=data["name"],
        size=data["size"],
        protocol_version=data["protocol_version"],
    )

    if not result.is_valid():
        raise ValueError("Invalid media wire payload.")

    return result
