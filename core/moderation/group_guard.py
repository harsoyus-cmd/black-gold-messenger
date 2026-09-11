"""
BGM Global Group Moderation Engine
Black Gold Messenger

Filters out pornography, politics, hate speech (SARA), conflict issues,
and profanity to maintain a constructive business and international growth environment.
"""
import re
import logging

logger = logging.getLogger("BGMModeration")

class BGMContentGuard:
    def __init__(self):
        self.blocked_keywords = [
            "politics", "election", "government", "conflict", "war", "religion", "racist", "hate",
            "porn", "adult", "sex", "xxx", "nude",
            "stupid", "idiot", "damn", "hell", "fuck", "shit"
        ]

    def inspect_message(self, text: str) -> tuple[bool, str]:
        """Memeriksa teks pesan apakah melanggar aturan moderasi Global Group."""
        lower_text = text.lower()
        
        for keyword in self.blocked_keywords:
            pattern = rf"\b{re.escape(keyword)}\b"
            if re.search(pattern, lower_text):
                logger.warning(f"🛡️ [Moderation Triggered] Pesan diblokir karena mengandung kata: '{keyword}'")
                return False, f"Message blocked: Violates Global Group policy (contains restricted content: '{keyword}')."
        
        return True, "Message approved for Global Group."

if __name__ == "__main__":
    guard = BGMContentGuard()
    
    msg1 = "Hello partners, let's discuss cross-border AI software distribution and digital marketing scaling."
    allowed1, reason1 = guard.inspect_message(msg1)
    print(f"Test 1 ('{msg1[:30]}...'): {'✅ Lolos' if allowed1 else '❌ Ditolak'} -> {reason1}")

    msg2 = "Let's talk about the upcoming controversial politics and government elections."
    allowed2, reason2 = guard.inspect_message(msg2)
    print(f"Test 2 ('{msg2[:30]}...'): {'✅ Lolos' if allowed2 else '❌ Ditolak'} -> {reason2}")
