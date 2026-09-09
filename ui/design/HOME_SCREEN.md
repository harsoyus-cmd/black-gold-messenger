# BGM Home Screen

Version: 0.1.0

## 1. Purpose

Home is the primary navigation screen after BGM startup.

It provides fast access to the main BGM services:

- Chat
- World
- Radio
- Profile

## 2. Visual Foundation

Background:
BGM_BLACK

Surfaces:
BGM_SURFACE
BGM_SURFACE_2

Accent:
BGM_GOLD

Typography:
Atkinson Hyperlegible

## 3. Main Navigation

Primary navigation:

CHAT
WORLD
RADIO
PROFILE

The currently selected section uses the BGM gold accent.

Inactive sections use neutral text/icons.

## 4. Home Layout

Recommended structure:

Top Area
    BGM identity / user context

Main Content
    Recent conversations and relevant activity

Bottom Navigation
    Chat | World | Radio | Profile

The layout must remain simple and uncluttered.

## 5. Chat Entry

The Chat section provides access to:

- Personal conversations
- Personal groups

Recent conversations may show:

- contact/group name
- latest message preview
- timestamp
- unread indicator

## 6. World Entry

World provides navigation:

Continent
    ↓
Country
    ↓
Community

World content should not be loaded entirely at startup.

## 7. Radio Entry

Radio provides navigation:

Continent
    ↓
Country
    ↓
Station
    ↓
Player

Radio streams must not start automatically when Home opens.

## 8. Profile Entry

Profile provides access to:

- BGM identity
- application preferences
- notification preferences
- display preferences

Advanced settings may be added later.

## 9. Empty State

When there is no recent conversation:

Show a simple readable empty state.

Do not fill the screen with decorative graphics.

## 10. Loading State

Use lightweight loading indicators.

Do not use:
- video
- particle effects
- animated backgrounds
- heavy skeleton systems

## 11. Performance

Home must initialize only the information required
to display the current screen.

Do not load:
- all communities
- all radio stations
- all media
- complete message history

until requested.

## 12. Navigation Rule

Navigation must be predictable and consistent.

Back navigation must return to the previous logical screen.

## 13. Design Character

Home should feel:

- premium
- calm
- organized
- fast
- familiar

It must not feel:

- crowded
- corporate
- gaming-oriented
- overly decorative
