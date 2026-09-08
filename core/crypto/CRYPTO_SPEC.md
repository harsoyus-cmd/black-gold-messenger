# BGM Cryptography Specification

**Project:** Black Gold Messenger  
**Specification:** BGM Cryptography / E2EE  
**Version:** 0.1  
**Status:** Draft

---

## 1. Purpose

BGM Cryptography defines the cryptographic foundation for secure end-to-end communication between authorized BGM devices.

The design MUST provide:

- End-to-end encryption
- Message authentication
- Device authentication
- Forward secrecy
- Protection against message tampering
- Replay protection
- Multi-device support
- Server-independent security

---

## 2. Cryptographic Principles

BGM cryptography MUST follow these principles:

1. Private keys MUST remain under device control.
2. Private keys MUST NOT be transmitted through the network.
3. Encryption MUST occur before messages leave the sender device.
4. Decryption MUST occur only on an authorized recipient device.
5. Relays and servers MUST NOT require access to plaintext messages.
6. Cryptographic algorithms MUST use established, audited standards.
7. Random values MUST come from a cryptographically secure random source.
8. Cryptographic protocol versions MUST be explicitly identified.

---

## 3. Identity Keys

Each BGM Identity has cryptographic identity material.

The identity layer MUST support:

```text
BGM Identity
│
├── Identity Public Key
│
└── Authorized Devices
    ├── Device A
    │   ├── Device Public Key
    │   └── Device Private Key
    │
    ├── Device B
    │   ├── Device Public Key
    │   └── Device Private Key
    │
    └── Device C
        ├── Device Public Key
        └── Device Private Key
