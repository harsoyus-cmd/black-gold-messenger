# BGM Community States & Responsive Behavior

Version: 0.1.0

## 1. Purpose

Define the main states and responsive behavior
for the BGM community interface.

## 2. Normal State

Display:

- community header
- discussion entry or discussion content
- member entry
- applicable membership action

Only currently required community data should
be loaded.

## 3. Empty Discussion State

When no discussion messages exist:

Title:
No discussion yet

Supporting message:
Start the first discussion in this community.

Eligible members may use the composer.

## 4. Empty Member State

When no member data is available:

Title:
No members to display

Keep the state simple and readable.

## 5. Loading State

Use a lightweight progress indicator.

Avoid:

- animated skeleton-heavy layouts
- large placeholder graphics
- background loading of unrelated data

## 6. Offline State

If network connectivity is unavailable:

- preserve locally available community data
- clearly indicate unavailable actions
- do not falsely report successful membership
  or discussion operations

When connectivity returns, the UI may retry
operations through the existing core flow.

## 7. Operation Failure

If a community action fails:

- keep the current valid state
- show a concise error message
- provide Retry when appropriate

Never display a successful result before the
underlying operation succeeds.

## 8. Membership Transition

Membership state may transition between:

Not Member
    ↓
Request Sent
    ↓
Member

Or:

Member
    ↓
Not Member

The UI reflects the state returned by the
community layer.

It must not simulate a transition locally.

## 9. Navigation

Back navigation returns to the previous community
or World level.

Expected hierarchy:

World
    ↓
Continent
    ↓
Country
    ↓
Community
    ↓
Community Detail / Discussion / Members

Do not create unnecessary navigation layers.

## 10. Text Scaling

Support:

- Normal text
- Large text
- Extra Large text

Important information must remain readable
without relying on fixed tiny layouts.

## 11. Touch Targets

Interactive controls should provide approximately
44x44px touch areas.

Do not depend on tiny icons alone.

## 12. Orientation

Initial MVP:

- portrait-first
- landscape should remain functional when
  supported by the platform

Do not add complex orientation-specific layouts.

## 13. Low-RAM Behavior

When memory is constrained:

- load visible content first
- avoid unnecessary image resources
- avoid media preloading
- avoid continuous animation
- avoid large in-memory community histories

The UI should remain functional without
requiring heavy resources.

## 14. Visual Consistency

Maintain the BGM design system:

- black dominant background
- gold for selective emphasis
- readable light text
- restrained surfaces and borders
- minimal glow
- no game-like neon effects

## 15. Core Boundary

All authoritative community state remains owned
by the BGM community layer.

The UI is a presentation and interaction layer.

It must not duplicate community business rules.
