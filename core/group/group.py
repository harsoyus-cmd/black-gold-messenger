"""
BGM Personal Group
Black Gold Messenger

Lightweight personal group foundation.
"""

from dataclasses import dataclass, field


@dataclass
class BGMGroup:
    """Represents a lightweight personal group."""

    group_id: str
    name: str
    description: str = ""
    members: set[str] = field(default_factory=set)

    def is_valid(self) -> bool:
        return bool(
            self.group_id.strip()
            and self.name.strip()
        )

    def add_member(self, identity_id: str) -> None:
        if not identity_id.strip():
            raise ValueError("Identity ID must not be empty.")

        self.members.add(identity_id)

    def remove_member(self, identity_id: str) -> bool:
        if not identity_id.strip():
            raise ValueError("Identity ID must not be empty.")

        if identity_id not in self.members:
            raise ValueError("Identity is not a group member.")

        self.members.remove(identity_id)
        return True

    def is_member(self, identity_id: str) -> bool:
        return identity_id in self.members

    def get_members(self) -> set[str]:
        return set(self.members)
