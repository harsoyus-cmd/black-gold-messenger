import asyncio
import inspect
from core.service.service import BGMService, create_text_message

async def start_node():
    print("========================================")
    print("🌐 [LAB BGM] Memulai Node P2P Lokal")
    print("========================================")
    
    # 1. Mengecek struktur konstruktor BGMService
    sig = inspect.signature(BGMService.__init__)
    print(f"🔍 Parameter yang dibutuhkan BGMService: {sig}")
    
    try:
        # 2. Mencoba inisialisasi layanan (asumsi parameter default)
        print("⚙️ Melakukan inisialisasi BGMService...")
        bgm = BGMService()
        
        # 3. Mencoba membuat satu pesan BGM mentah
        print("✉️ Merakit pesan teks...")
        test_msg = create_text_message(
            sender_id="SYS_ADMIN", 
            recipient_id="ECHO_NODE", 
            content="Hello BGM World!"
        )
        print(f"✅ Pesan sukses dirakit:\n{test_msg}")
        
    except TypeError as e:
        print(f"\n⚠️ BGMService gagal dijalankan karena kurang parameter: {e}")
        print("Ini wajar, kita perlu memasukkan dependensi yang tepat (misal: db_path).")
    except Exception as e:
        print(f"\n❌ Eksekusi terhenti: {e}")

    print("========================================")

if __name__ == '__main__':
    asyncio.run(start_node())
