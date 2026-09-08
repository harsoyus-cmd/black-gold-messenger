"""
BGM Text Wire Payload
Black Gold Messenger

JSON + Base64 representation for encrypted text payloads.
"""

import base64
import json
from dataclasses import dataclass


TEXT_WIRE_PROTOCOL_VERSION = "0.1"


@dataclass(frozen=True)
class BGMTextWirePayload:
    """Serializable encrypted text payload."""

    ciphertext: bytes
    nonce: bytes
    key_id: str
    protocol_version: str = TEXT_WIRE_PROTOCOL_VERSION

    def is_valid(self) -> bool:
        """Perform basic structural validation."""

        return bool(
            self.ciphertext
            and self.nonce
            and self.key_id
            and self.protocol_version
        )


def encode_wire_payload(
    encrypted_payload,
) -> str:
    """Encode an encrypted payload as JSON with Base64 binary fields."""

    if not encrypted_payload.is_valid():
        raise ValueError("Invalid encrypted payload.")

    data = {
        "ciphertext": base64.b64encode(
            encrypted_payload.ciphertext
        ).decode("ascii"),
        "nonce": base64.b64encode(
            encrypted_payload.nonce
        ).decode("ascii"),
        "key_id": encrypted_payload.key_id,
        "protocol_version": encrypted_payload.protocol_version,
    }

    return json.dumps(
        data,
        separators=(",", ":"),
        ensure_ascii=False,
    )


def decode_wire_payload(
    payload: str,
) -> BGMTextWirePayload:
    """Decode a JSON + Base64 encrypted text payload."""

    if not isinstance(payload, str):
        raise TypeError("Payload must be a string.")

    if not payload:
        raise ValueError("Payload must not be empty.")

    try:
        data = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise ValueError("Invalid wire payload JSON.") from exc

    required = (
        "ciphertext",
        "nonce",
        "key_id",
        "protocol_version",
    )

    if not all(field in data for field in required):
        raise ValueError("Wire payload is missing required fields.")

    try:
        ciphertext = base64.b64decode(
            data["ciphertext"],
            validate=True,
        )
        nonce = base64.b64decode(
            data["nonce"],
            validate=True,
        )
    except (ValueError, TypeError) as exc:
        raise ValueError("Invalid Base64 data.") from exc

    result = BGMTextWirePayload(
        ciphertext=ciphertext,
        nonce=nonce,
        key_id=data["key_id"],
        protocol_version=data["protocol_version"],
    )

    if not result.is_valid():
        raise ValueError("Invalid wire payload.")

    return result
