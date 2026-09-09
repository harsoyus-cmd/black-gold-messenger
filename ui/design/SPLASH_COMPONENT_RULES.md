# BGM Splash & Identity Component Rules

Version: 0.1.0

## 1. Splash Component

Responsibilities:
- display BGM identity
- provide a clean startup visual
- transition to the next UI state

The splash component must not:
- generate identity
- perform cryptography
- access message storage
- load chat data
- load radio streams
- initialize every feature module

## 2. Logo Area

The logo area must accept the final BGM logo asset.

The component must not alter the logo design.

Logo variants may later include:
- full color
- monochrome
- small-size variant

Only the approved BGM logo may be used.

## 3. Brand Text

Primary brand:
BLACK GOLD MESSENGER

Short brand:
BGM

Typography follows the BGM Typography System.

## 4. Identity Status Component

Possible states:

AVAILABLE
NOT_AVAILABLE
CREATING
ERROR

The UI displays state information only.

Core logic remains in the BGM engine.

## 5. Primary Actions

Identity screen may provide:

Create Identity
Continue
Retry

Actions must be:
- clearly readable
- easy to tap
- visually consistent
- lightweight

## 6. Loading State

If identity creation requires time:

- show a simple progress/loading indicator
- prevent accidental repeated activation
- avoid heavy animation

## 7. Error State

Errors must be human-readable.

Technical implementation details must remain hidden
from normal users.

## 8. Component Independence

Splash and Identity components must remain independent
from Home, Chat, World, Radio, and Profile components.

This allows later UI modules to be added without
rewriting the startup layer.

## 9. Low-RAM Requirement

Components must avoid unnecessary persistent
background work after startup.

Resources used only by Splash should be released
after the transition completes.
