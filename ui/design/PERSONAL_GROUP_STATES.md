# BGM Personal Group States

Version: 0.1.0

## 1. Purpose

Define visual and interaction states for a BGM
personal group conversation.

## 2. Normal State

When messages are available:

- display messages chronologically
- show sender identity where needed
- keep the latest relevant messages visible
- keep the composer available

## 3. Empty State

When no messages exist:

Title:
No messages yet

Supporting message:
Send a message to start the group conversation.

The composer remains immediately available.

## 4. Loading State

While group data is loading:

- show lightweight progress indication
- preserve the conversation structure when practical

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

The UI must reflect state supplied by the
existing BGM core.

Do not falsely report successful delivery.

## 6. Delivery Failure

When a group message fails:

- keep the message visible
- clearly indicate failure
- provide retry when supported

Retry behavior remains controlled by the
existing BGM delivery system.

## 7. Membership State

If the current identity is no longer a member:

- stop presenting the group as an active
  conversation
- preserve locally available information
  when appropriate
- explain that access is no longer available

Membership decisions remain controlled by the
existing BGM group layer.

## 8. Error State

If group data cannot be loaded:

Title:
Unable to load group

Supporting message:
Please try again.

Action:
Retry

Existing locally available data should remain
accessible when possible.

## 9. Navigation

Back navigation must remain available.

The user must not be trapped in a loading
or error state.

## 10. Core Integration Boundary

The UI consumes state from the existing BGM
group and messaging layers.

The UI must not implement its own:

- membership engine
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
- loading unrelated member media

## 12. Accessibility

Important state information must not depend
only on color.

Use readable text or clear icons when needed.

## 13. Visual Character

All group states should preserve the BGM
visual character:

- black foundation
- restrained gold emphasis
- high readability
- calm presentation
- fast interaction
