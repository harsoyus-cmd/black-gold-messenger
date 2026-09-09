# BGM Radio Player

Version: 0.1.0

## 1. Purpose

Define the lightweight radio playback interface
for BGM World Radio.

## 2. Player Context

The player is opened after the user explicitly
selects a radio station.

The selected station remains visible.

## 3. Station Information

Display:

- station name
- location context when available
- playback state

The station information comes from the existing
BGMRadioStation data.

## 4. Playback States

The UI reflects the existing BGMRadioPlayer
states:

- STOPPED
- PLAYING
- PAUSED

Do not create additional playback states in the
UI.

## 5. STOPPED

Display:

Play

Playback has not started.

## 6. PLAYING

Display:

Pause
Stop

The UI must reflect the actual player state.

## 7. PAUSED

Display:

Play
Stop

The UI must not report PLAYING while the player
is paused.

## 8. Explicit Playback

Playback starts only after the user selects:

Play

Opening the Radio section or station directory
must never start playback automatically.

## 9. Stop

Selecting:

Stop

ends the current playback session and returns
the player to STOPPED.

The UI reflects the state supplied by the
BGMRadioPlayer.

## 10. Station Switching

Selecting another station must not silently
assume successful playback.

The UI should:

1. stop or transition from the current station
   according to the player implementation
2. request playback of the selected station
3. display the resulting player state

The UI does not implement stream handling itself.

## 11. Stream Errors

If playback cannot start:

Title:
Unable to play station

Supporting message:
Please try again.

The UI must not display PLAYING unless the
underlying player reports PLAYING.

## 12. Core Integration Boundary

The UI uses:

BGMRadioStation
BGMRadioPlayer

The UI does not implement:

- stream transport
- buffering engine
- audio decoding
- stream URL generation
- radio server functionality

## 13. Background Behavior

Radio playback may continue according to the
platform audio lifecycle and future integration.

The MVP UI must not introduce unnecessary
background services.

## 14. Low-RAM Rules

Avoid:

- animated audio visualizers
- waveform rendering
- video backgrounds
- album-art-heavy layouts
- continuous GPU effects
- unnecessary polling

Use simple controls and text.

## 15. Accessibility

Use:

- clearly labeled Play, Pause, and Stop actions
- approximately 44x44px touch targets
- readable station name
- readable playback state
- support larger system text
- state information not dependent only on color

## 16. Visual Character

The player should feel:

- premium
- calm
- focused
- modern
- lightweight

Use BGM_GOLD for the active playback state
and primary playback action.

Avoid excessive glow and decorative effects.
