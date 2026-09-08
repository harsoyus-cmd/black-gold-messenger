"""
BGM P2P Transport
Black Gold Messenger

Reliable TCP transport foundation.
"""

from dataclasses import dataclass
import socket
import struct


TRANSPORT_PROTOCOL_VERSION = "0.1"
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 38472
DEFAULT_TIMEOUT = 10.0
MAX_FRAME_SIZE = 1024 * 1024


class BGMTransportError(Exception):
    """Base exception for BGM transport errors."""


class BGMTransportConnectionError(BGMTransportError):
    """Raised when a transport connection cannot be established."""


class BGMTransportFrameError(BGMTransportError):
    """Raised when a transport frame is invalid."""


@dataclass(frozen=True)
class BGMTransportEndpoint:
    """Represents a TCP transport endpoint."""

    host: str
    port: int

    def is_valid(self) -> bool:
        """Perform basic endpoint validation."""

        return bool(
            self.host
            and 1 <= self.port <= 65535
        )


def encode_frame(payload: bytes) -> bytes:
    """
    Encode a payload using BGM length-prefixed framing.
    """

    if not payload:
        raise BGMTransportFrameError(
            "Payload must not be empty."
        )

    if len(payload) > MAX_FRAME_SIZE:
        raise BGMTransportFrameError(
            "Payload exceeds maximum frame size."
        )

    header = struct.pack(
        "!I",
        len(payload),
    )

    return header + payload


def _receive_exact(
    sock: socket.socket,
    size: int,
) -> bytes:
    """Receive exactly size bytes from a socket."""

    data = bytearray()

    while len(data) < size:
        chunk = sock.recv(size - len(data))

        if not chunk:
            raise BGMTransportConnectionError(
                "Connection closed while receiving data."
            )

        data.extend(chunk)

    return bytes(data)


def decode_frame(
    sock: socket.socket,
) -> bytes:
    """
    Receive and decode one BGM framed payload.
    """

    header = _receive_exact(
        sock,
        4,
    )

    payload_length = struct.unpack(
        "!I",
        header,
    )[0]

    if payload_length == 0:
        raise BGMTransportFrameError(
            "Frame payload must not be empty."
        )

    if payload_length > MAX_FRAME_SIZE:
        raise BGMTransportFrameError(
            "Frame exceeds maximum size."
        )

    return _receive_exact(
        sock,
        payload_length,
    )


class BGMTransportConnection:
    """Represents one connected BGM TCP peer."""

    def __init__(
        self,
        sock: socket.socket,
        endpoint: BGMTransportEndpoint,
    ) -> None:
        self.socket = sock
        self.endpoint = endpoint
        self.closed = False

    def send(self, payload: bytes) -> None:
        """Send one framed BGM payload."""

        if self.closed:
            raise BGMTransportConnectionError(
                "Connection is closed."
            )

        frame = encode_frame(payload)

        try:
            self.socket.sendall(frame)
        except OSError as exc:
            self.closed = True
            raise BGMTransportConnectionError(
                "Failed to send data."
            ) from exc

    def receive(self) -> bytes:
        """Receive one framed BGM payload."""

        if self.closed:
            raise BGMTransportConnectionError(
                "Connection is closed."
            )

        try:
            return decode_frame(self.socket)
        except OSError as exc:
            self.closed = True
            raise BGMTransportConnectionError(
                "Failed to receive data."
            ) from exc

    def close(self) -> None:
        """Close the transport connection."""

        if not self.closed:
            try:
                self.socket.shutdown(
                    socket.SHUT_RDWR
                )
            except OSError:
                pass

            try:
                self.socket.close()
            finally:
                self.closed = True


class BGMTransportServer:
    """TCP listener for incoming BGM connections."""

    def __init__(
        self,
        host: str = DEFAULT_HOST,
        port: int = DEFAULT_PORT,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> None:
        if not 1 <= port <= 65535:
            raise ValueError(
                "Port must be between 1 and 65535."
            )

        if timeout <= 0:
            raise ValueError(
                "Timeout must be greater than zero."
            )

        self.endpoint = BGMTransportEndpoint(
            host=host,
            port=port,
        )
        self.timeout = timeout
        self.socket: socket.socket | None = None

    def start(self) -> None:
        """Start the TCP listener."""

        if self.socket is not None:
            raise BGMTransportError(
                "Transport server is already running."
            )

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
        )

        try:
            sock.setsockopt(
                socket.SOL_SOCKET,
                socket.SO_REUSEADDR,
                1,
            )
            sock.bind(
                (
                    self.endpoint.host,
                    self.endpoint.port,
                )
            )
            sock.listen(5)
            sock.settimeout(self.timeout)
            self.socket = sock
        except OSError as exc:
            sock.close()
            raise BGMTransportConnectionError(
                "Failed to start transport server."
            ) from exc

    def accept(
        self,
    ) -> BGMTransportConnection | None:
        """Accept one incoming connection."""

        if self.socket is None:
            raise BGMTransportError(
                "Transport server is not running."
            )

        try:
            client_socket, address = self.socket.accept()
        except socket.timeout:
            return None
        except OSError as exc:
            raise BGMTransportConnectionError(
                "Failed to accept connection."
            ) from exc

        client_socket.settimeout(self.timeout)

        endpoint = BGMTransportEndpoint(
            host=address[0],
            port=address[1],
        )

        return BGMTransportConnection(
            client_socket,
            endpoint,
        )

    def close(self) -> None:
        """Stop the TCP listener."""

        if self.socket is not None:
            try:
                self.socket.close()
            finally:
                self.socket = None


def connect(
    host: str,
    port: int,
    timeout: float = DEFAULT_TIMEOUT,
) -> BGMTransportConnection:
    """Connect to a BGM TCP transport endpoint."""

    endpoint = BGMTransportEndpoint(
        host=host,
        port=port,
    )

    if not endpoint.is_valid():
        raise ValueError(
            "Invalid transport endpoint."
        )

    if timeout <= 0:
        raise ValueError(
            "Timeout must be greater than zero."
        )

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
    )

    try:
        sock.settimeout(timeout)
        sock.connect(
            (
                endpoint.host,
                endpoint.port,
            )
        )
    except OSError as exc:
        sock.close()
        raise BGMTransportConnectionError(
            "Failed to connect to peer."
        ) from exc

    return BGMTransportConnection(
        sock,
        endpoint,
    )
