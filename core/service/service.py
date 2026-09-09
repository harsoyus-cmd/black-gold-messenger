"""
BGM Core Service
Black Gold Messenger

Lightweight orchestration boundary for BGM core modules.
"""

from core.identity import BGMIdentity
from core.protocol import BGMMessage
from core.network import BGMNetwork, export_network_passport
from core.storage import BGMStorage
from core.text import create_text_message
from core.mail import create_secure_mail_message
from core.media import create_media_message
from core.world import BGMWorld
from core.translation import BGMTranslationService
from core.radio import BGMRadioDirectory

class BGMService:
    """
    Lightweight service boundary for the BGM engine.

    Core modules remain independent. The service only coordinates
    them for the application layer.
    """

    def __init__(self, storage: BGMStorage, identity: BGMIdentity | None = None, network: BGMNetwork | None = None):
        if not isinstance(storage, BGMStorage):
            raise TypeError("storage must be a BGMStorage instance.")

        if identity is not None and not isinstance(identity, BGMIdentity):
            raise TypeError("identity must be a BGMIdentity instance.")

        if network is not None and not isinstance(network, BGMNetwork):
            raise TypeError("network must be a BGMNetwork instance.")

        self.storage = storage
        self.identity = identity
        self.network = network
        self.world = BGMWorld()
        self.translation_service = None
        self.radio_directory = BGMRadioDirectory()

    def initialize(self) -> None:
        """Initialize required local service storage."""

        self.storage.initialize()

    def create_text_message(
        self,
        sender_identity_id: str,
        sender_device_id: str,
        recipient_identity_id: str,
        text: str,
        session_key: bytes,
        key_id: str,
        associated_data: bytes | None = None,
    ) -> BGMMessage:
        """Create an encrypted BGM TEXT message through the Text Engine."""

        return create_text_message(
            sender_identity_id=sender_identity_id,
            sender_device_id=sender_device_id,
            recipient_identity_id=recipient_identity_id,
            text=text,
            session_key=session_key,
            key_id=key_id,
            associated_data=associated_data,
        )

    def create_secure_mail_message(
        self,
        sender_identity_id: str,
        sender_device_id: str,
        recipient_identity_id: str,
        subject: str,
        body: str,
        session_key: bytes,
        key_id: str,
        associated_data: bytes | None = None,
    ) -> BGMMessage:
        """Create an encrypted BGM MAIL message through the Mail Engine."""

        return create_secure_mail_message(
            sender_identity_id=sender_identity_id,
            sender_device_id=sender_device_id,
            recipient_identity_id=recipient_identity_id,
            subject=subject,
            body=body,
            session_key=session_key,
            key_id=key_id,
            associated_data=associated_data,
        )

    def create_media_message(
        self,
        sender_identity_id: str,
        sender_device_id: str,
        recipient_identity_id: str,
        media_type: str,
        name: str,
        size: int,
    ) -> BGMMessage:
        """Create a BGM media message through the Media Engine."""

        return create_media_message(
            sender_identity_id=sender_identity_id,
            sender_device_id=sender_device_id,
            recipient_identity_id=recipient_identity_id,
            media_type=media_type,
            name=name,
            size=size,
        )

    def save_message(self, message, status: str = "PENDING") -> None:
        """Store a BGM message through the existing storage module."""

        if not isinstance(message, BGMMessage):
            raise TypeError("message must be a BGMMessage.")

        self.storage.save_message(message, status=status)

    def get_message(self, message_id: str):
        """Retrieve a message through the existing storage module."""

        if not isinstance(message_id, str):
            raise TypeError("message_id must be a string.")

        if not message_id.strip():
            raise ValueError("message_id must not be empty.")

        return self.storage.get_message(message_id)

    def update_message_status(
        self,
        message_id: str,
        status: str,
    ) -> None:
        """Update message status through the existing storage module."""

        if not isinstance(message_id, str):
            raise TypeError("message_id must be a string.")

        if not message_id.strip():
            raise ValueError("message_id must not be empty.")

        if not isinstance(status, str):
            raise TypeError("status must be a string.")

        if not status.strip():
            raise ValueError("status must not be empty.")

        self.storage.update_status(
            message_id=message_id,
            status=status,
        )

    def get_pending_messages(self, limit: int = 50):
        """Retrieve pending messages through the existing storage module."""

        if not isinstance(limit, int):
            raise TypeError("limit must be an integer.")

        if limit <= 0:
            raise ValueError("limit must be greater than zero.")

        return self.storage.get_pending_messages(limit=limit)

    def get_world(self) -> BGMWorld:
        return self.world

    def set_translation_service(
        self,
        service: BGMTranslationService,
    ) -> None:
        if not isinstance(service, BGMTranslationService):
            raise TypeError(
                "service must be a BGMTranslationService."
            )

        self.translation_service = service

    def get_translation_service(
        self,
    ) -> BGMTranslationService | None:
        return self.translation_service

    def get_radio_directory(self) -> BGMRadioDirectory:
        return self.radio_directory

    def get_identity(self) -> BGMIdentity:
        """Return the configured BGM identity."""

        if self.identity is None:
            raise RuntimeError("Identity dependency is not configured.")

        return self.identity

    def get_network(self) -> BGMNetwork:
        """Return the configured BGM network."""

        if self.network is None:
            raise RuntimeError("Network dependency is not configured.")

        return self.network

    def get_network_passport(self) -> dict:
        """Return the Network Passport through the existing Network module."""

        if self.network is None:
            raise RuntimeError("Network dependency is not configured.")

        return export_network_passport(self.network)

    def process_pending(
        self,
        send_function,
        limit: int = 50,
        max_attempts: int = 3,
    ) -> int:
        """Process pending messages through the existing delivery module."""

        if not callable(send_function):
            raise TypeError("send_function must be callable.")

        if not isinstance(limit, int):
            raise TypeError("limit must be an integer.")

        if limit <= 0:
            raise ValueError("limit must be greater than zero.")

        if not isinstance(max_attempts, int):
            raise TypeError("max_attempts must be an integer.")

        if max_attempts <= 0:
            raise ValueError("max_attempts must be greater than zero.")

        from core.delivery import process_pending_messages

        return process_pending_messages(
            storage=self.storage,
            send_function=send_function,
            limit=limit,
            max_attempts=max_attempts,
        )
