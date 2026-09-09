# BGM Recent Chat List

Version: 0.1.0

## 1. Purpose

Display recent personal and group conversations
on the BGM Home / Chat destination.

## 2. Conversation Item

Each conversation item may display:

- contact or group name
- latest message preview
- timestamp
- unread indicator

The item must remain compact and easy to scan.

## 3. Personal Conversation

Personal conversation item:

Identity
    ↓
Latest message
    ↓
Timestamp / unread state

The identity name must have visual priority
over secondary information.

## 4. Personal Group

Group conversation item:

Group name
    ↓
Latest message
    ↓
Timestamp / unread state

A group indicator may be used when needed.

## 5. Unread State

Unread conversations should be clearly distinguishable.

Recommended indicators:

- gold unread dot
- stronger text weight
- subtle BGM_GOLD accent

Do not use excessive glow.

## 6. Empty State

When no conversations exist:

Title:
No conversations yet

Supporting message:
Start a conversation to see it here.

Keep the empty state simple.

## 7. Long Text

Long message previews must be truncated.

The list must never expand indefinitely because
of a long message.

## 8. Interaction

Selecting a conversation opens its corresponding
chat screen.

The Home list must not contain full message history.

## 9. Performance

Use a lightweight scrolling list.

Only visible or required conversation data
should be rendered.

Do not preload media previews unnecessarily.

## 10. Low-RAM Rules

Avoid:

- automatic image loading for every conversation
- video previews
- animated avatars
- heavy shadows
- complex card effects
- unnecessary background processing

## 11. Future Extension

Conversation items may later support:

- pinned conversations
- muted conversations
- archive
- media indicators
- delivery status

These are deferred and should not complicate
the initial UI.
