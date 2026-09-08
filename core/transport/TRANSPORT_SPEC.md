# BGM P2P Transport Specification

**Project:** Black Gold Messenger  
**Version:** 0.1 Draft  
**Status:** Foundation

## 1. Purpose

BGM P2P Transport provides direct network communication between BGM devices.

The transport layer is responsible for moving BGM protocol data between peers.

## 2. Initial MVP Scope

The first implementation targets:

- TCP over IPv4
- Android and Linux-compatible environments
- Direct peer-to-peer connections on reachable networks
- Reliable ordered byte streams

Internet-wide connectivity, relay transport, NAT traversal, and mesh routing are deferred to later phases.

## 3. Transport Principles

Transport MUST:

- support direct peer connections
- provide reliable data delivery
- preserve message boundaries through BGM framing
- detect connection closure
- handle connection timeouts
- avoid transmitting private cryptographic keys
- remain independent from message encryption

## 4. Separation of Responsibilities

Transport is responsible for:

- opening connections
- accepting connections
- sending framed data
- receiving framed data
- connection lifecycle
- network errors

Transport is NOT responsible for:

- identity authentication
- message encryption
- message authorization
- application-level message interpretation

Those responsibilities belong to higher BGM layers.

## 5. Connection Model

A BGM peer may operate as:

- CONNECTOR
- LISTENER

A device may perform both roles simultaneously.

## 6. Addressing

A transport endpoint contains:

- IPv4 address
- TCP port

The peer identity is carried by higher-level BGM protocol data.

An IP address MUST NOT be treated as a BGM identity.

## 7. Message Framing

TCP provides a byte stream and does not preserve application message boundaries.

BGM therefore requires explicit framing.

Initial frame format:

- 4-byte unsigned big-endian payload length
- payload bytes

The maximum accepted payload size MUST be limited.

## 8. Connection Lifecycle

A connection may transition through:

- DISCONNECTED
- CONNECTING
- CONNECTED
- CLOSING
- CLOSED

## 9. Timeouts

Connections MUST support configurable connection and receive timeouts.

A timeout MUST NOT cause the application to hang indefinitely.

## 10. Error Handling

Transport errors MUST be converted into controlled BGM transport errors.

Unexpected network failures MUST NOT crash the application process.

## 11. Security Boundary

Transport does not provide end-to-end encryption.

Encrypted BGM payloads MUST be passed through the transport layer without modification.

Plaintext application messages MUST NOT be assumed secure merely because TCP is used.

## 12. Future Extensions

Future versions may support:

- IPv6
- TLS-like transport protection where appropriate
- NAT traversal
- relay-assisted transport
- QUIC
- Wi-Fi Direct
- Bluetooth transport
- mesh transport
- Internet peer connectivity

## 13. Production Requirements

Before production release, transport requires:

- connection authentication through the BGM secure session layer
- malformed frame protection
- maximum frame size enforcement
- timeout handling
- connection cleanup
- interoperability testing
- network abuse protection
- reconnect strategy
