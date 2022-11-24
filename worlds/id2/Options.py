import typing
from Options import Choice, Option, Toggle, Range

class Goal(Choice):
    """
    Upon completing this goal, your raft will be complete and you can finish your run.
    All Raft Pieces: Collect all 8 raft pieces
    Potion Hunt: Collect a configurable number of potions
    Beat Dungeons: Complete a configurable number of dungeons
    """
    display_name = "Ending Goal"
    option_allRaftPieces = 0
    option_potionHunt = 1
    option_beatDungeons = 2
    default = 0

class RandomizeDungeonRewards(Choice):
    """
    Randomize the locations of Raft Pieces, Forbidden Keys, Loot, and the three cards at the end of Dream Dungeons.
    Vanillla: Rewards are in their normal locations
    Shuffled: Dungeon rewards can only replace each other
    Anywhere: Dungeon rewards can be in any randomized check
    """
    display_name = "Randomize Dungeon Rewards"
    option_vanilla = 0
    option_shuffled = 1
    option_anywhere = 2
    default = 0

class RandomizeDungeonItems(Choice):
    """
    Put dungeon items into the pool (excluding keys)
    Vanilla: Major items are not randomized
    Equipment: Randomize the main dungeon item (dynamite, ice ring, etc.)
    Crayons: Randomize the locations of dungeon crayons
    Both: Add both the dungeon item and crayon to the pool
    """
    display_name = "Randomize Dungeon Items"
    option_vanilla = 0
    option_equipment = 1
    option_crayons = 2
    option_both = 3
    default = 1

class RandomizeKeys(Choice):
    """
    Put keys in the pool
    Vanilla: Keys are in their normal locations
    Dungeons: Keys are found in dungeons
    Anywhere: Keys can be found in any randomized check
    Keysy: Keys are removed from the pool and all locked doors are automatically unlocked
    """
    display_name = "Randomize Keys"
    option_vanilla = 0
    option_dungeons = 1
    option_anywhere = 2
    option_keysy = 3
    default = 0

class RandomizeCaveItems(Toggle):
    """
    Put the items directly found in caves into the pool
    """
    display_name = "Randomize Cave Items"
    default = False


class RandomizePortalWorlds(Choice):
    """
    Randomize the items found in Portal Worlds
    Vanilla: Items are not randomized
    Shuffled: Items are shuffled between portal worlds
    Anywhere: Items can be anywhere
    """
    display_name = "Randomize Portal World Items"
    option_vanlla = 0
    option_shuffled = 1
    option_anywhere = 2
    default = 0

class RandomizeCards(Toggle):
    """
    Put cards in the pool
    """
    display_name = "Randomize cards"
    default = False

class CardsAreHints(Toggle):
    """
    Cards provide hints telling you if locations are useful or not
    Recommended to use if randomizing cards
    """
    display_name = "Cards Give Hints"
    default = False

id2_options: typing.Dict[str, type(Option)] = {
    **{
        option.__name__: option
        for option in (
            Goal, RandomizeDungeonRewards, RandomizeDungeonItems, RandomizeKeys,
            RandomizeCaveItems, RandomizePortalWorlds, RandomizeCards, CardsAreHints
        )
    }
}