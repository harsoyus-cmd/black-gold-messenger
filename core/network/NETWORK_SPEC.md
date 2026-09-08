# BGM Network Specification

Black Gold Messenger — by Grand Visioner

## 1. Purpose

BGM Network is the personal communication network layer of BGM.

It connects one BGM Identity with trusted devices, contacts,
communication permissions, and the BGM Network Passport.

Core principle:

> Your Identity. Your Devices. Your Network.

## 2. Responsibilities

BGM Network is responsible for:

- network identity reference
- trusted device management
- device trust state
- communication permissions
- personal network configuration
- BGM Network Passport foundation

## 3. Non-Responsibilities

BGM Network must not:

- replace BGM Identity
- implement cryptography
- implement message encryption
- implement peer discovery
- implement TCP transport
- implement offline delivery
- implement UI
- implement translation
- implement wallet or blockchain
- implement voice or video calls

## 4. Identity

One BGM Identity may control multiple trusted devices.

The Network layer references the existing BGM Identity.

It must not create a second identity system.

## 5. Trusted Devices

Each device has:

- device_id
- device status
- trust state
- registration information

A trusted device may participate in the owner's BGM Network.

A revoked device must no longer be considered trusted.

## 6. Device Trust States

MVP states:

- PENDING
- TRUSTED
- REVOKED

State flow:

PENDING -> TRUSTED
TRUSTED -> REVOKED

A revoked device must not automatically return to TRUSTED.

Re-authorization is a future security-controlled operation.

## 7. Communication Permissions

Permissions define which communication capabilities a network
participant may use.

Initial permission types:

- CHAT
- MAIL
- FILE
- MEDIA
- CALL

The CALL permission is reserved for future voice/video features.

Permissions are independent from message encryption.

## 8. Permission Principle

A permission grants capability.

A missing permission means the capability is not granted.

The Network layer does not perform the communication itself.

It only provides the authorization state to higher layers.

## 9. Network Identity

BGM Network has a network identity reference associated with the
owner's BGM Identity.

The Network identity must remain linked to the existing identity
architecture.

No duplicate root identity is created.

## 10. Network Passport

BGM Network Passport is the portable representation of a user's
personal network configuration.

The MVP foundation may contain:

- passport version
- BGM Identity reference
- trusted device references
- communication permission state
- network configuration reference

Sensitive cryptographic secrets must not be stored in plaintext
inside the Passport.

Secure export and recovery are future security work.

## 11. Portability

The long-term goal is:

> Move your network, not just your account.

A user should eventually be able to migrate the BGM Network to
another device without rebuilding the entire network manually.

Migration security is a future hardening phase.

## 12. Architecture

BGM Network sits above the existing communication foundation:

BGM Identity
    ->
BGM Network
    ->
Trusted Devices / Permissions
    ->
Discovery / Secure Session / Transport
    ->
Messages / Mail / Media

BGM Network does not replace lower communication layers.

## 13. Resource Constraints

The Network layer must remain lightweight.

MVP requirements:

- small in-memory structures
- no permanent background worker
- no unnecessary threads
- bounded data
- minimal storage overhead
- modular components

## 14. Future Extensions

Future versions may add:

- device pairing
- QR-based device authorization
- device revocation hardening
- network recovery
- secure Passport export/import
- contact trust
- group permissions
- browser/device pairing
- network migration
- stronger device authentication

## 15. MVP Acceptance Criteria

BGM Network MVP foundation must be able to:

1. reference an existing BGM Identity
2. register a device
3. track device trust state
4. revoke a trusted device
5. define communication permissions
6. expose network configuration
7. provide a foundation for BGM Network Passport
8. remain independent from Crypto, Transport, Discovery, Storage,
   Text Engine, and UI
9. remain lightweight for low-resource devices

BGM Network Specification v0.1 Draft
