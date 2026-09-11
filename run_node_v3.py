import asyncio
import os
from core.storage.storage import BGMStorage
from core.service.service import BGMService, create_text_message

async def start_node():
    print("========================================")
    print("🔐 [LAB BGM] Simulasi Kriptografi & Pesan (Tahap 3)")
    print("========================================")
    
    try:
        # 1. Inisialisasi Service
        print("💾 Menginisialisasi Database & Service...")
        storage = BGMStorage("data/bgm.db")
        bgm = BGMService(storage=storage)
        
        # 2. Membuat Material Kriptografi (Simulasi)
        print("🔑 Membangkitkan 'Session Key' acak (32-bytes / 256-bit)...")
        dummy_session_key = os.urandom(32) 
        
        # 3. Merakit Pesan Terenkripsi
        print("✉️ Merakit pesan teks ke dalam BGMMessage...")
        test_msg = create_text_message(
            sender_identity_id="YUSUF_ID_001",
            sender_device_id="DEV_TERMUX_01",
            recipient_identity_id="TARGET_ID_999",
            text="Operasi Sandi Black Gold Messenger berhasil!",
            session_key=dummy_session_key,
            key_id="KEY_2026_01"
        )
        
        print("\n✅ Eksekusi Pembuatan Pesan BERHASIL!")
        print("========================================")
        print("Membongkar Metadata Pesan BGM:")
        print(f"  • Kelas Objek : {type(test_msg).__name__}")
        
        # Mengekstrak atribut yang tersedia di dalam objek pesan
        for attr in dir(test_msg):
            if not attr.startswith("_") and not callable(getattr(test_msg, attr)):
                val = getattr(test_msg, attr)
                # Potong nilai bytes jika terlalu panjang agar rapi di terminal
                if isinstance(val, bytes) and len(val) > 32:
                    val = f"{val[:16]}... ({len(val)} bytes)"
                print(f"  • {attr:15}: {val}")
                
    except Exception as e:
        print(f"\n❌ Eksekusi terhenti: {type(e).__name__} - {e}")

    print("========================================")

if __name__ == '__main__':
    asyncio.run(start_node())
