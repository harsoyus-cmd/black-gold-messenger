import sqlite3
from datetime import datetime, timezone, timedelta

class BGMLocalRetentionManager:
    def __init__(self, db_path="data/bgm_retention.db"):
        self.conn = sqlite3.connect(db_path)
        self._setup_tables()

    def _setup_tables(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    message_id TEXT PRIMARY KEY,
                    payload TEXT,
                    media_type TEXT,
                    timestamp TEXT
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS emails (
                    email_id TEXT PRIMARY KEY,
                    subject TEXT,
                    body TEXT,
                    timestamp TEXT,
                    is_saved INTEGER DEFAULT 0
                )
            """)

    def execute_auto_cleanup(self, retention_days: int):
        """Menghapus data lama berdasarkan pilihan hari, mengamankan email yang ditandai."""
        cutoff = (datetime.now(timezone.utc) - timedelta(days=retention_days)).isoformat()
        
        with self.conn:
            cursor_msg = self.conn.execute("DELETE FROM messages WHERE timestamp < ?", (cutoff,))
            deleted_msgs = cursor_msg.rowcount

            cursor_email = self.conn.execute(
                "DELETE FROM emails WHERE timestamp < ? AND is_saved = 0", (cutoff,)
            )
            deleted_emails = cursor_email.rowcount

        print(f"🧹 [Auto-Cleanup] Berhasil membersihkan {deleted_msgs} pesan/media dan {deleted_emails} surel kedaluwarsa (> {retention_days} hari).")

    def toggle_save_email(self, email_id: str, save: bool):
        """Menandai email agar kebal dari penghapusan otomatis."""
        with self.conn:
            self.conn.execute("UPDATE emails SET is_saved = ? WHERE email_id = ?", (1 if save else 0, email_id))
        status = "Disimpan Permanen" if save else "Masuk Jadwal Auto-Delete"
        print(f"📌 [Email Manager] Surel {email_id} diatur ke status: {status}")

if __name__ == "__main__":
    manager = BGMLocalRetentionManager()
    manager.execute_auto_cleanup(retention_days=30)
