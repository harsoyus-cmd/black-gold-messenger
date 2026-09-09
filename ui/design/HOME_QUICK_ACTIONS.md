# BGM Home Quick Actions

Version: 0.1.0

## 1. Purpose

Provide fast access to frequently used BGM actions
without overcrowding the Home screen.

## 2. Primary Actions

Initial quick actions:

- New Chat
- New Group

These actions should be immediately understandable.

## 3. New Chat

Action:
New Chat

Purpose:
Start a personal conversation.

The UI delegates message and identity operations
to the existing BGM core.

## 4. New Group

Action:
New Group

Purpose:
Start a personal group conversation.

Group creation and membership logic remain
responsibilities of the existing BGM group layer.

## 5. Visual Treatment

Quick actions should use:

- simple icon
- readable label
- BGM_GOLD for primary emphasis
- BGM_SURFACE for contained surfaces

Avoid:
- large decorative buttons
- excessive gold
- animated effects
- oversized icons

## 6. Placement

Quick actions may appear near the top of the
Chat/Home content area.

They must not push recent conversations
unnecessarily far down the screen.

## 7. Interaction

Tap action:
Open the corresponding creation flow.

After completion:
Return to the appropriate conversation destination.

## 8. Low-RAM Rules

Quick actions must not initialize:

- complete contact lists
- complete group lists
- media systems
- radio systems
- world systems

until the user requests them.

## 9. Future Extension

Possible future actions:

- New Community
- Open Mail
- Open Radio

These remain deferred.

Do not add them to the initial Home UI
until required by the roadmap.
