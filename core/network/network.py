"""
BGM Network
Black Gold Messenger

Personal Communication Network foundation.
"""

NETWORK_PROTOCOL_VERSION = "0.1"


class BGMNetwork:
    """Lightweight representation of a user's BGM Network."""

    def __init__(self, identity_id: str):
        if not isinstance(identity_id, str):
            raise TypeError("identity_id must be a string.")

        if not identity_id.strip():
            raise ValueError("identity_id must not be empty.")

        self.identity_id = identity_id
        self.devices = {}
        self.permissions = {}

    def network_protocol_version(self) -> str:
        """Return the current BGM Network protocol version."""

        return NETWORK_PROTOCOL_VERSION

    def get_identity_id(self) -> str:
        """Return the BGM Identity reference."""

        return self.identity_id


DEVICE_PENDING = "PENDING"
DEVICE_TRUSTED = "TRUSTED"
DEVICE_REVOKED = "REVOKED"


def _validate_device_id(device_id: str) -> None:
    if not isinstance(device_id, str):
        raise TypeError("device_id must be a string.")

    if not device_id.strip():
        raise ValueError("device_id must not be empty.")


def register_device(network: BGMNetwork, device_id: str) -> None:
    """Register a new device as PENDING."""

    if not isinstance(network, BGMNetwork):
        raise TypeError("network must be a BGMNetwork.")

    _validate_device_id(device_id)

    if device_id in network.devices:
        raise ValueError("Device already registered.")

    network.devices[device_id] = DEVICE_PENDING


def trust_device(network: BGMNetwork, device_id: str) -> None:
    """Move a PENDING device to TRUSTED."""

    if device_id not in network.devices:
        raise ValueError("Device not found.")

    if network.devices[device_id] != DEVICE_PENDING:
        raise ValueError("Only PENDING devices can become TRUSTED.")

    network.devices[device_id] = DEVICE_TRUSTED


def revoke_device(network: BGMNetwork, device_id: str) -> None:
    """Revoke a TRUSTED device."""

    if device_id not in network.devices:
        raise ValueError("Device not found.")

    if network.devices[device_id] != DEVICE_TRUSTED:
        raise ValueError("Only TRUSTED devices can be revoked.")

    network.devices[device_id] = DEVICE_REVOKED


def get_device_status(network: BGMNetwork, device_id: str) -> str:
    """Return the current trust state of a device."""

    if device_id not in network.devices:
        raise ValueError("Device not found.")

    return network.devices[device_id]


PERMISSION_CHAT = "CHAT"
PERMISSION_MAIL = "MAIL"
PERMISSION_FILE = "FILE"
PERMISSION_MEDIA = "MEDIA"
PERMISSION_CALL = "CALL"

VALID_PERMISSIONS = (
    PERMISSION_CHAT,
    PERMISSION_MAIL,
    PERMISSION_FILE,
    PERMISSION_MEDIA,
    PERMISSION_CALL,
)


def set_permission(
    network: BGMNetwork,
    participant_id: str,
    permission: str,
    allowed: bool,
) -> None:
    """Set one communication permission for a participant."""

    if not isinstance(network, BGMNetwork):
        raise TypeError("network must be a BGMNetwork.")

    if not isinstance(participant_id, str):
        raise TypeError("participant_id must be a string.")

    if not participant_id.strip():
        raise ValueError("participant_id must not be empty.")

    if permission not in VALID_PERMISSIONS:
        raise ValueError("Invalid communication permission.")

    if not isinstance(allowed, bool):
        raise TypeError("allowed must be a boolean.")

    if participant_id not in network.permissions:
        network.permissions[participant_id] = {}

    network.permissions[participant_id][permission] = allowed


def is_permission_allowed(
    network: BGMNetwork,
    participant_id: str,
    permission: str,
) -> bool:
    """Return whether a communication permission is granted."""

    if permission not in VALID_PERMISSIONS:
        raise ValueError("Invalid communication permission.")

    return network.permissions.get(
        participant_id,
        {},
    ).get(permission, False)


PASSPORT_PROTOCOL_VERSION = "0.1"


def export_network_passport(network: BGMNetwork) -> dict:
    """Create a portable, non-secret representation of the BGM Network."""

    if not isinstance(network, BGMNetwork):
        raise TypeError("network must be a BGMNetwork.")

    return {
        "passport_version": PASSPORT_PROTOCOL_VERSION,
        "identity_id": network.identity_id,
        "devices": dict(network.devices),
        "permissions": {
            participant_id: dict(permission_map)
            for participant_id, permission_map
            in network.permissions.items()
        },
    }


def network_passport_version() -> str:
    """Return the current Network Passport protocol version."""

    return PASSPORT_PROTOCOL_VERSION
