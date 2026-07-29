from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import CelesteClassicWorld

def create_and_connect_regions(world: CelesteClassicWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: CelesteClassicWorld) -> None:
    title = Region("Title Screen", world.player, world.multiworld)
    regions = [title]
    regions.append(Region("500M", world.player, world.multiworld))
    regions.append(Region("1000M", world.player, world.multiworld))
    regions.append(Region("Old Site", world.player, world.multiworld))
    regions.append(Region("1500M", world.player, world.multiworld))
    regions.append(Region("2000M", world.player, world.multiworld))
    regions.append(Region("2200M", world.player, world.multiworld))
    regions.append(Region("2500M", world.player, world.multiworld))
    regions.append(Region("Summit", world.player, world.multiworld))

    world.multiworld.regions += regions

def connect_regions(world: CelesteClassicWorld) -> None:
    title = world.get_region("Title Screen")
    m500 = world.get_region("500M")
    m1000 = world.get_region("1000M")
    m1200 = world.get_region("Old Site")
    m1500 = world.get_region("1500M")
    m2000 = world.get_region("2000M")
    m2200 = world.get_region("2200M")
    m2500 = world.get_region("2500M")
    m3100 = world.get_region("Summit")

    title.connect(m500, "Title to 500M", Has("500M Checkpoint") | (Has("Springs") & Has("Crumbling Blocks")))
    title.connect(m1000, "Title to 1000M", Has("1000M Checkpoint"))
    title.connect(m1200, "Title to Old Site", Has("Old Site Checkpoint"))
    title.connect(m1500, "Title to 1500M", Has("1500M Checkpoint"))
    title.connect(m2000, "Title to 2000M", Has("2000M Checkpoint"))
    title.connect(m2200, "Title to 2200M", Has("2200M Checkpoint"))
    title.connect(m2500, "Title to 2500M", Has("2500M Checkpoint"))
    m500.connect(m1000, "500M to 1000M", Has("Balloons") & Has("White Clouds") & Has("Crumbling Blocks") & Has("Springs"))
    m1000.connect(m1200, "1000M to Old Site", Has("Crumbling Blocks") & Has("Balloons") & Has("White Clouds"))
    m1200.connect(m1500, "Old Site to 1500M", Has("Balloons") & Has("Crumbling Blocks") & Has("Springs"))
    m1500.connect(m2000, "1500M to 2000M", Has("Crumbling Blocks") & Has("Springs") & Has("Balloons") & Has("White Clouds"))
    m2000.connect(m2200, "2000M to 2200M", Has("Crumbling Blocks") & Has("Balloons") & Has("Springs"))
    m2200.connect(m2500, "2200M to 2500M", Has("Double Dash"))
    m2500.connect(m3100, "2500M to Summit", Has("Double Dash") & Has("Crumbling Blocks") & Has("Springs") & Has("Balloons"))