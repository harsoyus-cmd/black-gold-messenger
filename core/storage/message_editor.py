from datetime import datetime, timezone, timedelta

def can_edit_message(message_timestamp_str: str) -> tuple[bool, str]:
    """Memeriksa apakah pesan masih dalam batas waktu 15 menit untuk diedit."""
    msg_time = datetime.fromisoformat(message_timestamp_str)
    now = datetime.now(timezone.utc)
    
    # Batas waktu 15 menit
    time_difference = now - msg_time
    if time_difference <= timedelta(minutes=15):
        return True, "Edit allowed: Within 15-minute window."
    else:
        return False, "Edit rejected: 15-minute time window has expired."

if __name__ == "__main__":
    # Simulasi pengujian waktu pesan baru (Baru saja dikirim)
    recent_msg_time = datetime.now(timezone.utc).isoformat()
    allowed, reason = can_edit_message(recent_msg_time)
    print(f"Uji Edit Pesan Baru: {'✅ Diizinkan' if allowed else '❌ Ditolak'} -> {reason}")
