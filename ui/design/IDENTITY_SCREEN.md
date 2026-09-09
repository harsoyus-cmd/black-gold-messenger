# BGM Identity Screen

Version: 0.1.0

## 1. Purpose

Provide the user-facing screen for BGM identity status.

The screen belongs to the UI layer.

Identity creation, validation, cryptography,
and persistence remain responsibilities of the BGM core.

## 2. Identity Available

When a valid BGM identity is available, display:

- BGM identity status
- Identity identifier
- Continue action

The identity identifier must remain readable.

## 3. Identity Not Available

When no identity is available, display:

Title:
BGM Identity

Message:
Your BGM identity is not ready yet.

Primary action:
Create Identity

The exact identity-generation process is delegated
to the existing BGM core.

## 4. Identity Creation

The UI must:

1. Request identity creation through the existing core API.
2. Receive the resulting identity.
3. Display the identity status.
4. Continue to Home when successful.

The UI must not implement its own cryptographic
identity-generation algorithm.

## 5. Error State

If identity creation fails:

- show a clear error message
- keep the user on the Identity screen
- provide a Retry action

Do not expose technical stack traces to the user.

## 6. Visual Structure

Recommended order:

BGM logo
    ↓
BGM Identity
    ↓
Identity status / identifier
    ↓
Primary action

Keep the layout centered and uncluttered.

## 7. Low-RAM Rules

Avoid:
- animated backgrounds
- large images
- video
- particle effects
- unnecessary network calls
- heavy UI dependencies

## 8. Future Extension

The screen may later support:

- identity backup
- identity import
- identity recovery
- device management

These features are intentionally deferred.

Do not implement them in UI-02.
