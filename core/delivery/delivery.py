"""
BGM Offline Delivery
Black Gold Messenger

Lightweight delivery queue management.
"""

from collections.abc import Callable


DELIVERY_PROTOCOL_VERSION = "0.1"
DEFAULT_MAX_ATTEMPTS = 3


def delivery_protocol_version() -> str:
    """Return the current BGM Delivery protocol version."""

    return DELIVERY_PROTOCOL_VERSION


def delivery_attempt(
    message: dict,
    send_function: Callable[[dict], bool],
) -> bool:
    """
    Attempt to deliver one stored message.

    The transport layer is provided by the caller.
    Returns True when transport reports success.
    """

    if not isinstance(message, dict):
        raise TypeError("Message must be a dictionary.")

    if not message.get("message_id"):
        raise ValueError("Message must contain message_id.")

    if not callable(send_function):
        raise TypeError("send_function must be callable.")

    return bool(send_function(message))

def deliver_with_retry(
    message: dict,
    send_function: Callable[[dict], bool],
    max_attempts: int = DEFAULT_MAX_ATTEMPTS,
) -> bool:
    """
    Attempt delivery up to max_attempts times.

    Returns True when delivery succeeds.
    Returns False when the retry limit is reached.
    """

    if not isinstance(max_attempts, int):
        raise TypeError("max_attempts must be an integer.")

    if max_attempts <= 0:
        raise ValueError("max_attempts must be greater than zero.")

    for _ in range(max_attempts):
        if delivery_attempt(message, send_function):
            return True

    return False

def process_pending_messages(
    storage,
    send_function: Callable[[dict], bool],
    limit: int = 50,
    max_attempts: int = DEFAULT_MAX_ATTEMPTS,
) -> int:
    """
    Process a bounded batch of pending messages.

    Successful messages become SENT.
    Failed messages remain PENDING until the retry limit is handled
    by the caller's retry policy.
    """

    if not hasattr(storage, "get_pending_messages"):
        raise TypeError("storage must provide get_pending_messages.")

    messages = storage.get_pending_messages(limit=limit)

    processed = 0

    for message in messages:
        success = deliver_with_retry(
            message,
            send_function,
            max_attempts=max_attempts,
        )

        if success:
            storage.update_status(
                message["message_id"],
                "SENT",
            )

        processed += 1

    return processed
