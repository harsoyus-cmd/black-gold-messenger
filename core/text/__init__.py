"""
BGM Text Engine package.
"""

from .message import create_text_message
from .text import (
    TEXT_ENGINE_PROTOCOL_VERSION,
    validate_text,
    encode_text,
    decode_text,
    encrypt_text,
    decrypt_text,
    text_engine_protocol_version,
)
from .wire import (
    BGMTextWirePayload,
    decode_wire_payload,
    encode_wire_payload,
)

__all__ = [
    "create_text_message",
    "TEXT_ENGINE_PROTOCOL_VERSION",
    "validate_text",
    "encode_text",
    "decode_text",
    "encrypt_text",
    "decrypt_text",
    "text_engine_protocol_version",
    "BGMTextWirePayload",
    "decode_wire_payload",
    "encode_wire_payload",
]
