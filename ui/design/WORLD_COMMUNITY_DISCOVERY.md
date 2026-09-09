# BGM Community Discovery

Version: 0.1.0

## 1. Purpose

Define the community discovery interface
inside the BGM World hierarchy.

## 2. Navigation Context

The user reaches this screen through:

World
    ↓
Continent
    ↓
Country
    ↓
Community

The selected country remains visible through
the screen title or navigation context.

## 3. Community Item

Each community item may display:

- community name
- short description when available
- member count when available

The community name has visual priority.

## 4. Community Selection

Selecting a community opens its community
interface.

The discovery screen does not perform
membership decisions itself.

## 5. Join State

A community may expose an appropriate state:

- Join
- Request Sent
- Member

The UI must reflect the actual state supplied
by the existing BGM community layer.

Do not invent membership status.

## 6. Empty State

If no communities are available:

Title:
No communities yet

Supporting message:
There are no communities available in this country.

Keep the empty state simple.

## 7. Loading State

Community data should load progressively.

Only communities for the selected country
should be requested.

Avoid loading communities from other countries.

## 8. Error State

If communities cannot be loaded:

Title:
Unable to load communities

Supporting message:
Please try again.

Action:
Retry

## 9. Core Integration Boundary

The UI consumes community data from the
existing BGM community layer.

The UI does not duplicate:

- join request rules
- invitation rules
- membership validation
- removal rules
- discussion logic

## 10. Search

Community search is deferred from the initial MVP.

When introduced later, it should remain lightweight
and operate on the relevant community scope.

## 11. Low-RAM Rules

Avoid:

- loading all communities globally
- large banner image preloading
- video previews
- animated community cards
- heavy shadows
- complex list effects

Text-first discovery is preferred.

## 12. Accessibility

Use:

- readable community names
- readable descriptions
- approximately 44x44px touch targets
- status information that does not depend only
  on color
- support larger system text

## 13. Visual Character

Community discovery should feel:

- welcoming
- organized
- private
- premium
- calm

Use BGM_GOLD selectively for important actions
and active states.
