# BGM Community Screen

Version: 0.1.0

## 1. Purpose

Define the main community interface after a
user opens a BGM community.

## 2. Navigation Context

The user reaches this screen through:

World
    ↓
Continent
    ↓
Country
    ↓
Community
    ↓
Community Screen

The selected community remains visible through
the screen title and navigation context.

## 3. Community Header

The header may display:

- community name
- short description when available
- member count when available
- country context when useful

The community name has highest visual priority.

## 4. Main Content

The main community screen provides access to:

- community discussion
- member list
- community information
- membership actions when applicable

Only the currently required community data
should be loaded.

## 5. Discussion Entry

Selecting the discussion area opens the community
discussion interface.

Discussion messages use the existing BGM
community discussion model.

The UI does not create a separate messaging
protocol.

## 6. Member Entry

Selecting the member area opens the community
member list.

Membership data comes from the existing BGM
community layer.

Do not invent owner, administrator, or moderator
roles.

## 7. Membership Actions

Available actions depend on the actual membership
state.

Possible states include:

- Join
- Request Sent
- Member
- Leave

The UI delegates membership changes to the
existing BGM community layer.

## 8. Empty State

If the community has no discussion messages:

Title:
No discussion yet

Supporting message:
Start the first discussion in this community.

Keep the empty state lightweight.

## 9. Loading State

Community content should load progressively.

Do not load the entire World hierarchy or unrelated
communities when opening this screen.

## 10. Error State

If community content cannot be loaded:

Title:
Unable to load community

Supporting message:
Please try again.

Action:
Retry

## 11. Core Integration Boundary

The UI consumes:

- community identity
- membership state
- member data
- discussion data
- membership actions

from the existing BGM community layer.

The UI does not duplicate:

- join approval rules
- invitation rules
- removal rules
- membership validation
- discussion validation

## 12. Low-RAM Rules

Avoid:

- automatic loading of large banners
- video previews
- animated backgrounds
- heavy shadows
- complex community cards
- loading unrelated community data

Use text-first presentation.

## 13. Accessibility

Use:

- readable 16–18px primary text
- approximately 44x44px touch targets
- clear section labels
- status information that does not depend only
  on color
- support larger system text

## 14. Visual Character

The community screen should feel:

- private
- welcoming
- organized
- premium
- calm

Use BGM_GOLD selectively for active states
and important actions.
