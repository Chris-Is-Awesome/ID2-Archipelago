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

class PotionReq(Range):
    """If Potion Hunt is the required goal, how many potions are required"""
    display_name = "Potions Required"
    range_start = 1
    range_end = 50
    default = 12

class ExtraPotions(Range):
    """If Potion Hunt is the required goal, how many extra potions are placed in the pool"""
    display_name = "Extra Potions"
    range_start = 0
    range_end = 50
    default = 6

class RequiredDungeons(Range):
    """If Beat Dungeons is the required goal, how many dungeons must be beaten"""
    display_name = "Required Dungeon Count"
    range_start = 1
    range_end = 17
    default = 8

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

class MaxMeleeLevel(Range):
    """
    The highest level of melee you can obtain
    (1: Stick, 2: Fire Sword, 3: Fire Mace, 4: EFCS)
    0 is a stickless randomizer if you choose not to start with one
    EFCS is not recommended as it is not factored into logic.
    """
    display_name = "Max Melee Level"
    range_start = 0
    range_end = 4
    default = 3

class MaxForceLevel(Range):
    """
    The highest level of Force Wand you can obtain
    0 removes Force Wand from the pool
    Levels 2 and 3 do more damage
    4 is a dev item that does a ton of damage and shoots lightning
    """
    display_name = "Max Force Level"
    range_start = 0
    range_end = 4
    default = 3

class MaxDynamiteLevel(Range):
    """
    The highest level of Dynamite you can obtain
    0 removes Dynamite from the pool
    Levels 2 and 3 do more damage
    4 is a dev item that destroys puzzles, not recommended and is not in logic
    """
    display_name = "Max Dynamite Level"
    range_start = 0
    range_end = 4
    default = 3

class MaxIceLevel(Range):
    """
    The highest level of Ice Ring you can obtain
    0 removes Ice Ring from the pool
    Levels 2 and 3 do more damage
    4 is a dev item that does more damage and has a higher range
    """
    display_name = "Max Ice Ring Level"
    range_start = 0
    range_end = 4
    default = 3

class MaxChainLevel(Range):
    """
    The highest level of Chain you can obtain
    0: not in the pool
    1: Increases melee range by 50%
    2: Increases melee range by 100%
    3: Melee attacks also attack behind you
    """
    display_name = "Max Tracker Level"
    range_start = 0
    range_end = 3
    default = 3

class MaxTrackerLevel(Range):
    """
    The highest level of Tracker you can obtain
    0: not in the pool
    1: Reveals the location of all dungeon bosses
    2: Reveals the location of all chests and keys
    3: Reveals the layout of all dungeons
    """
    display_name = "Max Tracker Level"
    range_start = 0
    range_end = 3
    default = 3

class MaxAmuletLevel(Range):
    """
    The highest level of Amulet you can obtain
    0: not in the pool
    1: Reduces damage from melee attacks
    2: Reduces damage from projectiles
    3: Increases I-frames when rolling
    """
    display_name = "Max Amulet Level"
    range_start = 0
    range_end = 3
    default = 3

class MaxHeadbandLevel(Range):
    """
    The highest level of Headband you can obtain
    0: not in the pool
    1: Increases damage of projectiles
    2: Increases damage of melee attacks
    3: Attacks have a chance of instantly killing enemies
    """
    display_name = "Max Headband Level"
    range_start = 0
    range_end = 3
    default = 3

class MaxTomeLevel(Range):
    """
    The highest level of Tome you can obtain
    0: not in the pool
    1: 1/4 chance of resisting negative status
    2: 1/2 chance of resisting negative status
    3: 3/4 chance of resisting negative status
    """
    display_name = "Max Tracker Level"
    range_start = 0
    range_end = 3
    default = 3

class ExtraShardsInPool(Range):
    """
    Extra shards put into the pool
    The randomizer will always place the minimum required to open every secret dungeon, plus this amount
    """
    display_name = "Extra Shards In Pool"
    range_start = 0
    range_end = 24
    default = 12

class LockpicksInPool(Range):
    """
    Lockpicks to place in pool
    Lockpicks are not considered by logic
    Lockpicks are useless if Keysy is on
    """
    display_name = "Lockpicks in pool"
    range_start = 0
    range_end = 24
    default = 12

class CrayonsInPool(Range):
    """
    Amount of Crayons to add to the pool
    """
    display_name = "Crayons in pool"
    range_start = 0
    range_end = 40
    default = 20

class NegaCrayonsInPool(Range):
    """
    Amount of Nega-Crayons to add to the pool
    Nega-Crayons reduce max health by one
    Will not reduce health below one point
    """
    display_name = "Nega-Crayons in pool"
    range_start = 0
    range_end = 40
    default = 0

class S1Requirement(Range):
    """
    Shards required to open Sunken Labyrinth
    8: Default
    0: Open by default
    -1: Random between 1-36
    """
    display_name = "Sunken Labyrinth Shard Requirement"
    range_start = -1
    range_end = 36
    default = 8

class S2Requirement(Range):
    """
    Shards required to open Machine Fortress
    16: Default
    0: Open by default
    -1: Random between 1-36
    """
    display_name = "Machine Fortress Shard Requirement"
    range_start = -1
    range_end = 36
    default = 16

