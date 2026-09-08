"""
BGM Peer Discovery
Black Gold Messenger

Local-network peer discovery foundation.
"""

from dataclasses import dataclass
import json
import socket
import time


DISCOVERY_PROTOCOL_VERSION = "0.1"
DISCOVERY_PORT = 38471
DISCOVERY_MESSAGE_TYPE = "BGM_DISCOVERY"
PEER_EXPIRATION_SECONDS = 30.0


@dataclass(frozen=True)
class BGMDiscoveredPeer:
    """Represents a discovered BGM peer."""

    identity_id: str
    device_id: str
    address: str
    port: int
    timestamp: float
    display_name: str = ""

    def is_valid(self) -> bool:
        """Perform basic peer validation."""

        return bool(
            self.identity_id
            and self.device_id
            and self.address
            and 1 <= self.port <= 65535
            and self.timestamp > 0
        )


def create_discovery_packet(
    identity_id: str,
    device_id: str,
    port: int = DISCOVERY_PORT,
    display_name: str = "",
) -> bytes:
    """Create a local-network discovery announcement."""

    if not identity_id:
        raise ValueError("Identity ID must not be empty.")

    if not device_id:
        raise ValueError("Device ID must not be empty.")

    if not 1 <= port <= 65535:
        raise ValueError("Port must be between 1 and 65535.")

    packet = {
        "type": DISCOVERY_MESSAGE_TYPE,
        "version": DISCOVERY_PROTOCOL_VERSION,
        "identity_id": identity_id,
        "device_id": device_id,
        "port": port,
        "display_name": display_name,
        "timestamp": time.time(),
    }

    return json.dumps(
        packet,
        separators=(",", ":"),
    ).encode("utf-8")


def parse_discovery_packet(
    data: bytes,
    address: str,
) -> BGMDiscoveredPeer:
    """Parse and validate a discovery announcement."""

    if not data:
        raise ValueError("Discovery packet must not be empty.")

    try:
        packet = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("Invalid discovery packet.") from exc

    if packet.get("type") != DISCOVERY_MESSAGE_TYPE:
        raise ValueError("Invalid discovery message type.")

    if packet.get("version") != DISCOVERY_PROTOCOL_VERSION:
        raise ValueError("Unsupported discovery protocol version.")

    peer = BGMDiscoveredPeer(
        identity_id=packet.get("identity_id", ""),
        device_id=packet.get("device_id", ""),
        address=address,
        port=int(packet.get("port", 0)),
        timestamp=float(packet.get("timestamp", 0)),
        display_name=packet.get("display_name", ""),
    )

    if not peer.is_valid():
        raise ValueError("Invalid discovered peer.")

    return peer


class BGMDiscovery:
    """UDP-based local-network peer discovery."""

    def __init__(
        self,
        identity_id: str,
        device_id: str,
        port: int = DISCOVERY_PORT,
        display_name: str = "",
    ) -> None:
        self.identity_id = identity_id
        self.device_id = device_id
        self.port = port
        self.display_name = display_name
        self.peers: dict[tuple[str, str], BGMDiscoveredPeer] = {}

    def create_packet(self) -> bytes:
        """Create this device's discovery packet."""

        return create_discovery_packet(
            identity_id=self.identity_id,
            device_id=self.device_id,
            port=self.port,
            display_name=self.display_name,
        )

    def send_broadcast(
        self,
        broadcast_address: str = "255.255.255.255",
    ) -> None:
        """Broadcast this device's presence on the local network."""

        packet = self.create_packet()

        with socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM,
        ) as sock:
            sock.setsockopt(
                socket.SOL_SOCKET,
                socket.SO_BROADCAST,
                1,
            )
            sock.sendto(
                packet,
                (broadcast_address, self.port),
            )

    def add_peer(
        self,
        peer: BGMDiscoveredPeer,
    ) -> None:
        """Add or refresh a discovered peer."""

        if not peer.is_valid():
            raise ValueError("Invalid peer.")

        if (
            peer.identity_id == self.identity_id
            and peer.device_id == self.device_id
        ):
            return

        key = (peer.identity_id, peer.device_id)
        self.peers[key] = peer

    def remove_expired_peers(
        self,
        now: float | None = None,
    ) -> int:
        """Remove peers that have not announced recently."""

        current_time = time.time() if now is None else now

        expired_keys = [
            key
            for key, peer in self.peers.items()
            if current_time - peer.timestamp > PEER_EXPIRATION_SECONDS
        ]

        for key in expired_keys:
            del self.peers[key]

        return len(expired_keys)

    def get_peers(self) -> list[BGMDiscoveredPeer]:
        """Return currently tracked peers."""

        self.remove_expired_peers()
        return list(self.peers.values())

    def listen_once(
        self,
        timeout: float = 2.0,
    ) -> BGMDiscoveredPeer | None:
        """Listen for one discovery announcement."""

        if timeout <= 0:
            raise ValueError("Timeout must be greater than zero.")

        with socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM,
        ) as sock:
            sock.setsockopt(
                socket.SOL_SOCKET,
                socket.SO_REUSEADDR,
                1,
            )
            sock.bind(("", self.port))
            sock.settimeout(timeout)

            try:
                data, address = sock.recvfrom(4096)
            except socket.timeout:
                return None

        peer = parse_discovery_packet(
            data,
            address[0],
        )

        self.add_peer(peer)

        return peer
