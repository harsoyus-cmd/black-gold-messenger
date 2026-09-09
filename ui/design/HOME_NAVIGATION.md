# BGM Home Navigation System

Version: 0.1.0

## 1. Primary Navigation

BGM primary navigation contains four sections:

1. Chat
2. World
3. Radio
4. Profile

These are the main destinations of the application.

## 2. Bottom Navigation

Default placement:
Bottom of the screen.

Items:

Chat
World
Radio
Profile

The active destination uses:
- BGM_GOLD
- clear icon state
- readable label

Inactive destinations use:
- BGM_TEXT_SECONDARY
- neutral icon state

Do not use excessive glow.

## 3. Navigation Icons

Icons must be:

- simple
- recognizable
- consistent
- lightweight

Avoid:
- detailed illustrations
- animated icons
- oversized icons
- decorative effects

## 4. Bottom Navigation Height

The navigation area must provide comfortable
touch targets without consuming excessive screen space.

Each destination must have a minimum comfortable
interactive area of approximately 44 × 44 px.

## 5. App Bar

The top area may contain:

- current screen title
- identity/user context
- screen-specific action

The app bar must remain visually simple.

## 6. Home App Bar

Default Home title:

BGM

The logo may be displayed when the final approved
logo asset becomes available.

## 7. Active State

The active navigation destination must be obvious
without relying on color alone.

Use a combination of:
- icon state
- label state
- subtle gold accent

## 8. Navigation State

Only the currently selected destination should
receive active styling.

Do not illuminate all navigation items simultaneously.

## 9. Back Navigation

Back behavior must follow the logical navigation stack.

From a detail screen:
Back returns to the previous screen.

From a root destination:
Back behavior is handled by the application shell.

## 10. Low-RAM Rules

Navigation must avoid:

- heavy animations
- animated backgrounds
- blur effects
- unnecessary screen duplication
- loading all destination data simultaneously

Destination content should be initialized on demand.

## 11. Future Extension

Additional destinations may be introduced later,
but the primary navigation should remain limited
to the core BGM experience unless a future roadmap
explicitly changes it.
