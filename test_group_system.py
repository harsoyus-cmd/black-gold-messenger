import sqlite3
import os

class BGMGroupManager:
    def __init__(self, db_path="data/bgm_groups.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self._setup_tables()

    def _setup_tables(self):
        with self.conn:
            # Tabel Grup (Global / Private)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS groups (
                    group_id TEXT PRIMARY KEY,
                    group_name TEXT,
                    group_type TEXT, -- 'GLOBAL' atau 'PRIVATE'
                    creator_id TEXT,
                    created_at TEXT
                )
            """)
            # Tabel Anggota Grup
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS group_members (
                    group_id TEXT,
                    member_id TEXT,
                    role TEXT, -- 'ADMIN' atau 'MEMBER'
                    PRIMARY KEY (group_id, member_id)
                )
            """)

    def create_group(self, group_id: str, group_name: str, group_type: str, creator_id: str):
        with self.conn:
            self.conn.execute(
                "INSERT OR IGNORE INTO groups (group_id, group_name, group_type, creator_id, created_at) VALUES (?, ?, ?, ?, datetime('now'))",
                (group_id, group_name, group_type.upper(), creator_id)
            )
            self.conn.execute(
                "INSERT OR IGNORE INTO group_members (group_id, member_id, role) VALUES (?, ?, ?)",
                (group_id, creator_id, 'ADMIN')
            )
        print(f"👥 [{group_type.upper()} GROUP] Berhasil membuat grup: '{group_name}' (ID: {group_id})")

if __name__ == "__main__":
    manager = BGMGroupManager()
    # Uji buat Grup Global
    manager.create_group("GRP_GLOBAL_01", "Global Open Mesh", "GLOBAL", "USER_YUSUF")
    # Uji buat Grup Pribadi (Private)
    manager.create_group("GRP_PRIV_02", "Secure Private Squad", "PRIVATE", "USER_YUSUF")
    print("✅ Skrip verifikasi tabel grup berjalan sukses!")
