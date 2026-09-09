# BGM Radio Station Discovery

Version: 0.1.0

## 1. Purpose

Define the lightweight station discovery
interface inside World Radio.

## 2. Navigation

The discovery hierarchy is:

Radio
    ↓
Continent
    ↓
Country
    ↓
Station

The selected continent and country remain visible
through the navigation context.

## 3. Station Item

Each station item may display:

- station name
- short description when available
- country context when useful

Station name is the primary visual element.

## 4. Station Selection

Selecting a station opens the player.

The UI passes the actual station information
to the existing BGM radio player.

The UI must not invent or modify stream URLs.

## 5. Playback Indicator

If a station is currently playing, the UI may
display a lightweight active indicator.

The indicator must reflect the actual player
state.

Do not animate continuously.

## 6. No Automatic Playback

Opening:

- Radio
- Continent
- Country
- Station Directory

must not automatically start playback.

Playback begins only after an explicit user
action.

## 7. Empty State

If the selected country has no stations:

Title:
No radio stations yet

Supporting message:
There are no radio stations available in this country.

Keep the empty state simple.

## 8. Loading State

Load stations progressively.

Only stations relevant to the selected country
should be requested.

Avoid loading the global station directory
unnecessarily.

## 9. Error State

If station discovery fails:

Title:
Unable to load radio stations

Supporting message:
Please try again.

Action:
Retry

## 10. Core Boundary

The UI consumes:

BGMRadioDirectory
BGMRadioStation

The UI does not duplicate:

- station storage
- station filtering logic
- stream URL generation
- playback implementation

## 11. Search

Station search is deferred from the initial MVP.

When introduced later, it should operate only
within the relevant station scope and remain
lightweight.

## 12. Low-RAM Rules

Avoid:

- large station artwork
- video previews
- animated equalizers
- heavy card effects
- preloading stations from other locations
- unnecessary background requests

Use a simple scrolling list.

## 13. Accessibility

Use:

- readable station names
- clear location context
- approximately 44x44px touch areas
- playback state not dependent only on color
- support larger system text

## 14. Visual Character

Station discovery should feel:

- global
- clean
- premium
- calm
- efficient

Use BGM_GOLD selectively for the selected
station and active playback state.
