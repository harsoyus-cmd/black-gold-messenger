"""
BGM Identity
Black Gold Messenger

Core identity primitives.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BGMIdentity:
    """
    Represents the public identity of a BGM user.

    Private cryptographic material is intentionally not stored here.
    """

    identity_id: str
    public_key: str

    def is_valid(self) -> bool:
        """Perform basic structural validation."""
        return bool(self.identity_id and self.public_key)


def generate_identity_id() -> str:
    """
    Generate a random BGM Identity ID.

    The identifier contains 32 cryptographically secure random bytes.
    """
    import secrets

    return "BGM-" + secrets.token_hex(32)
