# BGM Peer Discovery Specification

**Project:** Black Gold Messenger  
**Version:** 0.1 Draft  
**Status:** Foundation

## 1. Purpose

BGM Peer Discovery allows BGM devices to discover reachable peers without requiring a central server.

## 2. Initial MVP Scope

The first implementation targets devices connected to the same local network.

Supported initial transport environments:

- Wi-Fi LAN
- Local IPv4 network
- Android and Linux-compatible environments

Long-range radio, Internet-wide discovery, and mesh routing are deferred to later phases.

## 3. Discovery Principles

Peer discovery MUST:

- avoid exposing private cryptographic keys
- use BGM Identity IDs as public identifiers
- provide reachable network information
- allow peers to establish a connection
- tolerate peers appearing and disappearing
- avoid requiring a central discovery server

## 4. Discovery Information

A discovery announcement may contain:

- Protocol version
- BGM Identity ID
- Device ID
- Device display name
- Network address
- Discovery port
- Timestamp
- Discovery nonce

Private keys MUST NOT be included.

## 5. Local Discovery

The MVP may use local-network discovery mechanisms such as UDP broadcast or multicast.

The discovery mechanism is only for finding peers.

It MUST NOT be treated as proof of identity.

## 6. Identity Verification

Discovery identifies a potentially reachable device.

Cryptographic authentication MUST occur during secure session establishment.

A discovered BGM ID alone MUST NOT prove ownership.

## 7. Peer Lifecycle

A peer may have these states:

- DISCOVERED
- CONNECTING
- CONNECTED
- DISCONNECTED
- EXPIRED

## 8. Expiration

Discovery records MUST have a limited lifetime.

A peer that stops announcing itself MUST eventually be removed from the active peer list.

## 9. Security Boundary

Discovery metadata may be visible to devices on the same network.

Confidential message content MUST NOT be transmitted through discovery.

## 10. Future Extensions

Future versions may support:

- Bluetooth discovery
- Wi-Fi Direct
- Internet peer discovery
- relay-assisted discovery
- decentralized discovery
- mesh discovery
- external long-range radio hardware

## 11. Production Requirement

Before production release, discovery requires:

- authenticated session establishment
- replay protection
- malformed packet handling
- peer expiration
- network abuse protection
- interoperability testing
