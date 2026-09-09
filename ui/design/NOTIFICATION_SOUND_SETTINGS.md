# BGM Notification & Sound Settings

Version: 0.1.0

## 1. Purpose

Define the notification and sound settings
interface for BGM.

## 2. Notification Categories

The settings may provide independent controls
for:

- personal messages
- personal groups
- communities
- secure mail
- calls when supported

Each setting must reflect the actual notification
capability available in the application.

## 3. Notification Enable State

Each category may provide:

- Enabled
- Disabled

The UI must reflect the actual saved preference.

Do not report a setting as enabled if the
underlying preference was not saved successfully.

## 4. Notification Sound

Provide:

Notification Sound

The MVP sound identity is:

BGM Crystal

The sound should remain short and lightweight.

## 5. Sound Enable State

Provide:

- Sound On
- Sound Off

When sound is disabled, notification delivery
may continue if notifications are otherwise
enabled.

## 6. Sound Preview

A lightweight preview action may be provided.

The preview:

- is explicitly user-triggered
- plays only the selected notification sound
- does not start background playback

Avoid automatic sound playback when opening
Settings.

## 7. Volume

A notification volume control may be exposed
only when supported by the platform/application.

Do not implement a second independent audio
engine.

## 8. Distinct Notification Sounds

Future versions may provide distinct BGM Crystal
variations for:

- personal message
- mail
- group
- community
- call
- warning

The MVP should avoid loading all sound variants
unnecessarily.

## 9. Core Boundary

Notification and sound settings remain
application-level preferences.

The UI does not implement:

- notification delivery
- audio playback engine
- operating-system notification transport
- background audio services

## 10. Error State

If a preference cannot be saved:

Title:
Unable to save setting

Supporting message:
Please try again.

The UI must restore the last confirmed state.

## 11. Low-RAM Rules

Avoid:

- loading multiple sound files simultaneously
- long notification audio
- waveform visualizations
- animated sound controls
- background audio processing

Use short compressed audio resources.

## 12. Accessibility

Use:

- clear setting names
- readable state labels
- approximately 44x44px interactive controls
- support larger system text
- do not communicate state through color alone

## 13. Visual Character

Notification settings should feel:

- simple
- precise
- calm
- premium

Use BGM_GOLD selectively for active states.

Avoid excessive glow, gradients, and decorative
controls.
