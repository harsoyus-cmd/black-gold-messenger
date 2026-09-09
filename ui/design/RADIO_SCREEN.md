# BGM World Radio

Version: 0.1.0

## 1. Purpose

Define the main World Radio interface for
discovering and opening BGM radio stations.

## 2. Navigation Context

The user reaches radio through:

Radio
    ↓
Continent
    ↓
Country
    ↓
Station
    ↓
Player

The selected location remains visible through
the screen title or navigation context.

## 3. Radio Entry

The Radio section provides access to:

- continent selection
- country selection
- station directory

Do not automatically start a radio stream when
opening the Radio section.

## 4. Continent View

Display available continents supplied by the
radio/world data layer.

The list should remain text-first and lightweight.

Selecting a continent opens its available
countries.

## 5. Country View

Display countries with available radio stations.

Selecting a country opens its station directory.

Only the selected location should be loaded when
possible.

## 6. Station Directory

Each station item may display:

- station name
- short description when available
- country context when useful

The station name has highest visual priority.

## 7. Station Selection

Selecting a station opens the radio player.

The UI passes the station information to the
existing BGM radio player.

The UI does not implement stream transport.

## 8. Player Entry

The player may display:

- station name
- playback state
- Play
- Pause
- Stop

Playback state must reflect the existing
BGMRadioPlayer state.

## 9. Core Integration Boundary

The UI consumes:

BGMRadioDirectory
BGMRadioStation
BGMRadioPlayer

The UI does not duplicate:

- station directory storage
- stream transport
- playback engine
- stream URL processing

## 10. Loading State

Use lightweight progress indication.

Do not preload stations from unrelated
continents or countries.

## 11. Empty State

If no stations are available:

Title:
No radio stations yet

Supporting message:
There are no radio stations available here.

Keep the state simple.

## 12. Error State

If radio data cannot be loaded:

Title:
Unable to load radio

Supporting message:
Please try again.

Action:
Retry

## 13. Low-RAM Rules

Avoid:

- loading all stations globally
- automatic stream playback
- large station artwork preloading
- video previews
- animated visualizers
- heavy shadows
- complex animated player effects

Radio playback should not require a heavy
visual interface.

## 14. Accessibility

Use:

- readable station names
- readable location labels
- approximately 44x44px playback controls
- clear playback state
- support larger system text
- state information that does not depend only
  on color

## 15. Visual Character

World Radio should feel:

- global
- calm
- premium
- focused
- lightweight

Use BGM_GOLD selectively for active station
and playback states.

Do not use excessive glow or game-like
visualizers.
