from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

class CelesteClassicWebWorld(WebWorld):
    game = "Celeste Classic"
    theme = "ice"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Celeste Classic for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["ChromaNyan"],
    )
    tutorials = [setup_en]