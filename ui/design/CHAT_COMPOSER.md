# BGM Chat Composer

Version: 0.1.0

## 1. Purpose

Define the message composer for BGM personal chat.

## 2. Composer Structure

The composer contains:

- text input
- send action
- optional attachment action

The initial MVP prioritizes text messaging.

## 3. Text Input

The input should:

- support normal message text
- support multiple lines
- expand vertically within a reasonable limit
- remain easy to read

Target text size:

- 16–18px

Do not use tiny text to fit long messages.

## 4. Send Action

The send action must be:

- clearly visible
- easy to tap
- approximately 44x44px touch area

When the message is sent:

- the input is cleared
- the new message appears in the conversation
- delivery status is provided by the existing BGM core

## 5. Empty Input

When there is no text:

- send action may be disabled or visually de-emphasized

Do not trigger an empty message.

## 6. Attachment Action

An attachment action may be displayed for
future media integration.

Initial supported direction:

- image
- file
- video
- audio

Actual media processing remains handled by
the existing BGM core.

The composer must not implement media
encryption or storage itself.

## 7. Keyboard Behavior

When the keyboard opens:

- composer remains visible
- latest relevant messages remain accessible
- screen must not unnecessarily jump

When the keyboard closes:

- conversation returns to normal layout

## 8. Long Message Input

Long text should remain usable.

The composer may expand until a practical
maximum height, then become internally scrollable.

Do not allow the composer to cover the
entire conversation.

## 9. Interaction

Primary interaction:

Type → Send → Message appears

Avoid unnecessary confirmation dialogs.

## 10. Core Integration Boundary

The UI delegates:

- message creation
- encryption
- message storage
- delivery
- failure handling

to the existing BGM core.

The UI only manages presentation and user input.

## 11. Low-RAM Rules

Avoid:

- animated input backgrounds
- heavy blur
- complex effects
- continuously running processing
- preloading attachment previews

Attachment resources should load only
when requested.

## 12. Accessibility

Use:

- minimum approximately 44x44px touch targets
- readable 16–18px input text
- clear focus indication
- support for larger system text sizes

## 13. Visual Character

The composer should feel:

- simple
- premium
- fast
- familiar
- unobtrusive

It must not dominate the chat screen.
