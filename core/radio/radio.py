"""
BGM World Radio
Black Gold Messenger

Lightweight radio station directory foundation.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class BGMRadioStation:
    """Represents one radio station."""

    station_id: str
    name: str
    stream_url: str
    continent_id: str
    country_id: str
    description: str = ""

    def is_valid(self) -> bool:
        return bool(
            self.station_id.strip()
            and self.name.strip()
            and self.stream_url.strip()
            and self.continent_id.strip()
            and self.country_id.strip()
        )


@dataclass
class BGMRadioDirectory:
    """Lightweight radio station directory."""

    stations: dict[str, BGMRadioStation] = field(default_factory=dict)

    def add_station(self, station: BGMRadioStation) -> None:
        if not isinstance(station, BGMRadioStation):
            raise TypeError("station must be a BGMRadioStation.")

        if not station.is_valid():
            raise ValueError("Invalid radio station.")

        self.stations[station.station_id] = station

    def get_station(self, station_id: str) -> BGMRadioStation | None:
        return self.stations.get(station_id)

    def get_stations(
        self,
        continent_id: str | None = None,
        country_id: str | None = None,
    ) -> list[BGMRadioStation]:
        stations = list(self.stations.values())

        if continent_id is not None:
            stations = [
                station
                for station in stations
                if station.continent_id == continent_id
            ]

        if country_id is not None:
            stations = [
                station
                for station in stations
                if station.country_id == country_id
            ]

        return stations