class S3Requirement(Range):
    """
    Shards required to open Dark Hypostyle
    24: Default
    0: Open by default
    -1: Random between 1-36
    """
    display_name = "Dark Hypostyle Shard Requirement"
    range_start = -1
    range_end = 36
    default = 24

class OpenS4(Toggle):
    """
    Tomb of Simulacrum is open without needing four Forbidden Keys
    Forbidden Keys are removed from the pool
    """

class OpenD8(Toggle):
    """
    Grand Library is open without needing seven raft pieces
    """
    display_name = "Open Grand Library"
    default = False

class OpenDW(Toggle):
    """
    Dream World is open without needing a raft piece
    """
    display_name = "Open Dream World"
    default = False

class EmptyChests(Toggle):
    """
    Junk chests can randomly be empty instead of having a junk item
    """
    display_name = "Enable Empty Chests"
    default = False

class BeeTraps(Toggle):
    """
    Junk chests can randomly be replaced with bee traps
    """
    display_name = "Enable Bee Traps"
    default = False

class MimicTraps(Toggle):
    """
    Junk chests can randomly be replaced with Hermit Leg chests (mimics)
    """
    display_name = "Enable Chest Mimics"
    default = False

class DeathLink(Choice):
    """
    If you or anyone else with Death Link dies, everyone with Death Link dies
    Off: Death Link is disabled for you
    On: Death Link is enabled for you
    Light: Death Link is enabled, dying from Death Link respawns you in the current room
    Hardcore: Death Link is enabled, dying respawns you at Fluffy Fields pond
    """
    display_name = "Death Link"
    option_off = 0
    option_on = 1
    option_light = 2
    option_hardcore = 3
    default = 0

class StartingMelee(Range):
    """
    Starting Melee level
    0: No stick
    1: Stick
    2: Fire Sword
    3: Fire Mace
    4: EFCS
    """
    display_name = "Starting Melee Level"
    range_start = 0
    range_end = 4
    default = 1

class StartingForce(Range):
    """Starting Force Wand level"""
    display_name = "Starting Force Wand"
    range_start = 0
    range_end = 4
    default = 0

class StartingDynamite(Range):
    """Starting Dynamite level"""
    display_name = "Starting Dynamite"
    range_start = 0
    range_end = 4
    default = 0

class StartingIce(Range):
    """Starting Ice Ring level"""
    display_name = "Starting Ice Ring"
    range_start = 0
    range_end = 4
    default = 0

class StartingChain(Range):
    """Starting Chain level"""
    display_name = "Starting Chain"
    range_start = 0
    range_end = 3
    default = 0

class StartingHeadband(Range):
    """Starting Headband level"""
    display_name = "Starting Headband"
    range_start = 0
    range_end = 3
    default = 0

class StartingTracker(Range):
    """Starting Tracker level"""
    display_name = "Starting Tracker"
    range_start = 0
    range_end = 3
    default = 0

class StartingAmulet(Range):
    """Starting Amulet level"""
    display_name = "Starting Amulet"
    range_start = 0
    range_end = 3
    default = 0

class StartingTome(Range):
    """Starting Tome level"""
    display_name = "Starting Tome"
    range_start = 0
    range_end = 3
    default = 0

class StartWithRoll(Toggle):
    """
    Start with the ability to roll
    If disabled, roll can be found in the pool
    """
    display_name = "Start With Roll"
    default = True

class RollOpensChests(Toggle):
    """If on, roll can be used to open chests"""
    display_name = "Rolling Opens Chests"
    default = False

class TricksInLogic(Toggle):
    """Ice Force jumps and difficult combat without rolling can be logically required"""
    display_name = "Allow Difficult Tricks in Logic"

class PhasingInLogic(Toggle):
    """Phasing (a glitch) can be logically required"""
    display_name = "Allow Phasing in Logic"
    default = False
 
id2_options: typing.Dict[str, type(Option)] = {
    **{
        option.__name__: option
        for option in (
            Goal, PotionReq, ExtraPotions, RequiredDungeons, RandomizeDungeonRewards, 
            RandomizeDungeonItems, RandomizeKeys, RandomizeCaveItems, RandomizePortalWorlds, 
            RandomizeCards, CardsAreHints, MaxMeleeLevel, MaxForceLevel, MaxDynamiteLevel, 
            MaxIceLevel, MaxChainLevel, MaxTrackerLevel, MaxAmuletLevel, MaxHeadbandLevel, 
            MaxTomeLevel, ExtraShardsInPool, LockpicksInPool, CrayonsInPool, NegaCrayonsInPool, 
            OpenD8, S1Requirement, S2Requirement, S3Requirement, OpenS4, OpenDW, EmptyChests,
            BeeTraps, MimicTraps, DeathLink, StartWithRoll, RollOpensChests, StartingMelee, 
            StartingForce, StartingDynamite, StartingIce, StartingChain, StartingTracker, 
            StartingAmulet, StartingHeadband, StartingTome, TricksInLogic, PhasingInLogic
        )
    }
}