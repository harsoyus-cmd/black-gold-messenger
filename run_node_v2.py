import asyncio
import inspect
from core.storage.storage import BGMStorage
from core.service.service import BGMService, create_text_message

async def start_node():
    print("========================================")
    print("🌐 [LAB BGM] Memulai Node P2P Lokal (Tahap 2)")
    print("========================================")
    
    try:
        # 1. Cek parameter BGMStorage
        storage_sig = inspect.signature(BGMStorage.__init__)
        print(f"🔍 Parameter BGMStorage: {storage_sig}")
        
        # 2. Inisialisasi Database Storage
        print("💾 Menginisialisasi BGMStorage...")
        # Jika butuh argumen (selain self), kita berikan path db-nya
        if len(storage_sig.parameters) > 1: 
            storage = BGMStorage("data/bgm.db")
        else:
            storage = BGMStorage()
            
        print("✅ BGMStorage siap!")
        
        # 3. Inisialisasi BGMService dengan storage
        print("⚙️ Melakukan inisialisasi BGMService...")
        bgm = BGMService(storage=storage)
        print("✅ Mesin utama BGMService berhasil dihidupkan!")
        
        # 4. Merakit pesan eksperimen
        print("✉️ Merakit dan memvalidasi struktur pesan...")
        test_msg = create_text_message(
            sender_id="YUSUF_NODE_01", 
            recipient_id="ECHO_NODE", 
            content="Hello BGM World! Mesin sudah menyala."
        )
        print(f"✅ Pesan sukses dirakit:\n{test_msg}")
        
    except Exception as e:
        print(f"\n❌ Eksekusi terhenti: {type(e).__name__} - {e}")

    print("========================================")

if __name__ == '__main__':
    asyncio.run(start_node())
