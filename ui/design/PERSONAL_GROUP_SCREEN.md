# BGM Personal Group Screen

Version: 0.1.0

## 1. Purpose

Define the primary screen for BGM personal group
conversations.

## 2. Screen Structure

Personal Group contains:

- top app bar
- group information context
- message list
- message composer

The structure should remain familiar to the
personal chat experience.

## 3. Top App Bar

Display:

- group name
- member count when available
- back navigation

Optional group actions are deferred.

The group name has visual priority.

## 4. Group Information

The screen may show compact group context:

- group name
- member count

Detailed member management belongs to a separate
group interface.

## 5. Message List

Messages are displayed chronologically.

Each message may contain:

- sender identity
- message text
- timestamp
- delivery status when available

The sender identity is important because multiple
people participate in the conversation.

## 6. Message Appearance

Incoming and outgoing messages should follow
the established BGM message bubble system.

Outgoing messages:

- restrained BGM_GOLD emphasis

Incoming messages:

- BGM_SURFACE or BGM_SURFACE_2

Do not introduce a separate visual language
for groups.

## 7. Empty Group

When no messages exist:

Title:
No messages yet

Supporting message:
Send a message to start the group conversation.

The composer remains available.

## 8. Navigation

Back returns to the originating conversation
list or previous destination.

Opening a group must not duplicate the entire
Home screen.

## 9. Core Integration Boundary

The UI delegates group behavior to the existing
BGM group and messaging layers.

The UI must not duplicate:

- membership logic
- group targeting
- message creation
- encryption
- storage
- delivery processing

## 10. Low-RAM Rules

Avoid:

- loading the entire message history at once
- loading all member profiles unnecessarily
- animated avatars
- heavy shadows
- blur effects
- unnecessary media previews

Only required group data should be loaded.

## 11. Accessibility

Target:

- chat text: 16–18px
- interactive controls: approximately 44x44px
- support larger system text sizes

## 12. Visual Character

The group screen should feel:

- private
- organized
- premium
- calm
- familiar

It must not become crowded as member count
increases.
