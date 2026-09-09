# BGM Identity Profile & Device Context

Version: 0.1.0

## 1. Purpose

Define the identity and device information
presented in the BGM Profile interface.

## 2. Identity Display

When an identity is available, display:

- BGM identity ID
- identity availability status

The identity ID is the primary identity
information shown to the user.

## 3. Identity State

The UI may represent:

- Identity Available
- Identity Not Available
- Identity Loading
- Identity Error

The displayed state must reflect the existing
BGM identity layer.

## 4. Identity Creation

If no identity exists:

Action:
Create Identity

Identity creation is delegated to the existing
BGM identity/core layer.

The UI must not implement:

- key generation
- cryptographic operations
- private key storage

## 5. Identity Error

If identity initialization fails:

Title:
Unable to load identity

Supporting message:
Please try again.

Action:
Retry

Do not display incomplete identity information.

## 6. Private Information

The UI must never display:

- private keys
- secret keys
- raw cryptographic secrets

Only public/appropriate identity information
may be presented.

## 7. Device Context

The profile may display lightweight device
context when available.

Examples:

- current device status
- device availability
- application version

Do not expose unnecessary hardware information.

## 8. Multiple Devices

Advanced multi-device management is deferred.

The MVP does not add:

- device pairing dashboards
- device transfer workflows
- remote device administration
- complex device synchronization

## 9. Core Boundary

The UI consumes identity information from the
existing BGM identity/service layer.

It does not duplicate identity storage,
generation, validation, or cryptography.

## 10. Loading Behavior

Identity information should load quickly.

Avoid loading unrelated:

- conversations
- communities
- radio stations
- media
- mail

when opening Profile.

## 11. Accessibility

Use:

- readable identity text
- clear identity state
- approximately 44x44px action areas
- support larger system text
- status information that does not depend only
  on color

## 12. Low-RAM Rules

Avoid:

- large identity graphics
- animated identity effects
- QR/video identity interfaces in the MVP
- unnecessary background identity processing

## 13. Visual Character

Identity presentation should feel:

- private
- secure
- premium
- calm
- trustworthy

The identity ID should be visually prominent
without using excessive gold or decoration.
