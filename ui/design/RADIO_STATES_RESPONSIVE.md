# BGM Radio States & Responsive Behavior

Version: 0.1.0

## 1. Purpose

Define radio interface states and responsive
behavior for the BGM MVP.

## 2. Normal State

Display:

- current location context
- station list or selected station
- current playback state when applicable

Only the required radio data should be loaded.

## 3. Loading State

Use lightweight progress indication.

Do not block unrelated BGM navigation while
radio data is loading.

Avoid heavy animated placeholders.

## 4. Empty State

If no stations are available:

Title:
No radio stations yet

Supporting message:
There are no radio stations available here.

## 5. Playback States

The interface reflects only the existing:

- STOPPED
- PLAYING
- PAUSED

The UI must not create a second playback state
system.

## 6. Playback Failure

If playback fails:

Title:
Unable to play station

Supporting message:
Please try again.

Action:
Retry

The UI must not display PLAYING unless the
underlying player reports that state.

## 7. Offline State

If network access is unavailable:

- preserve station information already available
- show that playback may be unavailable
- do not falsely report successful playback

When connectivity returns, the user may retry.

## 8. Navigation

Expected hierarchy:

Radio
    ↓
Continent
    ↓
Country
    ↓
Station
    ↓
Player

Back navigation returns to the previous radio
level.

Do not create unnecessary navigation layers.

## 9. Text Scaling

Support:

- Normal
- Large
- Extra Large

Station names and playback controls must remain
usable at larger text sizes.

## 10. Touch Targets

Interactive controls should provide approximately
44x44px touch areas.

Playback controls must have clear labels.

## 11. Orientation

Initial MVP:

- portrait-first
- landscape should remain functional when
  supported by the platform

Do not create complex orientation-specific
layouts.

## 12. Low-RAM Behavior

When memory is constrained:

- load visible station data first
- avoid station artwork preloading
- avoid video
- avoid animated visualizers
- avoid continuous polling
- avoid large in-memory station caches

Radio playback should use the smallest practical
UI resources.

## 13. Background Playback

Do not add a heavy background architecture in
the MVP UI.

Future platform-specific background playback
integration may be added separately.

## 14. Visual Consistency

Maintain the BGM design system:

- black dominant background
- gold selective emphasis
- readable light text
- restrained surfaces
- minimal glow
- no game-like neon visualizers

## 15. Core Boundary

The BGM radio layer remains authoritative for:

- station data
- station selection
- playback state
- playback operations

The UI is only the presentation and interaction
layer.
