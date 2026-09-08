"""
BGM Cryptography package.
"""

from .crypto import (
    CRYPTO_PROTOCOL_VERSION,
    CryptoKey,
    crypto_protocol_version,
    generate_key_id,
    generate_nonce,
)

__all__ = [
    "CRYPTO_PROTOCOL_VERSION",
    "CryptoKey",
    "crypto_protocol_version",
    "generate_key_id",
    "generate_nonce",
    "E2EE_PROTOCOL_VERSION",
    "EncryptedPayload",
    "e2ee_protocol_version",
]
from .e2ee import (
    E2EE_PROTOCOL_VERSION,
    EncryptedPayload,
    e2ee_protocol_version,
)
