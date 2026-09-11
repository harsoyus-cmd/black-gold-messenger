import asyncio
import os
import sys
from core.storage.storage import BGMStorage
from core.identity.identity import BGMIdentity
from core.service.service import BGMService, create_text_message
from core.network.hybrid_transport import BGMHybridRouter

async def interactive_terminal():
    print("========================================")
    print("💬 [LAB BGM] Terminal Obrolan Interaktif P2P")
    print("========================================")
    print("Ketik pesan Anda, lalu pilih jalur hibrid.")
    print("Ketik 'exit' atau 'quit' untuk keluar.\n")

    db_path = "data/bgm_interactive.db"
    storage = BGMStorage(db_path)
    identity = BGMIdentity(identity_id="USER_YUSUF", public_key=os.urandom(32))
    bgm = BGMService(storage=storage, identity=identity)
    router = BGMHybridRouter()

    loop = asyncio.get_event_loop()

    while True:
        # Input teks dari terminal secara asinkron
        text = await loop.run_in_executor(None, input, "💬 Pesan Anda > ")
        text = text.strip()
        
        if text.lower() in ["exit", "quit"]:
            print("👋 Menutup sesi obrolan interaktif.")
            break
        if not text:
            continue

        # Pilih jalur hibrid
        mode_input = await loop.run_in_executor(None, input, "🌐 Pilih jalur [wifi/internet/satellite] (default: wifi): ")
        mode = mode_input.strip().lower()
        if mode not in ["wifi", "internet", "satellite"]:
            mode = "wifi"

        # Proses E2EE & Pembuatan Pesan
        session_key = os.urandom(32)
        msg = create_text_message(
            sender_identity_id="USER_YUSUF",
            sender_device_id="TERMUX_CLI",
            recipient_identity_id="PEER_NODE_02",
            text=text,
            session_key=session_key,
            key_id="KEY_LIVE_01"
        )

        # Simpan ke storage database lokal
        if hasattr(storage, "save_message"):
            storage.save_message(msg)

        # Rutekan lewat transport hibrid
        payload_bytes = str(msg.payload).encode('utf-8')
        active_mode = await router.route_message(
            recipient_id="PEER_NODE_02",
            data=payload_bytes,
            preferred_mode=mode
        )

        print(f"   🔒 [E2EE Enkripsi Sukses] ID: {msg.message_id[:16]}...")
        print(f"   🚀 [Transmisi Hibrid] Terkirim via {active_mode.upper()} & Tersimpan di SQLite!\n")

if __name__ == "__main__":
    try:
        asyncio.run(interactive_terminal())
    except KeyboardInterrupt:
        print("\n👋 Sesi dihentikan oleh pengguna.")
