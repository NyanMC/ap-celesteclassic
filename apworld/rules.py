from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import CelesteClassicWorld

def set_all_rules(world: CelesteClassicWorld) -> None:
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_location_rules(world: CelesteClassicWorld) -> None:

    # 100M-400M
    world.set_rule(world.get_location("100M Strawberry"), Has("Breakable Blocks"))
    world.set_rule(world.get_location("300M Strawberry"), Has("Springs"))
    world.set_rule(world.get_location("400M"), Has("Springs"))
    world.set_rule(world.get_location("400M Strawberry"), Has("Springs") & Has("Crumbling Blocks"))

    #500M-900M
    world.set_rule(world.get_location("500M Strawberry"), Has("Keys"))
    world.set_rule(world.get_location("700M"), Has("Balloons"))
    world.set_rule(world.get_location("700M Strawberry"), Has("Balloons") & Has("White Clouds"))
    world.set_rule(world.get_location("800M"), Has("Balloons") & Has("White Clouds"))
    world.set_rule(world.get_location("900M"), Has("Balloons") & Has("White Clouds") & Has("Springs") & Has("Crumbling Blocks"))
    world.set_rule(world.get_location("900M Strawberry"), Has("Balloons") & Has("White Clouds") & Has("Springs") & Has("Crumbling Blocks") & Has("Breakable Blocks"))
    #1000M-1100M
    world.set_rule(world.get_location("1100M"), Has("Crumbling Blocks"))
    #1200M-1400M
    world.set_rule(world.get_location("1300M Strawberry"), Has("Keys"))
    world.set_rule(world.get_location("1400M"), Has("Balloons"))
    world.set_rule(world.get_location("1400M Strawberry"), Has("Balloons") & Has("Springs") & Has("Crumbling Blocks"))
    world.set_rule(world.get_location("1500M Strawberry"), Has("Keys") & Has("Balloons") & Has("Springs") & Has("Crumbling Blocks"))
    world.set_rule(world.get_location("1600M"), Has("Springs") & Has("Crumbling Blocks"))
    world.set_rule(world.get_location("1700M"), Has("Springs") & Has("Crumbling Blocks") & Has("Balloons"))
    world.set_rule(world.get_location("1700M Strawberry"), Has("Springs") & Has("Crumbling Blocks") & Has("Balloons") & Has("Breakable Blocks"))
    world.set_rule(world.get_location("1800M"), Has("Springs") & Has("Crumbling Blocks") & Has("Balloons"))
    world.set_rule(world.get_location("1900M"), Has("Springs") & Has("Crumbling Blocks") & Has("Balloons") & Has("White Clouds"))
    world.set_rule(world.get_location("1900M Strawberry"), Has("Springs") & Has("Crumbling Blocks") & Has("Balloons") & Has("White Clouds") & Has("Keys"))
    #2000M-2100M
    world.set_rule(world.get_location("2100M"), Has("Crumbling Blocks") & Has("Balloons"))
    #2200M-2500M
    world.set_rule(world.get_location("2300M"), Has("Double Dash"))
    world.set_rule(world.get_location("2300M Strawberry"), Has("Double Dash"))
    world.set_rule(world.get_location("2400M"), Has("Double Dash"))
    #2500M-3000M
    world.set_rule(world.get_location("2500M Strawberry"), Has("Double Dash") & Has("Keys"))
    world.set_rule(world.get_location("2600M"), Has("Double Dash") & Has("Crumbling Blocks") & Has("Springs"))
    world.set_rule(world.get_location("2600M Strawberry"), Has("Double Dash") & Has("Crumbling Blocks") & Has("Springs") & Has("Keys"))
    world.set_rule(world.get_location("2700M"), Has("Double Dash") & Has("Crumbling Blocks") & Has("Springs"))
    world.set_rule(world.get_location("2800M"), Has("Double Dash") & Has("Crumbling Blocks") & Has("Springs") & Has("Balloons"))
    world.set_rule(world.get_location("2800M Strawberry"), Has("Double Dash") & Has("Crumbling Blocks") & Has("Springs") & Has("Balloons") & Has("Keys"))
    world.set_rule(world.get_location("2900M"), Has("Double Dash") & Has("Crumbling Blocks") & Has("Springs") & Has("Balloons"))
    world.set_rule(world.get_location("2900M Strawberry"), Has("Double Dash") & Has("Crumbling Blocks") & Has("Springs") & Has("Balloons"))
    world.set_rule(world.get_location("2900M"), Has("Double Dash") & Has("Crumbling Blocks") & Has("Springs") & Has("Balloons"))
    world.set_rule(world.get_location("3000M"), Has("Double Dash") & Has("Crumbling Blocks") & Has("Springs") & Has("Balloons"))
    world.set_rule(world.get_location("3000M Strawberry"), Has("Double Dash") & Has("Crumbling Blocks") & Has("Springs") & Has("Balloons") & Has("Keys"))
    world.set_rule(world.get_location("Summit"), Has("Strawberry", count=world.options.strawberries_required.value))


def set_completion_condition(world: CelesteClassicWorld) -> None:
    world.set_completion_rule(Has("Victory"))