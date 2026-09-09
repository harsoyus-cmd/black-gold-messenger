# BGM Translation States & Language Selection

Version: 0.1.0

## 1. Purpose

Define language selection and translation states
for the BGM translation interface.

## 2. Language Selector

Language selectors should clearly identify:

- Source language
- Target language

Use readable language names.

Avoid flags as the primary language identifier
because one language may be used across multiple
countries.

## 3. Language Swap

When both languages are selected, the UI may
provide:

Swap Languages

The action exchanges source and target language.

Do not perform an automatic translation during
the swap.

## 4. Default State

Initial state:

- no unnecessary language data loaded
- source language selectable
- target language selectable
- source text ready for input

The UI should remain lightweight.

## 5. Empty Input State

When source text is empty:

- Translate action is unavailable
- no translation request is sent

Keep the screen clean and explanatory.

## 6. Loading State

While translation is running:

- preserve source text
- preserve selected languages
- show lightweight progress
- prevent duplicate requests when appropriate

## 7. Success State

A successful result displays:

- original text
- translated text
- source language
- target language

The original text remains available.

## 8. Unsupported State

When the selected translation service is not
implemented:

Title:
Translation unavailable

Supporting message:
This translation service is not available yet.

No fake or placeholder translation is shown as
a successful result.

## 9. Error State

If translation fails:

Title:
Unable to translate

Supporting message:
Please try again.

Action:
Retry

The user's source text remains intact.

## 10. Same Language

If source and target languages are identical,
the UI should avoid unnecessary translation work.

It may explain that both languages are the same
or simply keep the Translate action inactive.

## 11. Chat Integration

When launched from a chat message:

- preserve the original message
- preserve the conversation position
- display the translation as a temporary
  presentation result
- do not alter the stored message

## 12. Core Boundary

The UI delegates translation to the existing
BGM translation service.

The authoritative result remains:

BGMTranslationResult

The UI does not implement language detection,
translation algorithms, or model execution.

## 13. Low-RAM Rules

Avoid:

- loading all language resources at startup
- large language model memory usage
- automatic translation of conversations
- large translation history
- background translation jobs

Load only what the current operation requires.

## 14. Accessibility

Use:

- clear language names
- readable controls
- approximately 44x44px touch targets
- support larger system text
- clear state labels independent of color

## 15. Visual Character

Language selection should feel:

- simple
- precise
- calm
- premium

BGM_GOLD is reserved for selected states,
primary actions, and important indicators.
