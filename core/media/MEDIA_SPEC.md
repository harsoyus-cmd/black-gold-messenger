# BGM Light Media Specification

## Version

Protocol version: 0.1 Draft

## Purpose

BGM Light Media provides a lightweight application-layer foundation
for transferring media and files through the existing BGM network.

Supported media categories:

- IMAGE
- FILE
- AUDIO
- VIDEO

## Core Principles

BGM Light Media MUST:

- remain modular
- reuse the existing BGM Identity
- reuse the existing BGM Message Protocol
- reuse existing encryption/session infrastructure
- integrate with Local Storage
- integrate with Offline Delivery
- use existing P2P Transport
- avoid loading entire large files into RAM
- support bounded processing
- support future chunked transfer

## Non-Responsibilities

BGM Light Media does not own:

- identity
- cryptographic key management
- peer discovery
- TCP/socket management
- offline delivery policy
- UI
- translation
- voice calls
- video calls
- blockchain
- wallet functionality

## Media Categories

### IMAGE

Photos and other image files.

### FILE

General documents and binary files.

### AUDIO

Music and other audio files.

### VIDEO

Video files.

VIDEO means video-file transfer only.

It does NOT mean live video calling.

## Resource Model

Large media MUST NOT require the entire file to be loaded into memory.

Future implementations SHOULD support:

- chunking
- bounded read buffers
- streaming transfer
- resumable transfer
- transfer progress

## Architecture

BGM Identity
→ Media
→ Encryption
→ Storage
→ Offline Delivery
→ P2P Transport
→ Recipient

## International Readiness

Media metadata MUST remain language-neutral.

Human-readable labels belong to the application/UI layer.

## Lightweight Requirements

The MVP foundation MUST:

- avoid permanent worker processes
- avoid unnecessary background services
- use bounded memory
- avoid unnecessary copies of large data
- keep metadata small
- remain suitable for low-resource devices

## Security

Media content MUST be encrypted before transmission.

The Media layer MUST reuse the existing BGM E2EE infrastructure.

The Media layer MUST NOT create a separate cryptographic system.

## Future Extensions

Future versions may add:

- file metadata
- MIME type
- file size
- content hash
- thumbnails
- chunk manifests
- resumable transfers
- transfer receipts
- attachment expiration
- media caching
- storage quotas
- content-addressed storage

## MVP Acceptance Criteria

The Light Media foundation is complete when:

1. Media categories are defined.
2. Media metadata is separated from transport.
3. Existing BGMMessage remains the transport envelope.
4. Existing E2EE is reused.
5. Large-file processing is designed around bounded memory.
6. Image, File, Audio and Video remain modular.
7. Video file transfer remains separate from video calling.
8. UI remains outside the core Media module.
