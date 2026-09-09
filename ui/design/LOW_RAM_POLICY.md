# BGM Low-RAM UI Policy

Version: 0.1.0

## 1. Target

BGM UI must remain usable on older Android
devices with limited RAM.

Minimum design target:

- approximately 1 GB RAM class devices

## 2. Core Principles

Prefer:

- simple layouts
- text-first interfaces
- lazy loading
- small resources
- short-lived UI objects
- explicit user actions
- lightweight screen transitions

Avoid:

- unnecessary background work
- continuous animation
- video backgrounds
- 3D interfaces
- heavy blur
- complex shadows
- visualizers
- large persistent images

## 3. Screen Loading

Opening a screen must load only the resources
required by that screen.

Do not preload:

- conversations not visible
- community lists not required
- radio streams
- media files
- mail content
- translation models

## 4. Media

Media must be loaded only when requested.

Do not keep large media resources in memory
after they are no longer required.

Prefer streaming or bounded buffering where
appropriate.

## 5. Radio

Radio playback is explicit.

Do not:

- auto-play
- preload multiple streams
- maintain unnecessary visualizers
- keep inactive stations playing

## 6. Translation

Translation resources must remain lightweight.

Do not load large local language models in the
MVP.

Translation remains a service boundary.

## 7. Animation

Animations are optional.

If implemented:

- keep them short
- avoid continuous animation
- avoid particle systems
- avoid expensive blur
- avoid complex transitions

Static UI is preferred when performance is
uncertain.

## 8. Images

Use images only when they provide meaningful
interface value.

Prefer:

- small dimensions
- compressed formats
- lazy loading
- release after use

Avoid decorative large images.

## 9. Lists

Long lists should use lazy or virtualized
rendering when supported by the UI framework.

Do not instantiate unnecessary off-screen
items.

## 10. Notifications

Notification sounds should be short.

Do not load multiple sound resources
simultaneously.

Notification playback must not become a
continuous background process.

## 11. Background Processing

Avoid unnecessary:

- polling
- timers
- workers
- background synchronization
- repeated network activity

Background processing must have a concrete
purpose.

## 12. Memory Lifecycle

Screens should release resources when they
leave active use.

Avoid retaining:

- large images
- media buffers
- inactive streams
- obsolete screen objects

## 13. Battery

Low-RAM optimization also protects battery.

Prefer event-driven work over continuous polling.

## 14. Accessibility

Performance optimization must not reduce:

- readable text
- touch target size
- text scaling
- clear state information

## 15. Core Boundary

UI optimization must not duplicate or modify
the existing BGM core architecture.

The UI consumes existing services and models.

## 16. MVP Rule

Do not add heavy technology only to improve
visual appearance.

If a feature requires substantial RAM,
storage, CPU, GPU, or battery resources,
defer it to a later update.

## 17. Verification Rule

Every future UI implementation should be checked
for:

- unnecessary allocations
- large resources
- background work
- continuous animation
- excessive media buffering
- unnecessary preloading

Existing PASS components must not be rebuilt
unless a verified problem requires a change.
