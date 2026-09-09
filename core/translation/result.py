"""
BGM Translation Result
Black Gold Messenger

Preserves original text and translated display text.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BGMTranslationResult:
    """Represents original text and its translated display text."""

    original_text: str
    translated_text: str
    source_language: str
    target_language: str

    def is_valid(self) -> bool:
        return bool(
            self.original_text.strip()
            and self.translated_text.strip()
            and self.source_language.strip()
            and self.target_language.strip()
        )
