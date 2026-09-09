"""
BGM World
Black Gold Messenger

Lightweight global geographic hierarchy.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class BGMContinent:
    """Represents a continent in the BGM World hierarchy."""

    continent_id: str
    name: str

    def is_valid(self) -> bool:
        return bool(self.continent_id.strip() and self.name.strip())


@dataclass(frozen=True)
class BGMCountry:
    """Represents a country within a continent."""

    country_id: str
    name: str
    continent_id: str

    def is_valid(self) -> bool:
        return bool(
            self.country_id.strip()
            and self.name.strip()
            and self.continent_id.strip()
        )


@dataclass
class BGMWorld:
    """Lightweight World directory."""

    continents: dict[str, BGMContinent] = field(default_factory=dict)
    countries: dict[str, BGMCountry] = field(default_factory=dict)

    def add_continent(self, continent: BGMContinent) -> None:
        if not isinstance(continent, BGMContinent):
            raise TypeError("continent must be a BGMContinent.")

        if not continent.is_valid():
            raise ValueError("Invalid continent.")

        self.continents[continent.continent_id] = continent

    def add_country(self, country: BGMCountry) -> None:
        if not isinstance(country, BGMCountry):
            raise TypeError("country must be a BGMCountry.")

        if not country.is_valid():
            raise ValueError("Invalid country.")

        if country.continent_id not in self.continents:
            raise ValueError("Country continent does not exist.")

        self.countries[country.country_id] = country

    def get_continent(self, continent_id: str) -> BGMContinent | None:
        return self.continents.get(continent_id)

    def get_country(self, country_id: str) -> BGMCountry | None:
        return self.countries.get(country_id)

    def get_countries(self, continent_id: str) -> list[BGMCountry]:
        return [
            country
            for country in self.countries.values()
            if country.continent_id == continent_id
        ]
