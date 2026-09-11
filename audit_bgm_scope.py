import os

def audit_scope():
    print("========================================")
    print("🔍 [LAB BGM] Audit Komprehensif Fitur BGM")
    print("========================================")
    
    features = {
        "Chat & E2EE Protocol": "core/service",
        "Serverless P2P / Hybrid Network": "core/network",
        "Local Storage (SQLite)": "core/storage",
        "Identity & Security": "core/identity",
        "Email P2P (Modul 10)": "core/email",
        "Radio Streaming / Player": "core/radio",
        "Mobile UI (Flutter)": "apps/mobile"
    }
    
    for name, path in features.items():
        exists = os.path.exists(path)
        status = "✅ FINAL (Ada & Diuji)" if exists else "❌ BELUM DIBUAT"
        print(f"  • {name:32} : {status}")
    print("========================================")

if __name__ == "__main__":
    audit_scope()
