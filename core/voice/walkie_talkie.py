"""
BGM Walkie-Talkie / Radio Panggil Room Manager
Black Gold Messenger
"""
class BGMWalkieTalkieSystem:
    def __init__(self):
        self.rooms = {} # Format: { "room_id": [list_of_users] }

    def join_room(self, room_id: str, user_id: str):
        if room_id not in self.rooms:
            self.rooms[room_id] = []
        if user_id not in self.rooms[room_id]:
            self.rooms[room_id].append(user_id)
        print(f"🎙️ [Walkie-Talkie] Pengguna '{user_id}' bergabung ke Room ID: '{room_id}'")

    def broadcast_ptt_audio(self, room_id: str, sender_id: str, audio_size_kb: int):
        """Mengirim suara PTT (Push-to-Talk) hanya ke sesama anggota di Room ID yang sama."""
        if room_id in self.rooms and sender_id in self.rooms[room_id]:
            receivers = [u for u in self.rooms[room_id] if u != sender_id]
            print(f"📡 [PTT Transmission] Room [{room_id}] | {sender_id} mengirim suara ({audio_size_kb} KB) ke {len(receivers)} pendengar.")
            return True
        else:
            print(f"❌ [Access Denied] Pengguna {sender_id} tidak berada di Room ID {room_id}")
            return False

if __name__ == "__main__":
    wt = BGMWalkieTalkieSystem()
    
    # Simulasi Pengguna Masuk Room
    wt.join_room("BGM-TRADE-ASIA", "Yusuf_ID")
    wt.join_room("BGM-TRADE-ASIA", "Partner_SG")
    
    # Simulasi Transmisi Suara Walkie-Talkie
    wt.broadcast_ptt_audio("BGM-TRADE-ASIA", "Yusuf_ID", audio_size_kb=15)
