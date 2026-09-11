import os
import re

def audit_codebase():
    print("========================================")
    print("🔍 [LAB BGM] Memulai Audit Integritas Proyek")
    print("========================================")
    
    target_dirs = ["core", "apps/mobile", "tests"]
    todo_count = 0
    pass_count = 0
    not_implemented_count = 0
    
    file_stats = {"py": 0, "dart": 0}

    for d in target_dirs:
        if not os.path.exists(d):
            print(f"⚠️ Direktori tidak ditemukan: {d}")
            continue
        for root, _, files in os.walk(d):
            for file in files:
                ext = file.split('.')[-1]
                if ext in ["py", "dart"]:
                    file_stats[ext] += 1
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                            content = f.read()
                            
                            # Cari penanda pekerjaan belum selesai
                            todos = len(re.findall(r'#.*TODO', content, re.IGNORECASE))
                            passes = len(re.findall(r'\bpass\b', content))
                            not_imps = len(re.findall(r'NotImplementedError', content))
                            
                            todo_count += todos
                            not_implemented_count += not_imps
                            
                            if todos > 0 or not_imps > 0:
                                print(f"📌 [Catatan] {filepath} -> TODOs: {todos}, NotImp: {not_imps}")
                    except Exception as e:
                        print(f"❌ Gagal membaca {filepath}: {e}")

    print("\n----------------------------------------")
    print(f"📊 Statistik Berkas Kode:")
    print(f"  • Berkas Python (.py) : {file_stats['py']}")
    print(f"  • Berkas Dart (.dart) : {file_stats['dart']}")
    print("----------------------------------------")
    print(f"🔎 Hasil Pemindaian Status 'Belum Selesai':")
    print(f"  • Total Komentar TODO : {todo_count}")
    print(f"  • Total NotImplemented  : {not_implemented_count}")
    print("========================================")
    if todo_count == 0 and not_implemented_count == 0:
        print("🎉 Status Audit: BERSIH! Tidak ada kode sisa/stub.")
    else:
        print("⚠️ Status Audit: Ada beberapa catatan penanda di atas yang perlu ditinjau.")

if __name__ == "__main__":
    audit_codebase()
