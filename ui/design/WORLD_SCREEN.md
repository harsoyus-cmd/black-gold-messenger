# BGM World Screen

Version: 0.1.0

## 1. Purpose

Define the primary BGM World interface.

World provides structured discovery of:

World
    ↓
Continent
    ↓
Country
    ↓
Community

## 2. Screen Structure

World contains:

- top app bar
- continent list
- lightweight navigation
- optional search action for future use

The initial MVP prioritizes browsing.

## 3. Top App Bar

Display:

- title: World
- back navigation when applicable

The title should have clear visual priority.

## 4. Continent List

Each continent item may display:

- continent name
- available country count when available

Items should remain compact and easy to scan.

## 5. Country Navigation

Selecting a continent opens its countries.

Selecting a country opens its communities.

Navigation should preserve the user's current
position in the World hierarchy.

## 6. Community Navigation

Selecting a community opens its community
interface.

Community membership and discussion behavior
remain controlled by the existing BGM core.

## 7. Empty State

If no items are available:

Title:
Nothing here yet

Supporting message:
No available locations or communities.

Keep the state simple and readable.

## 8. Loading State

World data should load progressively.

Load only the level currently being viewed.

Avoid loading the complete World hierarchy
at startup.

## 9. Error State

If World data cannot be loaded:

Title:
Unable to load World

Supporting message:
Please try again.

Action:
Retry

## 10. Core Integration Boundary

The UI delegates World data to the existing
BGM World layer.

The UI must not duplicate:

- continent data
- country data
- community data
- membership rules
- discussion logic

## 11. Low-RAM Rules

Avoid:

- loading every country at startup
- loading every community at startup
- heavy map rendering
- animated globe graphics
- video backgrounds
- large cached lists

Use lightweight scrolling lists.

## 12. Accessibility

Use:

- readable 16–18px list text
- approximately 44x44px touch targets
- clear hierarchy
- support for larger system text

## 13. Visual Character

World should feel:

- organized
- global
- premium
- calm
- lightweight

Do not use a decorative 3D globe or game-like
world interface for the initial MVP.
