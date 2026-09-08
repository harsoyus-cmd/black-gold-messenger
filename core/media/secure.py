"""
BGM Secure Media
Black Gold Messenger

Encrypted media metadata integration.
"""

import json

from core.crypto.e2ee import (
    EncryptedPayload,
    decrypt_payload,
    encrypt_payload,
)

from .media import create_media_metadata


def encrypt_media_metadata(
    media_type: str,
    name: str,
    size: int,
    key: bytes,
    key_id: str,
    associated_data: bytes | None = None,
) -> EncryptedPayload:
    """
    Validate and encrypt BGM media metadata.
    """

    metadata = create_media_metadata(
        media_type=media_type,
        name=name,
        size=size,
    )

    plaintext = json.dumps(
        metadata,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")

    return encrypt_payload(
        plaintext=plaintext,
        key=key,
        key_id=key_id,
        associated_data=associated_data,
    )


def decrypt_media_metadata(
    encrypted: EncryptedPayload,
    key: bytes,
    associated_data: bytes | None = None,
) -> dict:
    """
    Decrypt and validate BGM media metadata.
    """

    plaintext = decrypt_payload(
        encrypted=encrypted,
        key=key,
        associated_data=associated_data,
    )

    try:
        metadata = json.loads(plaintext.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("Invalid encrypted media metadata.") from exc

    if not isinstance(metadata, dict):
        raise ValueError("Invalid media metadata.")

    required = (
        "media_type",
        "name",
        "size",
        "protocol_version",
    )

    if not all(field in metadata for field in required):
        raise ValueError(
            "Media metadata is missing required fields."
        )

    create_media_metadata(
        media_type=metadata["media_type"],
        name=metadata["name"],
        size=metadata["size"],
    )

    return metadata
