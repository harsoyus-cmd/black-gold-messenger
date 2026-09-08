# BGM Message Protocol Specification

**Project:** Black Gold Messenger  
**Specification:** BGM Message Protocol  
**Version:** 0.1  
**Status:** Draft

---

## 1. Purpose

BGM Message Protocol defines the standard structure for messages exchanged between BGM devices.

The protocol is designed for:

- Peer-to-peer communication
- End-to-end encryption
- Offline message delivery
- File and media messages
- Multi-device identity
- Future relay and mesh support
- Server-independent operation

---

## 2. Message Principles

Every BGM message MUST:

1. Have a unique message ID.
2. Identify the sender identity.
3. Identify the sender device.
4. Identify the recipient.
5. Contain a creation timestamp.
6. Contain a protocol version.
7. Support cryptographic authentication.
8. Support future protocol versions.

---

## 3. Message Envelope

A BGM message consists of an outer envelope and an encrypted payload.

```text
BGM Message
│
├── Protocol Version
├── Message ID
├── Sender Identity ID
├── Sender Device ID
├── Recipient Identity ID
├── Timestamp
├── Message Type
├── Cryptographic Metadata
└── Encrypted Payload
