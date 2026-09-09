# BGM Chat Conversation States

Version: 0.1.0

## 1. Purpose

Define visual and interaction states for a BGM
personal conversation.

## 2. Normal State

When messages are available:

- display messages chronologically
- keep the latest relevant messages visible
- keep composer available

## 3. Empty State

When no messages exist:

Title:
No messages yet

Supporting message:
Send a message to start the conversation.

The composer remains immediately available.

## 4. Loading State

While conversation data is loading:

- show lightweight progress indication
- preserve the chat structure when practical

Avoid:

- large skeleton layouts
- shimmer animation
- animated backgrounds
- unnecessary effects

## 5. Offline State

When network connectivity is unavailable:

- existing local messages remain readable
- composer remains available
- outgoing messages may remain pending

The UI must reflect the state supplied by
the BGM core.

Do not falsely report successful delivery.

## 6. Delivery Failure

When a message fails:

- keep the message visible
- clearly indicate failure
- provide retry when supported

Retry behavior remains controlled by the
existing BGM delivery system.

## 7. Temporary Connection State

When connection processing is active:

- use subtle status indication
- do not block conversation reading
- do not continuously animate the screen

## 8. Error State

If conversation data cannot be loaded:

Title:
Unable to load conversation

Supporting message:
Please try again.

Action:
Retry

Existing locally available data should remain
accessible when possible.

## 9. Navigation During States

Back navigation must remain available.

The user must not be trapped in a loading
or error state.

## 10. Core Integration Boundary

The UI consumes state from the existing BGM core.

The UI must not implement its own:

- network state engine
- delivery engine
- retry engine
- encryption
- storage system

## 11. Low-RAM Rules

Avoid:

- duplicated message lists
- continuous status animation
- background polling from the UI
- unnecessary network requests
- loading unrelated media

## 12. Accessibility

Status information must not rely only on color.

Important states should use readable text,
icons, or other clear indicators when needed.

## 13. Visual Character

All states should preserve the BGM character:

- black foundation
- restrained gold emphasis
- high readability
- calm presentation
- fast interaction
