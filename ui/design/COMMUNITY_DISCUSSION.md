# BGM Community Discussion

Version: 0.1.0

## 1. Purpose

Define the discussion interface inside a BGM
community.

## 2. Discussion Layout

The screen contains:

- community title in the app bar
- chronological discussion messages
- message composer for eligible members

Messages should remain visually consistent
with the existing BGM chat design.

## 3. Discussion Message

A message may display:

- sender identity
- message text
- message position in chronological order

Sender identity must remain visible so users can
distinguish participants.

## 4. Message Order

Messages are displayed chronologically.

The UI does not alter message ordering supplied
by the community discussion layer.

## 5. Composer

For an eligible community member:

- text input
- send action
- approximately 44x44px touch target

The composer should remain simple and lightweight.

## 6. Membership Boundary

Only the actual community membership state
determines whether discussion participation
is available.

The UI does not independently approve or reject
membership.

## 7. Non-Member State

If the current identity is not a member:

- discussion remains viewable only when the
  underlying community layer permits it
- composer must not be shown as available

The UI must follow the actual core state.

## 8. Empty State

If there are no messages:

Title:
No discussion yet

Supporting message:
Start the first discussion in this community.

For eligible members, keep the composer available.

## 9. Loading State

Load discussion messages progressively.

Do not preload unrelated communities,
World data, radio data, or media.

## 10. Error State

If discussion data cannot be loaded:

Title:
Unable to load discussion

Supporting message:
Please try again.

Action:
Retry

## 11. Core Integration Boundary

The UI delegates discussion validation and
message handling to the existing BGM community
discussion layer.

The UI does not duplicate:

- membership validation
- discussion validation
- message storage rules
- transport rules
- encryption rules

## 12. Low-RAM Rules

Avoid:

- loading the entire discussion history at once
- video or media previews
- heavy message effects
- animated backgrounds
- complex shadows
- unnecessary background processing

Prefer a lightweight chronological list.

## 13. Accessibility

Use:

- readable sender identity
- readable message text
- 16–18px primary text
- approximately 44x44px send action
- support larger system text
- clear distinction between sender and message

## 14. Visual Character

Discussion should feel:

- conversational
- calm
- private
- readable
- premium

Use the existing BGM message bubble language
without copying the personal chat screen blindly.
