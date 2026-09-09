# BGM Message Bubble & Status

Version: 0.1.0

## 1. Purpose

Define the visual treatment of incoming and outgoing
messages in a BGM personal chat.

## 2. Incoming Message

Incoming messages use:

- BGM_SURFACE or BGM_SURFACE_2
- high-contrast primary text
- compact message spacing

The incoming bubble must remain visually distinct
without excessive decoration.

## 3. Outgoing Message

Outgoing messages use:

- restrained BGM_GOLD emphasis
- dark readable text or high-contrast text
- the same general bubble language as incoming messages

Gold must not dominate the conversation.

## 4. Bubble Shape

Use moderate corner radius.

Recommended:

- 10px to 16px radius
- comfortable internal padding
- compact vertical spacing

Avoid:

- excessive rounding
- oversized bubbles
- heavy shadows
- gradients
- glowing effects on every message

## 5. Message Width

Message bubbles should occupy only the space
needed by their content, within a reasonable
maximum width.

Long messages must wrap naturally.

Do not stretch every message across the screen.

## 6. Timestamp

Timestamp is secondary information.

Use:

- smaller secondary text
- muted contrast
- placement that does not interfere with
  message readability

Do not make timestamps visually dominant.

## 7. Delivery Status

When available, outgoing messages may display:

- pending
- delivered
- failed

The UI reflects the status provided by the
existing BGM core.

The UI must not invent delivery states.

## 8. Failed Message

A failed message should be clearly identifiable.

Recommended:

- subtle BGM_ERROR indication
- retry action when supported

Do not hide the original message content.

## 9. Pending Message

Pending messages should remain visible while
delivery is being processed.

Use subtle visual indication.

Avoid continuous animation.

## 10. Selection and Interaction

Message selection or long-press actions may be
added later.

Initial MVP should prioritize:

- reading
- sending
- delivery visibility

## 11. Accessibility

Message text:

- minimum target 16px
- readable line spacing
- sufficient contrast

Status information must not depend only on color.

## 12. Low-RAM Rules

Avoid:

- animated bubbles
- blur effects
- per-message shadows
- complex gradients
- unnecessary avatars inside every message
- heavy rendering effects

## 13. Visual Character

The message area should feel:

- clean
- private
- premium
- calm
- familiar

It must not resemble a gaming interface
or an overly decorative chat application.
