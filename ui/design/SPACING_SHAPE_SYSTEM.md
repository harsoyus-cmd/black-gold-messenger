# BGM Spacing & Shape System

Version: 0.1.0

## 1. Spacing Scale

| Token | Size | Usage |
|---|---:|---|
| BGM_SPACE_1 | 4 px | Very small gaps |
| BGM_SPACE_2 | 8 px | Icon/text gaps |
| BGM_SPACE_3 | 12 px | Compact element spacing |
| BGM_SPACE_4 | 16 px | Standard spacing |
| BGM_SPACE_5 | 20 px | Section spacing |
| BGM_SPACE_6 | 24 px | Large section spacing |
| BGM_SPACE_7 | 32 px | Major screen separation |

## 2. Screen Padding

Default horizontal screen padding:
16 px

Large screens may increase padding when appropriate.

The UI must not waste screen space unnecessarily.

## 3. Touch Targets

Interactive elements should provide a comfortable touch area.

Minimum target:
44 × 44 px

Important actions may use larger targets.

## 4. Corner Radius

| Token | Radius | Usage |
|---|---:|---|
| BGM_RADIUS_SM | 6 px | Small controls |
| BGM_RADIUS_MD | 10 px | Inputs and standard cards |
| BGM_RADIUS_LG | 16 px | Message bubbles and prominent panels |
| BGM_RADIUS_XL | 20 px | Large feature surfaces |

Avoid excessive rounding.

The interface should feel refined rather than playful.

## 5. Borders

Default border:
Subtle dark/neutral border.

Gold borders:
Use only for selected or important elements.

Avoid outlining every element with gold.

## 6. Elevation

Prefer contrast between surfaces instead of heavy shadows.

Recommended hierarchy:

BGM_BLACK
    ↓
BGM_SURFACE
    ↓
BGM_SURFACE_2

Use shadows sparingly.

## 7. Glow

Gold glow is an accent effect.

Use only for:
- active navigation
- selected elements
- important BGM identity elements
- focused primary actions

Glow must remain subtle.

Never use continuous animated glow.

## 8. Lists

Lists should prioritize:
- readable text
- clear spacing
- simple separators
- fast rendering

Avoid heavy cards when a simple list is sufficient.

## 9. Low-RAM Rules

Avoid:
- unnecessary shadows
- large blur effects
- continuous animations
- complex backgrounds
- excessive rounded containers
- nested visual components without purpose

Simple UI elements are preferred.

## 10. Design Character

Spacing and shapes should create:

Order
Clarity
Calm
Premium appearance
Efficient use of screen space

The interface must not feel:

Crowded
Playful
Game-like
Over-decorated
Heavy
Cheap
