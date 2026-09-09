"""
BGM Group Messaging
Black Gold Messenger

Lightweight group message recipient expansion.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BGMGroupMessageTarget:
    """Represents one group-message recipient."""

    group_id: str
    recipient_identity_id: str

    def is_valid(self) -> bool:
        return bool(
            self.group_id.strip()
            and self.recipient_identity_id.strip()
        )


def build_group_targets(
    group_id: str,
    member_ids: set[str],
    sender_identity_id: str,
) -> list[BGMGroupMessageTarget]:
    """Build message targets for all group members except the sender."""

    if not isinstance(group_id, str):
        raise TypeError("group_id must be a string.")

    if not group_id.strip():
        raise ValueError("group_id must not be empty.")

    if not isinstance(member_ids, set):
        raise TypeError("member_ids must be a set.")

    if not isinstance(sender_identity_id, str):
        raise TypeError("sender_identity_id must be a string.")

    if not sender_identity_id.strip():
        raise ValueError("sender_identity_id must not be empty.")

    targets = []

    for identity_id in sorted(member_ids):
        if not isinstance(identity_id, str):
            raise TypeError("All member identities must be strings.")

        if not identity_id.strip():
            raise ValueError("Member identity ID must not be empty.")

        if identity_id == sender_identity_id:
            continue

        targets.append(
            BGMGroupMessageTarget(
                group_id=group_id,
                recipient_identity_id=identity_id,
            )
        )

    return targets


def create_group_text_messages(
    service,
    group_id: str,
    member_ids: set[str],
    sender_identity_id: str,
    sender_device_id: str,
    text: str,
    session_keys: dict[str, bytes],
    key_ids: dict[str, str],
    associated_data: bytes | None = None,
):
    """Create one encrypted text message for each group recipient."""

    if not hasattr(service, "create_text_message"):
        raise TypeError("service must provide create_text_message().")

    targets = build_group_targets(
        group_id=group_id,
        member_ids=member_ids,
        sender_identity_id=sender_identity_id,
    )

    messages = []

    for target in targets:
        if target.recipient_identity_id not in session_keys:
            raise ValueError(
                "Session key is missing for group recipient."
            )

        if target.recipient_identity_id not in key_ids:
            raise ValueError(
                "Key ID is missing for group recipient."
            )

        message = service.create_text_message(
            sender_identity_id=sender_identity_id,
            sender_device_id=sender_device_id,
            recipient_identity_id=target.recipient_identity_id,
            text=text,
            session_key=session_keys[target.recipient_identity_id],
            key_id=key_ids[target.recipient_identity_id],
            associated_data=associated_data,
        )

        messages.append(message)

    return messages
