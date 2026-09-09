# BGM Community Members & Membership Actions

Version: 0.1.0

## 1. Purpose

Define the member list and membership actions
inside a BGM community.

## 2. Member List

Each member item may display:

- identity
- membership status when relevant

The identity is the primary information.

## 3. Member Count

The community may display the current member
count when supplied by the BGM community layer.

The UI must use the actual count.

## 4. Membership States

The UI may represent:

- Member
- Request Sent
- Not Member
- Invited

The displayed state must come from the existing
community layer.

## 5. Join Request

A non-member may select:

Join

when the community permits a join request.

The request is processed by the existing BGM
community logic.

The UI must not approve the request itself.

## 6. Join Approval

The UI reflects the result supplied by the
community layer.

It does not implement approval rules.

The existing community model determines whether
a request becomes membership.

## 7. Invitation

An existing member may have access to an
invitation action when supported by the core.

Invitation handling remains delegated to the
existing community layer.

## 8. Leave Community

A member may select:

Leave Community

The action requires explicit user confirmation.

After a successful leave operation, the UI
refreshes the membership state.

## 9. Removal

The UI must not invent administrator controls.

Community removal follows the existing core rule:

10 unique member removal requests result in
automatic removal.

The UI only displays the resulting state.

## 10. Roles

The MVP has no:

- owner
- administrator
- moderator

Do not display role badges or role-management
controls.

## 11. Loading State

Member data should load progressively.

Only the selected community's members should
be requested.

## 12. Error State

If member data cannot be loaded:

Title:
Unable to load members

Supporting message:
Please try again.

Action:
Retry

## 13. Core Integration Boundary

The UI consumes membership information from the
existing BGM community layer.

The UI does not duplicate:

- approval logic
- invitation rules
- removal rules
- membership validation
- member storage

## 14. Low-RAM Rules

Avoid:

- loading unrelated communities
- large avatar image preloading
- video previews
- complex member cards
- heavy shadows
- continuous animations

Text-first member presentation is preferred.

## 15. Accessibility

Use:

- readable identity text
- clear action labels
- approximately 44x44px touch targets
- status information that does not depend only
  on color
- support larger system text

## 16. Visual Character

The member interface should feel:

- trustworthy
- private
- organized
- calm
- premium

Use BGM_GOLD selectively for active states
and important actions.
