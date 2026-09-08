"""
BGM Mail Wire package.
"""

from .payload import (
    BGMMailWirePayload,
    decode_wire_payload,
    encode_wire_payload,
)

__all__ = [
    "BGMMailWirePayload",
    "decode_wire_payload",
    "encode_wire_payload",
]
