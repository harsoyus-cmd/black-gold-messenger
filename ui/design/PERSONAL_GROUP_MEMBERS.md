# BGM Personal Group Members

Version: 0.1.0

## 1. Purpose

Define the member information interface for a
BGM personal group.

## 2. Member Access

The member interface is opened from the group
conversation header.

It should remain a lightweight secondary screen
or panel.

## 3. Member List

Each member item may display:

- identity name or identity identifier
- membership presence when available

The list must remain easy to scan.

## 4. Identity Priority

The member identity is the primary information.

Avoid unnecessary profile decoration.

## 5. Group Header Detail

The group header may provide:

- group name
- member count

A compact member summary may be shown when
useful.

## 6. Membership Rules

The UI reflects the rules provided by the
existing BGM group layer.

The UI must not create its own membership rules.

The existing group layer remains responsible for:

- adding members
- removing members
- checking membership
- returning member data

## 7. Actions

Initial MVP:

- view members

Future actions such as adding or removing
members remain dependent on the existing
group capabilities and roadmap.

## 8. Navigation

Back returns to the group conversation.

The member interface must not reset or recreate
the conversation.

## 9. Low-RAM Rules

Avoid:

- loading unnecessary profile media
- animated avatars
- large profile cards
- complex member effects
- preloading unrelated member data

Use a simple scrolling list.

## 10. Accessibility

Use:

- readable member identity text
- approximately 44x44px interactive areas
- support for larger system text

## 11. Visual Character

The member interface should remain:

- simple
- private
- organized
- premium
- consistent with BGM

It must not resemble an administration dashboard.
