"""
BGM Network package.
"""

from .network import (
    BGMNetwork,
    NETWORK_PROTOCOL_VERSION,
    DEVICE_PENDING,
    DEVICE_TRUSTED,
    DEVICE_REVOKED,
    PERMISSION_CHAT,
    PERMISSION_MAIL,
    PERMISSION_FILE,
    PERMISSION_MEDIA,
    PERMISSION_CALL,
    VALID_PERMISSIONS,
    PASSPORT_PROTOCOL_VERSION,
    register_device,
    trust_device,
    revoke_device,
    get_device_status,
    set_permission,
    is_permission_allowed,
    export_network_passport,
    network_passport_version,
)

__all__ = [
    "BGMNetwork",
    "NETWORK_PROTOCOL_VERSION",
    "DEVICE_PENDING",
    "DEVICE_TRUSTED",
    "DEVICE_REVOKED",
    "PERMISSION_CHAT",
    "PERMISSION_MAIL",
    "PERMISSION_FILE",
    "PERMISSION_MEDIA",
    "PERMISSION_CALL",
    "VALID_PERMISSIONS",
    "PASSPORT_PROTOCOL_VERSION",
    "register_device",
    "trust_device",
    "revoke_device",
    "get_device_status",
    "set_permission",
    "is_permission_allowed",
    "export_network_passport",
    "network_passport_version",
]
