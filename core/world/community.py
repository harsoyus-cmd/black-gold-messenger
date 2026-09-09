"""
BGM Community
Black Gold Messenger

Lightweight community-driven community foundation.
"""

from dataclasses import dataclass, field


JOIN_REQUEST_PENDING = "PENDING"
JOIN_REQUEST_APPROVED = "APPROVED"

REMOVAL_THRESHOLD = 10


@dataclass
class BGMCommunity:
    """Represents an open, community-driven BGM community."""

    community_id: str
    name: str
    continent_id: str
    country_id: str
    description: str = ""
    banner: str = ""
    rules: str = ""
    members: set[str] = field(default_factory=set)
    join_requests: dict[str, set[str]] = field(default_factory=dict)
    invitations: dict[str, set[str]] = field(default_factory=dict)
    removal_requests: dict[str, set[str]] = field(default_factory=dict)

    def is_valid(self) -> bool:
        return bool(
            self.community_id.strip()
            and self.name.strip()
            and self.continent_id.strip()
            and self.country_id.strip()
        )

    def add_member(self, identity_id: str) -> None:
        if not identity_id.strip():
            raise ValueError("Identity ID must not be empty.")

        self.members.add(identity_id)

    def is_member(self, identity_id: str) -> bool:
        return identity_id in self.members

    def leave(self, identity_id: str) -> bool:
        """Allow a member to leave the community voluntarily."""
        if not identity_id.strip():
            raise ValueError("Identity ID must not be empty.")

        if identity_id not in self.members:
            raise ValueError("Identity is not a community member.")

        self.members.remove(identity_id)
        self.removal_requests.pop(identity_id, None)

        for requests in self.removal_requests.values():
            requests.discard(identity_id)

        return True

    def invite(
        self,
        invited_identity_id: str,
        inviter_identity_id: str,
    ) -> None:
        """Create an invitation from one member to another identity."""
        if not invited_identity_id.strip():
            raise ValueError("Invited identity ID must not be empty.")

        if not inviter_identity_id.strip():
            raise ValueError("Inviter identity ID must not be empty.")

        if inviter_identity_id not in self.members:
            raise ValueError("Inviter must be a community member.")

        if invited_identity_id in self.members:
            raise ValueError("Identity is already a community member.")

        self.invitations.setdefault(
            invited_identity_id,
            set(),
        ).add(inviter_identity_id)

    def accept_invitation(self, identity_id: str) -> bool:
        """Accept an invitation and become a community member."""
        if not identity_id.strip():
            raise ValueError("Identity ID must not be empty.")

        if identity_id in self.members:
            raise ValueError("Identity is already a community member.")

        if identity_id not in self.invitations:
            raise ValueError("Invitation does not exist.")

        self.members.add(identity_id)
        del self.invitations[identity_id]

        return True

    def request_join(self, identity_id: str) -> None:
        if not identity_id.strip():
            raise ValueError("Identity ID must not be empty.")

        if identity_id in self.members:
            raise ValueError("Identity is already a community member.")

        self.join_requests.setdefault(identity_id, set())

    def approve_join(
        self,
        requester_identity_id: str,
        approver_identity_id: str,
    ) -> bool:
        if not requester_identity_id.strip():
            raise ValueError("Requester identity ID must not be empty.")

        if not approver_identity_id.strip():
            raise ValueError("Approver identity ID must not be empty.")

        if approver_identity_id not in self.members:
            raise ValueError("Approver must be a community member.")

        if requester_identity_id not in self.join_requests:
            raise ValueError("Join request does not exist.")

        self.members.add(requester_identity_id)
        del self.join_requests[requester_identity_id]

        return True

    def request_removal(
        self,
        target_identity_id: str,
        requester_identity_id: str,
    ) -> bool:
        if not target_identity_id.strip():
            raise ValueError("Target identity ID must not be empty.")

        if not requester_identity_id.strip():
            raise ValueError("Requester identity ID must not be empty.")

        if target_identity_id not in self.members:
            raise ValueError("Target identity is not a community member.")

        if requester_identity_id not in self.members:
            raise ValueError("Removal requester must be a community member.")

        if target_identity_id == requester_identity_id:
            raise ValueError("A member cannot request their own removal.")

        requests = self.removal_requests.setdefault(
            target_identity_id,
            set(),
        )

        requests.add(requester_identity_id)

        if len(requests) >= REMOVAL_THRESHOLD:
            self.members.remove(target_identity_id)
            del self.removal_requests[target_identity_id]
            return True

        return False

    def get_removal_request_count(self, target_identity_id: str) -> int:
        return len(self.removal_requests.get(target_identity_id, set()))
