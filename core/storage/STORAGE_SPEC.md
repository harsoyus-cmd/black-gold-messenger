# BGM Local Storage Specification

**Project:** Black Gold Messenger (BGM)
**Module:** Local Storage
**Protocol Version:** 0.1 Draft
**Status:** MVP Foundation

## 1. Purpose

BGM Local Storage provides lightweight persistent storage for local
BGM application data.

The storage layer must support reliable message persistence while
remaining suitable for low-resource Android devices.

## 2. Responsibilities

The Storage module is responsible for:

- storing BGM messages
- retrieving messages
- updating message status
- storing pending messages
- removing completed messages
- preserving message order
- providing persistent local data

## 3. Non-Responsibilities

The Storage module must not:

- perform encryption
- generate cryptographic keys
- manage identities
- perform peer discovery
- open network connections
- implement TCP transport
- implement UI
- translate messages
- generate message content
- replace the BGM Message Protocol

Encrypted payloads must be stored as received from the protocol layer.

## 4. Storage Strategy

The MVP will use SQLite through Python's standard-library
`sqlite3` module.

No external database dependency is required.

This keeps the foundation lightweight and portable.

## 5. Database Location

The application will provide the database path to the Storage layer.

The Storage module must not assume a fixed Android filesystem path.

## 6. Core Data

The initial storage model must support:

- message ID
- sender identity ID
- sender device ID
- recipient identity ID
- timestamp
- message type
- encrypted payload
- message status
- creation time

## 7. Message Status

Initial statuses:

`PENDING`

`SENT`

`DELIVERED`

`READ`

`FAILED`

Status transitions will be controlled by the application layer.

## 8. Security Boundary

The Storage module does not decrypt message content.

For E2EE messages, the stored payload remains encrypted.

Encryption and decryption remain responsibilities of:

`core/crypto/`

and

`core/text/`

## 9. Resource Constraints

The MVP storage implementation should:

- use SQLite
- avoid loading the entire message database into RAM
- retrieve messages in bounded batches
- avoid unnecessary indexes
- use parameterized SQL
- close database resources correctly
- avoid background workers

## 10. Persistence

Messages must survive:

- application restart
- device restart
- temporary network loss

Offline delivery will use the stored `PENDING` state.

## 11. Ordering

Messages must be retrievable in chronological order.

The primary ordering field is:

`created_at`

Message IDs remain unique identifiers and must not be used as
chronological ordering guarantees.

## 12. Data Integrity

The Storage layer must enforce:

- unique message IDs
- required message fields
- valid message status values
- valid message type values
- parameterized SQL statements

## 13. Future Extensions

Future versions may add:

- conversations
- contacts
- devices
- delivery receipts
- read receipts
- retry counters
- offline queue metadata
- attachments
- media metadata
- database migrations
- storage encryption at rest

These are outside the initial foundation.

## 14. MVP Success Criteria

The Storage foundation is successful when it can:

1. initialize a database
2. create the required schema
3. store a BGM message
4. retrieve a message
5. preserve encrypted payloads
6. update message status
7. retrieve pending messages
8. delete a message
9. preserve data after reopening the database
10. reject invalid data

---

**BGM Local Storage v0.1 Draft**
