"""
BGM Cryptography package.
"""

from .crypto import (
    CRYPTO_PROTOCOL_VERSION,
    CryptoKey,
    crypto_protocol_version,
    derive_encryption_key,
    derive_key,
    decrypt_data,
    ed25519_public_key,
    ed25519_sign,
    ed25519_verify,
    encrypt_data,
    generate_ed25519_private_key,
    generate_key_id,
    generate_nonce,
    generate_x25519_private_key,
    x25519_public_key,
    x25519_shared_secret,
)

from .e2ee import (
    E2EE_PROTOCOL_VERSION,
    EncryptedPayload,
    decrypt_payload,
    e2ee_protocol_version,
    encrypt_payload,
)

from .session import (
    SESSION_PROTOCOL_VERSION,
    BGMSessionKeys,
    create_session_keys,
    derive_session_key,
)

from .replay import (
    REPLAY_PROTOCOL_VERSION,
    BGMReplayState,
)

from .secure_session import (
    SECURE_SESSION_PROTOCOL_VERSION,
    HANDSHAKE_MESSAGE_TYPE,
    BGMSessionHandshake,
    create_handshake,
    verify_handshake,
    derive_handshake_secret,
    create_session_from_handshake,
)

__all__ = [
    "CRYPTO_PROTOCOL_VERSION",
    "CryptoKey",
    "crypto_protocol_version",
    "derive_encryption_key",
    "derive_key",
    "decrypt_data",
    "ed25519_public_key",
    "ed25519_sign",
    "ed25519_verify",
    "encrypt_data",
    "generate_ed25519_private_key",
    "generate_key_id",
    "generate_nonce",
    "generate_x25519_private_key",
    "x25519_public_key",
    "x25519_shared_secret",
    "E2EE_PROTOCOL_VERSION",
    "EncryptedPayload",
    "decrypt_payload",
    "e2ee_protocol_version",
    "encrypt_payload",
    "SESSION_PROTOCOL_VERSION",
    "BGMSessionKeys",
    "create_session_keys",
    "derive_session_key",
    "REPLAY_PROTOCOL_VERSION",
    "BGMReplayState",
    "SECURE_SESSION_PROTOCOL_VERSION",
    "HANDSHAKE_MESSAGE_TYPE",
    "BGMSessionHandshake",
    "create_handshake",
    "verify_handshake",
    "derive_handshake_secret",
    "create_session_from_handshake",
]
