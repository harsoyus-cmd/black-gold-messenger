# BGM Text Engine Specification

**Project:** Black Gold Messenger (BGM)  
**Module:** Text Engine  
**Protocol Version:** 0.1 Draft  
**Status:** MVP Foundation

## 1. Purpose

The BGM Text Engine provides the application-layer processing required
to create, validate, encrypt, decrypt, and recover BGM text messages.

The Text Engine does not own networking, identity management,
cryptographic key generation, discovery, or persistent storage.

## 2. Responsibilities

The Text Engine is responsible for:

- validating text content
- creating BGM text messages
- converting text to bytes
- encrypting text payloads
- decrypting text payloads
- validating encrypted payloads
- recovering decrypted text

## 3. Non-Responsibilities

The Text Engine must not:

- generate identity keys
- generate session keys
- perform peer discovery
- open network connections
- manage TCP transport
- manage persistent storage
- implement UI
- implement database logic
- manage device registration
- replace the BGM Message Protocol
- replace the BGM Cryptography module

## 4. Processing Flow

The intended MVP flow is:

Identity
→ Secure Session
→ Session Key
→ Text Engine
→ E2EE
→ Protocol
→ Transport

Receiving follows the reverse path:

Transport
→ Protocol
→ Secure Session
→ Session Key
→ Text Engine
→ E2EE
→ Plain Text

## 5. Encryption

Text payloads use the existing BGM E2EE implementation.

Current foundation:

- ChaCha20-Poly1305
- 32-byte symmetric encryption key
- 12-byte random nonce
- authenticated encryption
- optional associated data
- explicit key identifier

The Text Engine must never implement a second encryption algorithm.

## 6. Session Keys

Session keys are supplied by the BGM Secure Session layer.

The Text Engine must not:

- generate session keys
- derive session keys
- persist session keys
- modify session keys

For sending, the caller supplies the session `send_key`.

For receiving, the caller supplies the session `receive_key`.

## 7. Text Encoding

BGM Text Engine uses UTF-8 for text encoding.

This allows support for:

- Indonesian
- English
- Unicode characters
- emoji
- international languages

Invalid text input must be rejected before encryption.

## 8. Empty Messages

Empty text messages are invalid.

Whitespace-only messages are also rejected at the Text Engine layer.

## 9. Message Types

Text messages use:

`MessageType.TEXT`

The Text Engine must not create IMAGE, FILE, VIDEO, AUDIO, VOICE,
or SYSTEM messages.

Those types belong to their respective future modules.

## 10. Message Envelope

The Text Engine creates or processes the payload portion of a
`BGMMessage`.

The existing BGM Message Protocol remains authoritative for:

- message ID
- sender identity ID
- sender device ID
- recipient identity ID
- timestamp
- message type
- protocol version

## 11. Associated Data

When the caller supplies associated data, it must be passed unchanged
to the BGM E2EE layer.

Future versions may bind authenticated protocol metadata to the
encrypted payload.

The Text Engine must not invent metadata binding rules outside the
defined protocol.

## 12. Security Boundary

The Text Engine is not a cryptographic authority.

Security-sensitive operations remain inside:

`core/crypto/`

The Text Engine only consumes the cryptographic API exposed by that
module.

## 13. Resource Constraints

The MVP implementation should remain lightweight.

The Text Engine should:

- avoid unnecessary dependencies
- avoid large temporary buffers
- avoid background workers
- avoid caching message payloads
- process one text message at a time

The implementation must remain suitable for low-resource Android
devices.

## 14. Error Handling

Invalid input must produce explicit exceptions.

The Text Engine must never silently:

- modify text
- truncate text
- replace characters
- bypass encryption
- accept an empty message

## 15. Versioning

Current Text Engine version:

`0.1`

The Text Engine must remain compatible with the BGM Message Protocol
and BGM E2EE protocol versions it supports.

## 16. Future Work

The following are intentionally outside the MVP foundation:

- message authentication binding
- production replay protection
- secure key storage
- key rotation
- ratcheting
- multi-device security hardening
- offline queue
- persistent message storage
- delivery receipts
- read receipts
- typing indicators
- group messaging
- media messaging

These will be implemented in later modules.

## 17. MVP Success Criteria

The Text Engine foundation is considered successful when it can:

1. accept valid text
2. reject invalid or empty text
3. encode text as UTF-8
4. encrypt the text using a supplied session key
5. produce an authenticated encrypted payload
6. decrypt the payload using the correct receive key
7. reject tampered ciphertext
8. recover the original text exactly

---

**BGM Text Engine v0.1 Draft**
