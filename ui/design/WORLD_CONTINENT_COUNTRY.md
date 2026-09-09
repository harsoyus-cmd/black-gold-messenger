# BGM World Continent & Country

Version: 0.1.0

## 1. Purpose

Define the continent and country browsing
interfaces inside BGM World.

## 2. Continent View

The continent view displays available continents.

Each item may show:

- continent name
- country count when available

The list must remain compact.

## 3. Country View

Selecting a continent opens its countries.

Each country item may show:

- country name
- community count when available

Only the selected continent's country data
should be loaded initially.

## 4. Navigation Hierarchy

Navigation follows:

World
    ↓
Continent
    ↓
Country
    ↓
Community

The current hierarchy level should remain clear
from the app bar title or navigation context.

## 5. Back Navigation

From Country:

Back → Continent

From Continent:

Back → World/Home according to the originating
navigation path.

Do not reset the user's World position
unnecessarily.

## 6. Empty State

If a continent has no countries:

Title:
No countries yet

Supporting message:
There are no available countries here yet.

If a country has no communities:

Title:
No communities yet

Supporting message:
There are no available communities here yet.

## 7. Loading

Load data progressively.

Do not preload:

- every continent
- every country
- every community

Only data required by the current screen
should be requested.

## 8. Error State

If the current list cannot be loaded:

Title:
Unable to load

Supporting message:
Please try again.

Action:
Retry

## 9. Core Integration Boundary

The UI consumes data from the existing BGM World
layer.

The UI does not create or modify World entities.

## 10. Search

Search is deferred from the initial MVP.

When introduced later, it should search only
the currently relevant World scope unless
the roadmap explicitly expands it.

## 11. Low-RAM Rules

Avoid:

- maps
- country flag image loading for every item
- animated geographic graphics
- large cached datasets
- unnecessary background requests

Text-first lists are preferred.

## 12. Accessibility

Use:

- readable list text
- clear hierarchy
- approximately 44x44px touch targets
- support larger system text

## 13. Visual Character

The World browsing experience should remain:

- clean
- global
- premium
- calm
- fast

Use BGM_GOLD selectively for active or important
states rather than every list item.
