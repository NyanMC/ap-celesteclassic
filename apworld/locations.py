from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from .items import CelesteClassicItem

if TYPE_CHECKING:
    from .world import CelesteClassicWorld

LOCATION_NAME_TO_ID = {
    "100M": 1,
    "100M Strawberry": 2,
    "200M": 3,
    "300M": 4,
    "300M Strawberry": 5,
    "400M": 6,
    "400M Strawberry": 7,
    "500M": 8,
    "500M Strawberry": 9,
    "600M": 10,
    "700M": 11,
    "700M Strawberry": 12,
    "800M": 13,
    "900M": 14,
    "900M Strawberry": 15,
    "1000M": 16,
    "1100M": 17,
    "Old Site": 18,
    "Old Site Strawberry": 19,
    "1300M": 20,
    "1300M Strawberry": 21,
    "1400M": 22,
    "1400M Strawberry": 23,
    "1500M": 24,
    "1500M Strawberry": 25,
    "1600M": 26,
    "1700M": 27,
    "1700M Strawberry": 28,
    "1800M": 29,
    "1900M": 30,
    "1900M Strawberry": 31,
    "2000M": 32,
    "2100M": 33,
    "2200M": 34,
    "2300M": 35,
    "2300M Strawberry": 36,
    "2400M": 37,
    "2500M": 38,
    "2500M Strawberry": 39,
    "2600M": 40,
    "2600M Strawberry": 41,
    "2700M": 42,
    "2800M": 43,
    "2800M Strawberry": 44,
    "2900M": 45,
    "2900M Strawberry": 46,
    "3000M": 47,
    "3000M Strawberry": 48
}

class CelesteClassicLocation(Location):
    game = "Celeste Classic"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: CelesteClassicWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: CelesteClassicWorld) -> None:
    world.get_region("Title Screen").add_locations(get_location_names_with_ids(["100M","200M","300M","400M","100M Strawberry","300M Strawberry","400M Strawberry"]), CelesteClassicLocation)
    world.get_region("500M").add_locations(get_location_names_with_ids(["500M","600M","700M","800M","900M","500M Strawberry","700M Strawberry","900M Strawberry"]), CelesteClassicLocation)
    world.get_region("1000M").add_locations(get_location_names_with_ids(["1000M","1100M"]), CelesteClassicLocation)
    world.get_region("Old Site").add_locations(get_location_names_with_ids(["Old Site","1300M","1400M","Old Site Strawberry","1300M Strawberry","1400M Strawberry"]), CelesteClassicLocation)
    world.get_region("1500M").add_locations(get_location_names_with_ids(["1500M","1600M","1700M","1800M","1900M","1500M Strawberry","1700M Strawberry","1900M Strawberry"]), CelesteClassicLocation)
    world.get_region("2000M").add_locations(get_location_names_with_ids(["2000M","2100M"]), CelesteClassicLocation)
    world.get_region("2200M").add_locations(get_location_names_with_ids(["2200M","2300M","2400M","2300M Strawberry"]), CelesteClassicLocation)
    world.get_region("2500M").add_locations(get_location_names_with_ids(["2500M","2600M","2700M","2800M","2900M","3000M","2500M Strawberry","2600M Strawberry","2800M Strawberry","2900M Strawberry","3000M Strawberry"]), CelesteClassicLocation)

    



def create_events(world: CelesteClassicWorld) -> None:
    summit = world.get_region("Summit")

    summit.add_event(
        "Summit", "Victory", location_type=CelesteClassicLocation, item_type=CelesteClassicItem
    )