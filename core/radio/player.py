"""
BGM Radio Player Foundation
Black Gold Messenger

Lightweight stream/player state.
"""


class BGMRadioPlayer:
    """Manages lightweight radio stream state."""

    STOPPED = "STOPPED"
    PLAYING = "PLAYING"
    PAUSED = "PAUSED"

    def __init__(self):
        self.state = self.STOPPED
        self.station_id: str | None = None
        self.stream_url: str | None = None

    def play(self, station_id: str, stream_url: str) -> None:
        if not station_id.strip():
            raise ValueError("Station ID must not be empty.")

        if not stream_url.strip():
            raise ValueError("Stream URL must not be empty.")

        self.station_id = station_id
        self.stream_url = stream_url
        self.state = self.PLAYING

    def pause(self) -> None:
        if self.state != self.PLAYING:
            raise ValueError("Radio is not playing.")

        self.state = self.PAUSED

    def stop(self) -> None:
        self.state = self.STOPPED
        self.station_id = None
        self.stream_url = None

    def is_playing(self) -> bool:
        return self.state == self.PLAYING
