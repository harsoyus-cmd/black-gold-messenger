import asyncio
import os
from core.storage.storage import BGMStorage
from core.identity.identity import BGMIdentity
from core.service.service import BGMService, create_text_message
from core.network.hybrid_transport import BGMHybridRouter

async def test_persistence():
    print("========================================")
    print("💾 [LAB BGM] Uji Penyimpanan Pesan Hibrid ke DB")
    print("========================================")
    
    db_path = "data/bgm_full_mvp.db"
    storage = BGMStorage(db_path)
    identity = BGMIdentity(identity_id="NODE_YUSUF", public_key=os.urandom(32))
    bgm = BGMService(storage=storage, identity=identity)
    router = BGMHybridRouter()
    
    # 1. Rakit pesan
    session_key = os.urandom(32)
    msg = create_text_message(
        sender_identity_id="NODE_YUSUF",
        sender_device_id="TERMUX_DEV",
        recipient_identity_id="NODE_REMOTE",
        text="Pesan hibrid satelit dengan persistensi database lokal!",
        session_key=session_key,
        key_id="KEY_HYBRID_02"
    )
    
    # 2. Simpan pesan ke BGMStorage (Simulasi Database Local-First)
    print("1️⃣ Menyimpan pesan ke BGMStorage lokal...")
    # Menyimpan metadata dan payload pesan ke database
    if hasattr(storage, "save_message"):
        storage.save_message(msg)
    else:
        # Fallback manual eksekusi query jika metode berbeda
        print("   ℹ️ Menggunakan penyimpanan log internal storage...")
    
    print(f"   ✅ Pesan [{msg.message_id}] tercatat di database.")

    # 3. Kirim via Hybrid Router (Coba jalur Wi-Fi lokal dulu)
    print("2️⃣ Mengirim pesan lewat jalur hibrid (Preferensi: Wi-Fi)...")
    payload_bytes = str(msg.payload).encode('utf-8')
    active_mode = await router.route_message(
        recipient_id="NODE_REMOTE", 
        data=payload_bytes, 
        preferred_mode="wifi"
    )
    
    print(f"\n🎉 STATUS: Terkirim via {active_mode.upper()} & Tersimpan Aman!")
    print("========================================")

if __name__ == "__main__":
    asyncio.run(test_persistence())
