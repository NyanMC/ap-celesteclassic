from dataclasses import dataclass

from Options import Choice, DeathLink, OptionGroup, PerGameCommonOptions, Range, Toggle

class DeathLinkAmnesty(Range):
    """
    How many deaths it takes to send a DeathLink
    """
    display_name = "Death Link Amnesty"
    range_start = 1
    range_end = 30
    default = 10

class StrawberriesRequired(Range):
    """
    How many Strawberries you must receive to finish. There are 18 in total.
    """
    display_name = "Strawberries Required"
    range_start = 0
    range_end = 18
    default = 12

@dataclass
class CelesteClassicOptions(PerGameCommonOptions):
    death_link: DeathLink
    death_link_amnesty: DeathLinkAmnesty
    strawberries_required: StrawberriesRequired