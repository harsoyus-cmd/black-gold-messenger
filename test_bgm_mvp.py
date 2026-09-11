import asyncio
import os
import inspect
from core.storage.storage import BGMStorage
from core.service.service import BGMService, create_text_message
from core.identity.identity import BGMIdentity

async def run_mvp_diagnostics():
    print("========================================")
    print("🔬 [LAB BGM] Diagnostik MVP (Perbaikan Identitas)")
    print("========================================")
    
    try:
        # 1. Inspeksi Parameter BGMIdentity
        id_sig = inspect.signature(BGMIdentity.__init__)
        print(f"🔍 Parameter BGMIdentity: {id_sig}")

        # 2. Inisialisasi Storage Database
        db_path = "data/bgm_test.db"
        print(f"1️⃣ Menginisialisasi BGMStorage di [{db_path}]...")
        storage = BGMStorage(db_path)
        print("   ✅ Storage sukses.")

        # 3. Membuat Identitas Kriptografi yang Valid
        print("2️⃣ Membangkitkan Identitas Kriptografi...")
        # Simulasi kunci publik dan ID identitas berbasis bytes/string aman
        mock_identity_id = "ID_YUSUF_SECURE_001"
        mock_public_key = os.urandom(32) # Kunci publik kriptografi 256-bit
        
        identity = BGMIdentity(
            identity_id=mock_identity_id,
            public_key=mock_public_key
        )
        print(f"   ✅ BGMIdentity aktif (ID: {mock_identity_id})")

        # 4. Inisialisasi Service Utama
        print("3️⃣ Menginisialisasi BGMService (Orkestrator)...")
        bgm = BGMService(storage=storage, identity=identity)
        print("   ✅ BGMService aktif dan terikat.")

        # 5. Perakitan Pesan Terenkripsi E2EE
        print("4️⃣ Menguji Pembuatan Pesan E2EE...")
        session_key = os.urandom(32)
        msg = create_text_message(
            sender_identity_id=mock_identity_id,
            sender_device_id="TERMUX_DEV_01",
            recipient_identity_id="NODE_PEER_999",
            text="Halo dunia, uji coba BGM P2P sukses total!",
            session_key=session_key,
            key_id="KEY_TEST_2026"
        )
        print(f"   ✅ Pesan sukses dirakit: {msg.message_id}")
        print(f"   🔒 Ciphertext Payload: {msg.payload}")

        print("\n========================================")
        print("🎉 STATUS: SEMUA SUBSISTEM INTI 100% BERHASIL!")
        print("========================================")

    except Exception as e:
        print(f"\n❌ DIAGNOSTIK GAGAL: {type(e).__name__} - {e}")

if __name__ == "__main__":
    asyncio.run(run_mvp_diagnostics())
