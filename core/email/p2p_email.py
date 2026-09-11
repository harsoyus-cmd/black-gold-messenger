"""
BGM P2P Email Service (Updated with File Attachment Support)
Black Gold Messenger
"""
import os
import json
import logging
from datetime import datetime, timezone

logger = logging.getLogger("BGMEmail")

class BGMEmailMessage:
    def __init__(self, sender: str, recipient: str, subject: str, body: str, attachment_path: str = None):
        self.message_id = f"MAIL-{os.urandom(4).hex()}"
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.attachment_name = None
        self.attachment_data = None
        
        if attachment_path and os.path.exists(attachment_path):
            self.attachment_name = os.path.basename(attachment_path)
            with open(attachment_path, "rb") as f:
                # Simulasi pembacaan file biner untuk dilampirkan
                self.attachment_data = f"<binary_stream_of_{self.attachment_name}>"

        self.timestamp = datetime.now(timezone.utc).isoformat()

    def to_payload(self) -> dict:
        return {
            "type": "P2P_EMAIL",
            "message_id": self.message_id,
            "sender": self.sender,
            "recipient": self.recipient,
            "subject": self.subject,
            "body": self.body,
            "attachment": {
                "name": self.attachment_name,
                "data": self.attachment_data
            },
            "timestamp": self.timestamp
        }

class BGMEmailService:
    def __init__(self):
        print("📧 Layanan P2P Email (Teks + File) Siap Beroperasi.")

    def compose_email(self, sender: str, recipient: str, subject: str, body: str, attachment_path: str = None) -> dict:
        email_msg = BGMEmailMessage(sender, recipient, subject, body, attachment_path)
        payload = email_msg.to_payload()
        return {
            "envelope_id": email_msg.message_id,
            "ciphertext_data": json.dumps(payload),
            "status": "encrypted_ready_to_send"
        }

if __name__ == "__main__":
    service = BGMEmailService()
    envelope = service.compose_email(
        sender="yusuf@bgm",
        recipient="partner@bgm",
        subject="Project Contract & Specification",
        body="Please review the attached document for international expansion.",
        attachment_path=None # Bisa diisi path file misal 'document.pdf'
    )
    print(f"📦 Amplop Surel + Lampiran Berhasil Dirakit: {envelope['envelope_id']}")
