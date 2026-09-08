# BGM Mail Specification

Black Gold Messenger — by Grand Visioner

## 1. Purpose

BGM Mail provides peer-to-peer asynchronous communication
between BGM Identities.

BGM Mail is part of the BGM Personal Communication Network.

Core principle:

> Mail without a central mail server.

## 2. Responsibilities

BGM Mail is responsible for:

- mail message structure
- sender and recipient identity references
- mail subject
- mail body
- mail metadata required by the protocol
- encrypted mail payload integration
- mail status foundation

## 3. Non-Responsibilities

BGM Mail must not:

- replace BGM Identity
- implement cryptography
- implement key management
- implement peer discovery
- implement TCP transport
- implement offline delivery
- replace BGM Storage
- implement UI
- implement translation
- require Gmail, SMTP, IMAP, or another centralized mail service
- implement wallet or blockchain
- implement voice or video calls

## 4. Communication Model

BGM Mail uses the BGM communication foundation:

BGM Identity
    ->
BGM Mail
    ->
Encryption / Secure Session
    ->
BGM Storage
    ->
Offline Delivery
    ->
P2P Transport
    ->
Recipient BGM Identity

Mail may be delivered immediately when the recipient is online.

Mail may remain stored as PENDING when the recipient is offline.

## 5. Identity

Every BGM Mail message must reference:

- sender_identity_id
- sender_device_id
- recipient_identity_id

BGM Mail must use the existing BGM Identity system.

It must not create another identity system.

## 6. Mail Content

MVP mail content consists of:

- subject
- body

The body is text-based in the MVP.

Future versions may support:

- attachments
- images
- audio
- video files
- rich content

These must remain separate modules.

## 7. Subject

The mail subject is required for the MVP.

The subject must:

- be a string
- not be empty
- not contain only whitespace

## 8. Body

The mail body must:

- be a string
- not be empty
- not contain only whitespace
- use UTF-8 encoding

Unicode and international languages must be supported.

## 9. Encryption

Mail content must be encrypted before transmission.

The Mail layer may use the existing BGM cryptographic and
secure-session foundation.

BGM Mail must not implement a second encryption system.

The exact production message-authentication and key-lifecycle
hardening remains part of future security work.

## 10. Mail Envelope

The MVP Mail layer should provide the application data required
to construct a BGM message envelope.

The existing BGM Message Protocol remains the transport envelope.

BGM Mail must not modify or replace BGMMessage.

## 11. Mail Status

Initial status model:

PENDING
SENT
DELIVERED
READ
FAILED

These states integrate with the existing BGM Storage and
Offline Delivery foundation.

## 12. Offline Delivery

BGM Mail uses the existing Offline Delivery module.

When the recipient is unavailable:

PENDING
    ->
retry
    ->
SENT

If retry policy is exhausted:

PENDING
    ->
FAILED

The Mail module does not implement its own retry engine.

## 13. Storage

BGM Mail uses the existing BGM Storage layer.

Mail data must not create an independent database.

Encrypted payloads should remain opaque to storage.

## 14. Internationalization

BGM Mail must be international-ready.

The protocol must support:

- Unicode
- UTF-8
- Indonesian
- English
- other languages supported by the application

Translation is an application-layer feature and must remain
separate from the Mail protocol.

## 15. Resource Constraints

BGM Mail must remain lightweight.

MVP requirements:

- bounded message size
- no unnecessary threads
- no permanent background worker
- minimal memory usage
- minimal storage overhead
- modular implementation

Large attachments are future work and must use streaming or
chunked transfer rather than loading the entire file into RAM.

## 16. Security Boundaries

BGM Mail must preserve:

- end-to-end encryption
- identity separation
- device separation
- encrypted payload opacity
- message identifiers
- existing secure-session architecture

Future security work includes:

- stronger metadata binding
- replay hardening
- key rotation
- multi-device security
- secure recovery
- attachment security
- threat modeling
- interoperability testing

## 17. Future Extensions

Future versions may add:

- mail threads
- mail folders
- drafts
- attachments
- mail search
- read receipts
- delivery receipts
- contact permissions
- mail forwarding
- multi-device synchronization
- network migration

## 18. MVP Acceptance Criteria

BGM Mail MVP foundation must be able to:

1. create a valid mail message
2. validate sender identity
3. validate recipient identity
4. validate subject
5. validate body
6. support Unicode text
7. integrate with existing encryption
8. integrate with BGMMessage
9. integrate with existing Storage
10. integrate with existing Offline Delivery
11. remain independent from UI
12. remain independent from centralized email services
13. remain lightweight for low-resource devices

BGM Mail Specification v0.1 Draft
