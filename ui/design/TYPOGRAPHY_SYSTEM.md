# BGM Typography System

Version: 0.1.0

## 1. Primary Font

Font family:
Atkinson Hyperlegible

Purpose:
- High readability
- Clear character distinction
- Comfortable for long conversations
- Suitable for older users
- Suitable for small mobile screens

## 2. Text Scale

| Token | Size | Usage |
|---|---:|---|
| BGM_TEXT_XS | 12 px | Metadata, timestamps |
| BGM_TEXT_SM | 14 px | Supporting information |
| BGM_TEXT_MD | 16 px | Standard body text |
| BGM_TEXT_CHAT | 17 px | Chat messages |
| BGM_TEXT_LG | 18 px | Large body / important text |
| BGM_TEXT_XL | 22 px | Section headings |
| BGM_TEXT_XXL | 28 px | Main screen headings |

## 3. Accessibility Sizes

Normal:
16–17 px body/chat

Large:
18–20 px body/chat

Extra Large:
21–24 px body/chat

Text scaling must not break:
- message layout
- buttons
- navigation
- lists
- input fields

## 4. Weight

Regular:
Normal body and chat text.

Medium:
Names, navigation labels, important information.

Bold:
Screen titles and critical emphasis only.

Avoid excessive bold text.

## 5. Color Relationship

Primary text:
BGM_TEXT_PRIMARY

Secondary text:
BGM_TEXT_SECONDARY

Muted text:
BGM_TEXT_MUTED

Gold should not be used for ordinary paragraphs.
Gold is reserved for emphasis, active states, and BGM identity.

## 6. Readability Rules

- Prefer clear spacing over decorative effects.
- Do not use extremely small text for essential information.
- Do not place long text over bright gold backgrounds.
- Maintain strong contrast between text and background.
- Chat messages must remain comfortable to read for long sessions.

## 7. Low-RAM Rules

Typography must not require:
- animated text effects
- heavy font effects
- unnecessary font variants
- continuous text animations

The UI should use a small and controlled font set.

## 8. Design Character

Typography should feel:

Clear
Modern
Calm
Premium
Human

It must not feel:

Corporate
Gaming
Decorative
Overly futuristic
Difficult to read
