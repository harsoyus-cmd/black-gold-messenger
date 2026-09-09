# BGM Home States & Responsive Layout

Version: 0.1.0

## 1. Purpose

Define Home screen behavior for normal, empty, loading, error, and different screen sizes.

## 2. Normal State

When data is available, Home displays:

- primary navigation
- recent conversations
- available quick actions
- relevant identity context

Only required Home data should be loaded.

## 3. Empty State

When no conversations exist:

Title:
No conversations yet

Supporting message:
Start a conversation to see it here.

Provide a clear action to start a new chat.

Keep the screen visually calm.

## 4. Loading State

Loading should be lightweight.

Use:

- simple progress indication
- minimal placeholder content when necessary

Avoid:

- large skeleton layouts
- animated backgrounds
- continuous shimmer effects
- unnecessary screen-wide animation

## 5. Error State

If Home data cannot be loaded:

Title:
Unable to load Home

Supporting message:
Please try again.

Action:
Retry

The error state must not prevent access to other independent BGM destinations when possible.

## 6. Responsive Layout

The Home layout must adapt to available screen size.

Small screens:

- single-column layout
- compact spacing
- readable text
- no horizontal scrolling

Larger screens:

- maintain the same information hierarchy
- allow additional spacing
- avoid unnecessarily stretching content

Do not create a separate design language for larger screens.

## 7. Text Scaling

Home must remain usable when system text size is increased.

Minimum target:

- normal body text: 16px
- important labels: 16–18px
- headings: larger than body text

Content must not overlap when text becomes larger.

## 8. Touch Targets

Interactive controls should provide approximately 44x44px minimum touch area.

Small visual icons may remain smaller inside their touch area.

## 9. Orientation

Initial MVP:

- portrait-first
- landscape should remain functional when supported by the platform

Do not add complex orientation-specific layouts.

## 10. Low-RAM Rules

Avoid:

- duplicated screen trees
- preloading unrelated destinations
- large cached lists
- continuous animations
- video backgrounds
- heavy blur effects

Home should release or minimize resources when leaving the screen.

## 11. Navigation Consistency

The same primary navigation remains available across normal Home usage.

Back navigation must behave predictably.

## 12. Future Extension

Future Home features may include:

- pinned conversations
- unread summary
- mail shortcut
- community activity
- notification center

These are deferred until required.
