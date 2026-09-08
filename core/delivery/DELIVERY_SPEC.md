# BGM Offline Delivery Specification

Project: Black Gold Messenger (BGM)
Module: Offline Delivery
Protocol: 0.1 Draft
Status: MVP Foundation

## Purpose

Provides lightweight persistent delivery queue management for messages
that cannot be delivered immediately.

## Responsibilities

- read pending messages from Storage
- process bounded delivery batches
- call the Transport layer
- retry failed delivery attempts
- limit retry attempts
- update message status

## Non-Responsibilities

Delivery must not:

- encrypt or decrypt messages
- manage identities or keys
- perform peer discovery
- create sockets
- implement TCP
- implement UI
- translate messages
- replace Message Protocol
- store messages independently of Storage

## Architecture

BGM Message
  -> Storage
  -> Offline Delivery
  -> P2P Transport
  -> Remote Peer

Storage is the persistent source of truth.

## Status

PENDING -> delivery attempt -> SENT
PENDING -> retry -> SENT
PENDING -> retry limit -> FAILED

Future remote confirmation:
SENT -> DELIVERED -> READ

## Retry

Default maximum attempts: 3

Retries must be bounded. No infinite retry loop.

Retry scheduling is controlled by the application.
No permanent background worker is required for MVP.

## Resource Rules

- bounded batches
- low RAM usage
- lightweight retry metadata
- no unnecessary threads
- no permanent background service

## Transport Boundary

Delivery receives a transport callable from the application.

Delivery does not create or manage sockets.

The existing message_id is preserved for every retry.

## Error Handling

Transport failure keeps the message available for retry.

A failed message is not deleted before the retry limit is reached.

Unexpected programming and storage errors must not be silently ignored.

## MVP Success Criteria

1. Read pending messages.
2. Process a bounded batch.
3. Call Transport.
4. Mark successful sends as SENT.
5. Keep failed messages for retry.
6. Stop after the retry limit.
7. Never delete a pending message prematurely.
8. Work without a permanent background worker.

BGM Offline Delivery v0.1 Draft
