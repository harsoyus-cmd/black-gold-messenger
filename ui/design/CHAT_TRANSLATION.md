# BGM Chat Translation

Version: 0.1.0

## 1. Purpose

Define the translation interaction available
from a BGM conversation.

## 2. Translation Entry

Translation may be accessed from an individual
message when translation is applicable.

The original message remains unchanged.

## 3. Translation Action

The user may select:

Translate

The UI sends the selected message text to the
existing BGM translation service.

## 4. Language Selection

The user may select:

- source language
- target language

Previously selected languages may be reused
when appropriate.

The UI must clearly show the selected target
language.

## 5. Translation Result

The translated text is displayed together with
the original message.

The translation is a presentation result.

It does not replace the original message stored
or transmitted by BGM.

## 6. Result State

A successful result may display:

- original message
- translated message
- target language

Keep the presentation compact so the conversation
remains easy to read.

## 7. Unsupported Service

If translation is not currently available:

Title:
Translation unavailable

Supporting message:
This translation service is not available yet.

The original message remains visible.

## 8. Loading State

During translation:

- keep the original message visible
- show lightweight progress
- prevent unnecessary duplicate requests

Avoid blocking the entire conversation.

## 9. Error State

If translation fails:

- preserve the original message
- show a concise error state
- provide Retry when appropriate

Never replace the original message with an
error or incomplete translation.

## 10. Core Boundary

The UI delegates translation to:

BGMTranslationService

and consumes:

BGMTranslationResult

The UI does not modify:

- message encryption
- message payload
- transport
- message storage
- original message content

## 11. Privacy

Translation must respect the existing BGM
message privacy boundary.

The UI must not silently send message content
to an external translation provider.

Any future external translation provider
requires an explicit service integration and
privacy design.

## 12. Low-RAM Rules

Avoid:

- translating every message automatically
- preloading translations
- maintaining a large translation cache
- heavy local translation models
- continuous background processing

Translation is user-triggered.

## 13. Accessibility

Use:

- readable original and translated text
- clear target-language label
- approximately 44x44px translation action
- support larger system text
- distinguish translation state without relying
  only on color

## 14. Visual Character

Translation should remain visually subordinate
to the original conversation.

Use BGM_GOLD only for the translation action,
target-language indicator, or important state.

Do not create a separate heavy translation panel
inside every message.
