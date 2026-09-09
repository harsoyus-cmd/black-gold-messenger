# BGM Group Composer & Member Actions

Version: 0.1.0

## 1. Purpose

Define the composer and initial member actions
for BGM personal groups.

## 2. Group Composer

The group composer follows the established
personal chat composer.

Contains:

- text input
- send action
- optional attachment action

Text messaging remains the primary MVP action.

## 3. Message Sending

Primary flow:

Type → Send → Message appears

The UI delegates message creation, encryption,
storage, and delivery to the existing BGM core.

Do not implement a second messaging engine.

## 4. Sender Identity

Group messages must clearly identify the sender.

The UI may display:

- identity name
- identity identifier when no display name exists

Avoid repeating unnecessary identity information
on every message when the conversation context
already makes the sender clear.

## 5. Member Actions

Initial MVP actions are limited to capabilities
already provided by the existing group layer.

Possible actions:

- view members
- add member
- remove member

Only expose an action when the corresponding
core capability is available.

## 6. Membership Rules

The UI must not invent ownership, administrator,
moderator, or permission roles.

Membership decisions remain controlled by the
existing BGM group/community rules.

## 7. Add Member

If supported:

- open a lightweight identity selection flow
- select an identity
- delegate membership change to the core

Do not preload large contact databases.

## 8. Remove Member

If supported:

- clearly identify the selected member
- request confirmation before removal
- delegate the operation to the existing group layer

Do not perform removal only in the UI.

## 9. Composer Keyboard Behavior

When the keyboard opens:

- composer remains visible
- latest relevant messages remain accessible
- screen should not jump unnecessarily

## 10. Attachment Action

Media attachments may use the same direction
as personal chat:

- image
- file
- video
- audio

Actual media processing remains outside the UI.

## 11. Low-RAM Rules

Avoid:

- loading all contacts at once
- large member profile cards
- media preview preloading
- heavy animations
- blur effects
- continuous background processing

Load additional data only when requested.

## 12. Accessibility

Use:

- readable 16–18px text
- approximately 44x44px touch targets
- clear action labels
- support larger system text sizes

## 13. Visual Character

The group composer and member actions should
remain:

- simple
- premium
- organized
- familiar
- lightweight

Do not turn group management into an
administration-style interface.
