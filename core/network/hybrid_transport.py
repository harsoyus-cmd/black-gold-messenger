"""
BGM Hybrid Transport Layer
Supports routing over Local Wi-Fi, Standard Internet, and Satellite links.
"""
import asyncio
import logging

logger = logging.getLogger("BGMHybridNetwork")

class BaseTransport:
    async def send(self, recipient_id: str, data: bytes) -> bool:
        raise NotImplementedError

class WiFiTransport(BaseTransport):
    async def send(self, recipient_id: str, data: bytes) -> bool:
        logger.info("📡 Mengirim via Wi-Fi Lokal / Mesh...")
        return True

class InternetTransport(BaseTransport):
    async def send(self, recipient_id: str, data: bytes) -> bool:
        logger.info("🌍 Mengirim via Internet Publik / ISP...")
        return True

class SatelliteTransport(BaseTransport):
    async def send(self, recipient_id: str, data: bytes) -> bool:
        logger.info("🛰️ Mengirim via Tautan Satelit (High-Latency Fallback)...")
        return True

class BGMHybridRouter:
    def __init__(self):
        self.transports = {
            "wifi": WiFiTransport(),
            "internet": InternetTransport(),
            "satellite": SatelliteTransport()
        }

    async def route_message(self, recipient_id: str, data: bytes, preferred_mode: str = "auto"):
        """Memilih jalur terbaik secara dinamis."""
        if preferred_mode in self.transports:
            success = await self.transports[preferred_mode].send(recipient_id, data)
            if success:
                return preferred_mode

        # Fallback otomatis jika mode pilihan gagal
        for mode, transport in self.transports.items():
            logger.info(f"🔄 Mencoba fallback otomatis ke jalur: {mode}")
            if await transport.send(recipient_id, data):
                return mode
        
        raise ConnectionError("Semua jalur hibrid gagal dijangkau!")

if __name__ == "__main__":
    async def test():
        router = BGMHybridRouter()
        await router.route_message("PEER_XYZ", b"Test Data Hybrid", preferred_mode="satellite")
    
    asyncio.run(test())
