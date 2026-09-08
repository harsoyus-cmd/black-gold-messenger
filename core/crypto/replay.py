"""
BGM Replay Protection
Black Gold Messenger

Tracks received message identifiers and sequence numbers
to prevent replayed messages from being accepted twice.
"""

from dataclasses import dataclass, field


REPLAY_PROTOCOL_VERSION = "0.1"


@dataclass
class BGMReplayState:
    """
    Maintains replay-protection state for one secure session.
    """

    highest_sequence: int = -1
    seen_message_ids: set[str] = field(default_factory=set)
    protocol_version: str = REPLAY_PROTOCOL_VERSION

    def accept(self, message_id: str, sequence: int) -> bool:
        """
        Accept a new message only when it has not been replayed.

        Sequence numbers must be non-negative.
        """

        if not message_id:
            raise ValueError("Message ID must not be empty.")

        if sequence < 0:
            raise ValueError("Sequence must not be negative.")

        if message_id in self.seen_message_ids:
            return False

        if sequence <= self.highest_sequence:
            return False

        self.seen_message_ids.add(message_id)
        self.highest_sequence = sequence
        return True

    def is_valid(self) -> bool:
        """Perform basic replay-state validation."""

        return (
            self.highest_sequence >= -1
            and bool(self.protocol_version)
        )
