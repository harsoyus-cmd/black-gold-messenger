"""
BGM Text Engine
Black Gold Messenger

Application-layer text message processing.
"""

TEXT_ENGINE_PROTOCOL_VERSION = "0.1"


def validate_text(text: str) -> str:
    """
    Validate BGM text content.

    Returns the original text unchanged when valid.
    """

    if not isinstance(text, str):
        raise TypeError("Text must be a string.")

    if not text:
        raise ValueError("Text must not be empty.")

    if not text.strip():
        raise ValueError("Text must not contain only whitespace.")

    return text


def encode_text(text: str) -> bytes:
    """
    Validate and encode BGM text using UTF-8.
    """

    validate_text(text)

    return text.encode("utf-8")


def decode_text(data: bytes) -> str:
    """
    Decode UTF-8 text data.

    Invalid UTF-8 data raises UnicodeDecodeError.
    """

    if not isinstance(data, bytes):
        raise TypeError("Data must be bytes.")

    if not data:
        raise ValueError("Data must not be empty.")

    return data.decode("utf-8")


def text_engine_protocol_version() -> str:
    """Return the current BGM Text Engine protocol version."""

    return TEXT_ENGINE_PROTOCOL_VERSION


def encrypt_text(
    text: str,
    key: bytes,
    key_id: str,
    associated_data: bytes | None = None,
):
    """
    Validate, encode, and encrypt BGM text using the existing E2EE layer.
    """

    from core.crypto.e2ee import encrypt_payload

    plaintext = encode_text(text)

    return encrypt_payload(
        plaintext=plaintext,
        key=key,
        key_id=key_id,
        associated_data=associated_data,
    )


def decrypt_text(
    encrypted,
    key: bytes,
    associated_data: bytes | None = None,
) -> str:
    """
    Decrypt an encrypted BGM text payload and recover the original text.
    """

    from core.crypto.e2ee import decrypt_payload

    plaintext = decrypt_payload(
        encrypted=encrypted,
        key=key,
        associated_data=associated_data,
    )

    return decode_text(plaintext)
