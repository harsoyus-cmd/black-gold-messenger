"""
BGM Translation Service Hook
Black Gold Messenger

Lightweight translation service interface.
"""


class BGMTranslationService:
    """Base translation service hook."""

    def translate(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ) -> str:
        """Translate text through an external or local implementation."""

        raise NotImplementedError(
            "Translation service implementation is not configured."
        )
