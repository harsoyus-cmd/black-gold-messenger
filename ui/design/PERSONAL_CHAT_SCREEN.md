# BGM Personal Chat Screen

Version: 0.1.0

## 1. Purpose

Define the primary personal conversation screen
for one-to-one BGM messaging.

## 2. Screen Structure

Personal Chat contains:

- top app bar
- message list
- message composer
- optional conversation status

The layout must remain simple and readable.

## 3. Top App Bar

Display:

- contact identity name
- connection or conversation status when relevant
- back navigation

Optional actions may be added later.

The identity name has visual priority.

## 4. Message List

Messages are displayed chronologically.

Each message may contain:

- message text
- timestamp
- delivery status when available

The latest messages should remain visible
when the conversation opens.

## 5. Message Appearance

Outgoing messages:

- visually distinct from incoming messages
- may use restrained BGM_GOLD emphasis

Incoming messages:

- use BGM_SURFACE or BGM_SURFACE_2
- maintain strong text contrast

Avoid excessive gold.

## 6. Message Text

Primary chat text target:

- 16–18px
- high contrast
- comfortable line spacing

Long messages must wrap naturally.

Do not use tiny text to fit content.

## 7. Empty Conversation

When no messages exist:

Title:
No messages yet

Supporting message:
Send a message to start the conversation.

The composer remains immediately available.

## 8. Navigation

Back returns to the previous conversation list
or originating destination.

Opening a conversation must not duplicate
the entire Home screen.

## 9. Core Integration Boundary

The UI must use the existing BGM core for:

- identity
- message creation
- message storage
- delivery state
- network processing

The UI must not duplicate encryption,
message protocol, or storage logic.

## 10. Low-RAM Rules

Avoid:

- rendering the entire message history at once
- heavy message animations
- video backgrounds
- blur effects
- unnecessary image loading
- duplicated conversation data

Use a lightweight scrolling message list.

## 11. Accessibility

Minimum targets:

- body/chat text: 16px
- interactive controls: approximately 44x44px

Support larger system text sizes
without overlapping controls.

## 12. Visual Character

The screen should feel:

- premium
- calm
- private
- familiar
- fast

It must not feel:

- like a game
- overly futuristic
- crowded
- decorative
- like a copy of another messenger.
