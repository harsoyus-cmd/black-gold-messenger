# BGM Profile & Settings

Version: 0.1.0

## 1. Purpose

Define the lightweight Profile and Settings
interface for BGM.

## 2. Profile Entry

Profile is accessible from the primary BGM
navigation.

The profile interface may display:

- BGM identity
- identity status
- basic account/device context
- settings entry points

The UI uses the existing BGM identity layer.

## 3. Identity

Display the current BGM identity when available.

The UI must not generate or modify cryptographic
identity data directly.

Identity creation and identity storage remain
owned by the existing core.

## 4. Profile Information

The MVP may display:

- identity ID
- public identity information when appropriate
- current identity availability

Sensitive private key material must never be
displayed.

## 5. Settings Categories

Initial settings may include:

- Appearance
- Text Size
- Notifications
- Sound
- About BGM

Keep settings grouped into simple readable
sections.

## 6. Appearance

Appearance settings may provide:

- BGM dark appearance as the primary MVP design
- future theme expansion

The MVP should not introduce complex themes.

## 7. Text Size

Provide:

- Normal
- Large
- Extra Large

Text size changes should apply consistently
across supported BGM UI screens.

## 8. Notifications

Notification settings may control:

- message notifications
- group notifications
- community notifications
- mail notifications
- radio-related notifications when applicable

Only settings supported by the actual
notification implementation should be exposed.

## 9. Sound

Sound settings may provide:

- notification sound enabled/disabled
- notification volume where supported

The BGM notification sound family may use the
BGM Crystal identity defined by the design system.

Do not load unnecessary audio resources.

## 10. About BGM

The About section may display:

- Black Gold Messenger
- application version
- protocol/application version when appropriate

Keep the presentation lightweight.

## 11. Deferred Settings

Do not implement unfinished settings such as:

- advanced account recovery
- complex device management
- cloud synchronization
- heavy backup systems
- advanced privacy dashboards

These may be added in later versions.

## 12. Core Boundary

The UI consumes existing BGM identity and
application services.

The UI does not duplicate:

- cryptography
- identity generation
- key storage
- message storage
- network implementation

## 13. Loading State

Use lightweight loading only when profile or
settings data requires it.

Avoid loading unrelated BGM data.

## 14. Error State

If profile data cannot be loaded:

Title:
Unable to load profile

Supporting message:
Please try again.

Action:
Retry

## 15. Low-RAM Rules

Avoid:

- animated profile backgrounds
- large profile images
- video backgrounds
- heavy settings graphics
- unnecessary background processing
- large cached preference data

Prefer simple text-based settings rows.

## 16. Accessibility

Use:

- readable 16–18px primary text
- clear section labels
- approximately 44x44px touch targets
- support larger system text
- settings states that do not depend only on color

## 17. Visual Character

Profile and Settings should feel:

- private
- trustworthy
- premium
- calm
- simple

Use BGM_GOLD selectively for active settings,
important identity information, and primary
actions.

Avoid excessive gold, glow, gradients, and
decorative elements.
