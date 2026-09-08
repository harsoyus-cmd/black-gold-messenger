"""
BGM Local Storage
Black Gold Messenger

Lightweight SQLite persistence for BGM messages.
"""

import sqlite3
from pathlib import Path


STORAGE_PROTOCOL_VERSION = "0.1"

MESSAGE_STATUSES = (
    "PENDING",
    "SENT",
    "DELIVERED",
    "READ",
    "FAILED",
)


class BGMStorage:
    """Lightweight SQLite storage for BGM messages."""

    def __init__(self, database_path: str | Path):
        self.database_path = Path(database_path)

    def initialize(self) -> None:
        """Create the database and required message schema."""

        self.database_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with sqlite3.connect(self.database_path) as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS messages (
                    message_id TEXT PRIMARY KEY,
                    sender_identity_id TEXT NOT NULL,
                    sender_device_id TEXT NOT NULL,
                    recipient_identity_id TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    message_type TEXT NOT NULL,
                    payload TEXT NOT NULL,
                    status TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )

            connection.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_messages_created_at
                ON messages(created_at)
                """
            )

            connection.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_messages_status
                ON messages(status)
                """
            )

            connection.commit()

    def save_message(
        self,
        message,
        status: str = "PENDING",
    ) -> None:
        """Persist a BGMMessage."""

        if status not in MESSAGE_STATUSES:
            raise ValueError("Invalid message status.")

        self.initialize()

        with sqlite3.connect(self.database_path) as connection:
            connection.execute(
                """
                INSERT INTO messages (
                    message_id,
                    sender_identity_id,
                    sender_device_id,
                    recipient_identity_id,
                    timestamp,
                    message_type,
                    payload,
                    status,
                    created_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    message.message_id,
                    message.sender_identity_id,
                    message.sender_device_id,
                    message.recipient_identity_id,
                    message.timestamp,
                    message.message_type.value,
                    message.payload,
                    status,
                    message.timestamp,
                ),
            )
            connection.commit()

    def get_message(self, message_id: str):
        """Retrieve one message by ID."""

        self.initialize()

        with sqlite3.connect(self.database_path) as connection:
            connection.row_factory = sqlite3.Row

            row = connection.execute(
                """
                SELECT
                    message_id,
                    sender_identity_id,
                    sender_device_id,
                    recipient_identity_id,
                    timestamp,
                    message_type,
                    payload,
                    status,
                    created_at
                FROM messages
                WHERE message_id = ?
                """,
                (message_id,),
            ).fetchone()

        return dict(row) if row else None

    def update_status(
        self,
        message_id: str,
        status: str,
    ) -> None:
        """Update the status of a stored message."""

        if status not in MESSAGE_STATUSES:
            raise ValueError("Invalid message status.")

        self.initialize()

        with sqlite3.connect(self.database_path) as connection:
            cursor = connection.execute(
                """
                UPDATE messages
                SET status = ?
                WHERE message_id = ?
                """,
                (status, message_id),
            )

            if cursor.rowcount == 0:
                raise ValueError("Message not found.")

            connection.commit()

    def get_pending_messages(self, limit: int = 50):
        """Retrieve pending messages in chronological order."""

        if not isinstance(limit, int):
            raise TypeError("Limit must be an integer.")

        if limit <= 0:
            raise ValueError("Limit must be greater than zero.")

        self.initialize()

        with sqlite3.connect(self.database_path) as connection:
            connection.row_factory = sqlite3.Row

            rows = connection.execute(
                """
                SELECT
                    message_id,
                    sender_identity_id,
                    sender_device_id,
                    recipient_identity_id,
                    timestamp,
                    message_type,
                    payload,
                    status,
                    created_at
                FROM messages
                WHERE status = 'PENDING'
                ORDER BY created_at ASC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()

        return [dict(row) for row in rows]

    def delete_message(self, message_id: str) -> None:
        """Delete one stored message."""

        self.initialize()

        with sqlite3.connect(self.database_path) as connection:
            connection.execute(
                """
                DELETE FROM messages
                WHERE message_id = ?
                """,
                (message_id,),
            )
            connection.commit()


def storage_protocol_version() -> str:
    """Return the current BGM Storage protocol version."""

    return STORAGE_PROTOCOL_VERSION
