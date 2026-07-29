from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import CelesteClassicWorld

ITEM_NAME_TO_ID = {
    "Strawberry": 1,
    "Springs": 2,
    "Balloons": 3,
    "Crumbling Blocks": 4,
    "Breakable Blocks": 5,
    "White Clouds": 6,
    "Keys": 7,
    "Double Dash": 8,
    "Raspberry": 9,
    "500M Checkpoint": 10,
    "1000M Checkpoint": 11,
    "1500M Checkpoint": 12,
    "2000M Checkpoint": 13,
    "2500M Checkpoint": 14,
    "Old Site Checkpoint": 15,
    "2200M Checkpoint": 16,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Strawberry": ItemClassification.progression_deprioritized_skip_balancing,
    "Springs": ItemClassification.progression,
    "Balloons": ItemClassification.progression,
    "Crumbling Blocks": ItemClassification.progression,
    "Breakable Blocks": ItemClassification.progression,
    "White Clouds": ItemClassification.progression,
    "Keys": ItemClassification.progression,
    "Double Dash": ItemClassification.progression | ItemClassification.useful,
    "Raspberry": ItemClassification.filler,
    "500M Checkpoint": ItemClassification.progression,
    "1000M Checkpoint": ItemClassification.progression,
    "1500M Checkpoint": ItemClassification.progression,
    "2000M Checkpoint": ItemClassification.progression,
    "2500M Checkpoint": ItemClassification.progression,
    "Old Site Checkpoint": ItemClassification.progression,
    "2200M Checkpoint": ItemClassification.progression,
}

class CelesteClassicItem(Item):
    game = "Celeste Classic"

def get_random_filler_item_name(world: CelesteClassicWorld) -> str:
    return "Raspberry"

def create_item_with_correct_classification(world: CelesteClassicWorld, name: str) -> CelesteClassicItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return CelesteClassicItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: CelesteClassicWorld) -> None:

    important_prog = ["Springs", "Balloons", "Crumbling Blocks", "Breakable Blocks", "White Clouds", "Keys", "Double Dash"]
    checkpoints_interval = ["500M", "1000M", "1500M", "2000M", "2500M"]
    checkpoints_important = ["Old Site", "2200M"]

    itempool: list[Item] = []

    for item in important_prog:
        itempool.append(world.create_item(item))

    for name in checkpoints_interval:
        itempool.append(world.create_item(name+" Checkpoint"))

    for name in checkpoints_important:
        itempool.append(world.create_item(name+" Checkpoint"))

    for _ in range(18):
        itempool.append(world.create_item("Strawberry"))
    
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool