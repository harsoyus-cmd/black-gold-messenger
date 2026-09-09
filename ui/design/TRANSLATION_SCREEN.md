# BGM Translation Interface

Version: 0.1.0

## 1. Purpose

Define the lightweight translation interface
for BGM.

## 2. Translation Context

Translation is a display/service feature.

The UI sends text and language selection to the
existing BGM translation service.

The UI does not implement translation algorithms.

## 3. Main Layout

The screen contains:

- source language selector
- target language selector
- source text area
- translate action
- translated result area

The layout should remain simple and readable.

## 4. Source Language

Allow the user to select the source language.

When automatic language detection is supported
later, it may be added without changing the
basic interface.

## 5. Target Language

Allow the user to select the target language.

The selected target language must be clearly
visible before translation.

## 6. Source Text

The source text area should support:

- multiline text
- readable 16–18px text
- clear input state
- larger system text

Avoid unnecessary formatting controls.

## 7. Translate Action

Primary action:

Translate

The action is enabled only when translation
input is valid.

The UI delegates translation to the existing
BGM translation service.

## 8. Result

The translated result should display:

- original text when useful for comparison
- translated text
- source language
- target language

The original text must not be silently replaced.

## 9. Translation Service Boundary

The UI uses the existing:

BGMTranslationService

and:

BGMTranslationResult

The UI does not duplicate:

- translation algorithms
- translation model loading
- language processing
- network transport
- encryption

## 10. Unsupported Translation

The current translation service may report that
a translation implementation is unavailable.

The UI should show a clear state:

Translation unavailable

Supporting message:
This translation service is not available yet.

Do not present an unavailable translation as
successful.

## 11. Loading State

During translation:

- show lightweight progress
- prevent duplicate translation requests
  when appropriate
- keep existing input visible

Avoid heavy animation.

## 12. Error State

If translation fails:

Title:
Unable to translate

Supporting message:
Please try again.

Action:
Retry

The original input remains available.

## 13. Low-RAM Rules

Avoid:

- loading large local translation models
- keeping unnecessary translation history
- animated translation effects
- background translation processing
- large cached language resources

Heavy local translation technology is deferred
for future optimization.

## 14. Accessibility

Use:

- readable 16–18px primary text
- clear language labels
- approximately 44x44px controls
- support larger system text
- status information that does not depend only
  on color

## 15. Visual Character

Translation should feel:

- useful
- calm
- clear
- trustworthy
- premium

Use BGM_GOLD selectively for the primary
translation action and active language state.
