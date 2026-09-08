"""
BGM Session Cryptography
Black Gold Messenger

Foundation for secure session key management.
"""

from dataclasses import dataclass

from .crypto import derive_key


SESSION_PROTOCOL_VERSION = "0.1"


@dataclass(frozen=True)
class BGMSessionKeys:
    """
    Derived symmetric keys for a BGM secure session.
    """

    send_key: bytes
    receive_key: bytes
    session_id: str
    protocol_version: str = SESSION_PROTOCOL_VERSION

    def is_valid(self) -> bool:
        """Perform basic session key validation."""
        return bool(
            self.send_key
            and self.receive_key
            and self.session_id
            and self.protocol_version
        )


def derive_session_key(
    shared_secret: bytes,
    salt: bytes | None,
    session_id: str,
    direction: bytes,
) -> bytes:
    """
    Derive one directional session key using HKDF-SHA256.

    Directional context prevents the same key from being
    unintentionally reused for both sending and receiving.
    """

    if not shared_secret:
        raise ValueError("Shared secret must not be empty.")

    if not session_id:
        raise ValueError("Session ID must not be empty.")

    if not direction:
        raise ValueError("Direction must not be empty.")

    info = (
        b"BGM-SESSION-V0.1|"
        + session_id.encode("utf-8")
        + b"|"
        + direction
    )

    return derive_key(
        shared_secret=shared_secret,
        salt=salt,
        info=info,
        length=32,
    )


def create_session_keys(
    shared_secret: bytes,
    salt: bytes | None,
    session_id: str,
) -> BGMSessionKeys:
    """
    Derive independent send and receive keys for a session.
    """

    send_key = derive_session_key(
        shared_secret,
        salt,
        session_id,
        b"SEND",
    )

    receive_key = derive_session_key(
        shared_secret,
        salt,
        session_id,
        b"RECEIVE",
    )

    return BGMSessionKeys(
        send_key=send_key,
        receive_key=receive_key,
        session_id=session_id,
    )
