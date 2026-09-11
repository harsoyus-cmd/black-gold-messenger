import asyncio
import os
from core.storage.storage import BGMStorage
from core.identity.identity import BGMIdentity
from core.service.service import BGMService, create_text_message
from core.network.hybrid_transport import BGMHybridRouter

async def test_hybrid_pipeline():
    print("========================================")
    print("🛰️ [LAB BGM] Uji Integrasi Pesan & Hybrid Router")
    print("========================================")
    
    # 1. Setup komponen inti
    storage = BGMStorage("data/bgm_hybrid.db")
    identity = BGMIdentity(identity_id="NODE_YUSUF", public_key=os.urandom(32))
    bgm = BGMService(storage=storage, identity=identity)
    router = BGMHybridRouter()
    
    # 2. Buat pesan terenkripsi
    session_key = os.urandom(32)
    msg = create_text_message(
        sender_identity_id="NODE_YUSUF",
        sender_device_id="TERMUX_DEV",
        recipient_identity_id="NODE_REMOTE",
        text="Pesan satelit darurat lintas batas!",
        session_key=session_key,
        key_id="KEY_HYBRID_01"
    )
    
    # 3. Serialisasi payload untuk dikirim via router hibrid
    payload_bytes = str(msg.payload).encode('utf-8')
    
    # 4. Kirim menggunakan jalur satelit sebagai simulasi
    active_mode = await router.route_message(
        recipient_id="NODE_REMOTE", 
        data=payload_bytes, 
        preferred_mode="satellite"
    )
    
    print(f"\n✅ Pesan berhasil dikirim melalui jalur: {active_mode.upper()}")
    print(f"📦 ID Pesan: {msg.message_id}")
    print("========================================")

if __name__ == "__main__":
    asyncio.run(test_hybrid_pipeline())
