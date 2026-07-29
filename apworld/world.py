from collections.abc import Mapping
from typing import Dict, Optional, Any

from worlds.AutoWorld import World
from Options import Option

from . import items, locations, regions, rules, web_world
from . import options as celesteclassic_options

class CelesteClassicWorld(World):
    """
    Celeste Classic is the original version of Celeste made for the PICO-8. You join Madeline as she climbs the titular mountain, facing thirty rooms of challenges and collecting Strawberries along the way. In the randomizer, certain mechanics such as Springs only appear after receiving a corresponding item.
    """

    game = "Celeste Classic"
    web = web_world.CelesteClassicWebWorld()
    options_dataclass = celesteclassic_options.CelesteClassicOptions
    options: celesteclassic_options.CelesteClassicOptions
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID
    origin_region_name = "Title Screen"
    ut_can_gen_without_yaml = True

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.CelesteClassicItem:
        return items.create_item_with_correct_classification(self, name)
    
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> dict[str, Any]:
        return {
            "options": self.options.as_dict("death_link", "death_link_amnesty", "strawberries_required"),
        }
    
    def generate_early(self) -> None:
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]

            slot_options: dict[str, Any] = slot_data.get("options", {})
            for key, value in slot_options.items():
                opt: Optional[Option] = getattr(self.options, key, None)
                if opt is not None:
                    setattr(self.options, key, opt.from_any(value))
    
    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return slot_data