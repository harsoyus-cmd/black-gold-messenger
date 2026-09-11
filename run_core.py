import asyncio
import inspect
import core.service.service as bgm_service

async def boot_sequence():
    print("========================================")
    print("🔬 [LAB BGM] Memulai Proses Booting Core")
    print("========================================")
    
    # Introspeksi arsitektur: Mencari kelas utama penggerak BGM
    classes = [name for name, obj in inspect.getmembers(bgm_service) if inspect.isclass(obj)]
    functions = [name for name, obj in inspect.getmembers(bgm_service) if inspect.isfunction(obj)]
    
    print(f"📦 Kelas terdeteksi   : {classes}")
    print(f"⚙️ Fungsi terdeteksi : {functions}")
    print("✅ Introspeksi Core Python selesai!")
    print("========================================")

if __name__ == '__main__':
    asyncio.run(boot_sequence())
