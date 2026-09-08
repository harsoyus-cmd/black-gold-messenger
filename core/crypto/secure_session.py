"""
BGM Secure Session
Black Gold Messenger

Authenticated session handshake foundation.
"""

from dataclasses import dataclass
import secrets

from cryptography.hazmat.primitives.asymmetric.x25519 import (
    X25519PrivateKey,
)

from .crypto import (
    ed25519_public_key,
    ed25519_sign,
    ed25519_verify,
    x25519_public_key,
    x25519_shared_secret,
)
from .session import create_session_keys


SECURE_SESSION_PROTOCOL_VERSION = "0.1"
HANDSHAKE_MESSAGE_TYPE = "BGM_SESSION_HANDSHAKE"


@dataclass(frozen=True)
class BGMSessionHandshake:
    """Public data exchanged during session establishment."""

    identity_id: str
    device_id: str
    identity_public_key: bytes
    ephemeral_public_key: bytes
    nonce: bytes
    signature: bytes
    protocol_version: str = SECURE_SESSION_PROTOCOL_VERSION

    def is_valid(self) -> bool:
        """Perform basic handshake validation."""

        return bool(
            self.identity_id
            and self.device_id
            and self.identity_public_key
            and self.ephemeral_public_key
            and self.nonce
            and self.signature
            and self.protocol_version
        )


def _handshake_data(
    identity_id: str,
    device_id: str,
    ephemeral_public_key: bytes,
    nonce: bytes,
) -> bytes:
    """Build canonical handshake data for signing."""

    return (
        HANDSHAKE_MESSAGE_TYPE.encode("utf-8")
        + b"|"
        + SECURE_SESSION_PROTOCOL_VERSION.encode("utf-8")
        + b"|"
        + identity_id.encode("utf-8")
        + b"|"
        + device_id.encode("utf-8")
        + b"|"
        + ephemeral_public_key
        + b"|"
        + nonce
    )


def create_handshake(
    identity_id: str,
    device_id: str,
    identity_private_key: bytes,
) -> tuple[BGMSessionHandshake, X25519PrivateKey]:
    """
    Create a signed session handshake and fresh ephemeral X25519 key.
    """

    if not identity_id:
        raise ValueError("Identity ID must not be empty.")

    if not device_id:
        raise ValueError("Device ID must not be empty.")

    if not identity_private_key:
        raise ValueError(
            "Identity private key must not be empty."
        )

    ephemeral_private_key = X25519PrivateKey.generate()
    ephemeral_public = x25519_public_key(
        ephemeral_private_key
    )

    nonce = secrets.token_bytes(32)

    data = _handshake_data(
        identity_id,
        device_id,
        ephemeral_public,
        nonce,
    )

    signature = ed25519_sign(
        identity_private_key,
        data,
    )

    handshake = BGMSessionHandshake(
        identity_id=identity_id,
        device_id=device_id,
        identity_public_key=ed25519_public_key(
            identity_private_key
        ),
        ephemeral_public_key=ephemeral_public,
        nonce=nonce,
        signature=signature,
    )

    return handshake, ephemeral_private_key


def verify_handshake(
    handshake: BGMSessionHandshake,
) -> bool:
    """Verify the identity signature on a handshake."""

    if not handshake.is_valid():
        return False

    data = _handshake_data(
        handshake.identity_id,
        handshake.device_id,
        handshake.ephemeral_public_key,
        handshake.nonce,
    )

    return ed25519_verify(
        handshake.identity_public_key,
        handshake.signature,
        data,
    )


def derive_handshake_secret(
    local_ephemeral_private_key: X25519PrivateKey,
    remote_ephemeral_public_key: bytes,
) -> bytes:
    """Derive the shared secret from ephemeral X25519 keys."""

    if not remote_ephemeral_public_key:
        raise ValueError(
            "Remote ephemeral public key must not be empty."
        )

    return x25519_shared_secret(
        local_ephemeral_private_key,
        remote_ephemeral_public_key,
    )


def create_session_from_handshake(
    shared_secret: bytes,
    session_id: str,
):
    """Create directional session keys from a handshake secret."""

    return create_session_keys(
        shared_secret=shared_secret,
        salt=None,
        session_id=session_id,
    )
