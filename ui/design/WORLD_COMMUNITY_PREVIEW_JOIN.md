# BGM Community Preview & Join Entry

Version: 0.1.0

## 1. Purpose

Define the lightweight community preview shown
before entering or requesting membership.

## 2. Community Preview

The preview may display:

- community name
- description
- country context
- member count when available
- community rules summary when available

The community name has highest visual priority.

## 3. Primary Action

The available action depends on the actual
community membership state.

Possible states:

- Join
- Request Sent
- Member

The UI must reflect the existing BGM community
layer.

## 4. Join

When the community allows a join request:

Action:
Join

The UI sends the request through the existing
community logic.

The UI does not directly modify membership data.

## 5. Request Sent

When a request is already pending:

Display:
Request Sent

The action should not create duplicate requests.

## 6. Member

When the current identity is already a member:

Display:
Member

The primary action may open the community.

## 7. Invitation

If an invitation exists, the UI may expose:

- invitation context
- accept action
- decline action

Invitation processing remains controlled by
the existing BGM community layer.

## 8. Rules

Community rules may be displayed before joining.

Keep the presentation concise.

Long rules should use a scrollable text area
rather than expanding the entire screen.

## 9. Loading

While membership state is being resolved:

- use lightweight progress indication
- avoid blocking unrelated navigation

## 10. Error

If the join or invitation operation fails:

Title:
Unable to complete action

Supporting message:
Please try again.

The UI must not display success unless the
core operation succeeds.

## 11. Core Integration Boundary

The UI delegates:

- join requests
- invitation handling
- membership checks
- membership changes

to the existing BGM community layer.

No duplicate community rules are implemented
in the UI.

## 12. Low-RAM Rules

Avoid:

- large community banners loaded automatically
- video previews
- heavy animations
- complex card effects
- unnecessary background requests

## 13. Accessibility

Use:

- readable 16–18px primary text
- approximately 44x44px actions
- clear action labels
- status information not dependent only on color
- support larger system text

## 14. Visual Character

The preview should feel:

- trustworthy
- welcoming
- premium
- calm
- lightweight

Gold should emphasize the primary action,
not cover the entire interface.
