"""
BGM Community Discussion
Black Gold Messenger

Lightweight discussion foundation for community conversations.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class BGMDiscussionMessage:
    """Represents one community discussion message."""

    message_id: str
    sender_identity_id: str
    text: str

    def is_valid(self) -> bool:
        return bool(
            self.message_id.strip()
            and self.sender_identity_id.strip()
            and self.text.strip()
        )


@dataclass
class BGMCommunityDiscussion:
    """Lightweight discussion message collection."""

    community_id: str
    messages: list[BGMDiscussionMessage] = field(default_factory=list)

    def add_message(
        self,
        message: BGMDiscussionMessage,
        member_ids: set[str],
    ) -> None:
        if not isinstance(message, BGMDiscussionMessage):
            raise TypeError("message must be a BGMDiscussionMessage.")

        if not message.is_valid():
            raise ValueError("Invalid discussion message.")

        if message.sender_identity_id not in member_ids:
            raise ValueError("Sender must be a community member.")

        self.messages.append(message)

    def get_messages(self) -> list[BGMDiscussionMessage]:
        return list(self.messages)
