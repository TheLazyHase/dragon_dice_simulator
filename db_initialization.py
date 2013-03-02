#SQLAlchemy stuff
from models import (
    DBSession,
    metadata
)

from sqlalchemy import create_engine
import settings
engine = create_engine('mysql+mysqldb://'+settings.db_user+':'+settings.db_password+'@'+settings.db_host+'/'+settings.db_name)
DBSession.configure(bind=engine)
metadata.bind = engine

import models

metadata.drop_all()
DBSession.flush()
metadata.create_all()

from business.game import Game

game = Game('The game you just lost')
DBSession.add(game)

from business.game.player import PlayerGame

player = PlayerGame('Me')
DBSession.add(player)

player.game = game

from business.army.army import Army

player.buried_army = Army('Buried stuff')
DBSession.add(player.buried_army)
player.dead_army = Army('Dead stuff')
DBSession.add(player.dead_army)
player.reserve_army = Army('Reserve stuff')
DBSession.add(player.reserve_army)
player.summon_army = Army('Summonable stuff')
DBSession.add(player.summon_army)

from business.element import Element

blue = Element('Blue', 'Air', 'a')
DBSession.add(blue)
red = Element('Red', 'Fire', 'f')
DBSession.add(red)
green = Element('Green', 'Water', 'w')
DBSession.add(green)
gold = Element('Gold', 'Earth', 'e')
DBSession.add(gold)
black = Element('Black', 'Death', 'd')
DBSession.add(black)
ivory = Element('Ivory', 'None', 'i')
DBSession.add(ivory)
#Well, white could be represented by having the 5 element, but having a white element mean it's easier to know everything is here
white = Element('White', 'All', 'al') 
DBSession.add(white)

DBSession.flush()

from business.dice.dice_type import DiceType

common = DiceType('common unit', 1, 1)
DBSession.add(common)
uncommon = DiceType('uncommon unit', 2, 2)
DBSession.add(uncommon)
rare = DiceType('rare unit', 3, 3)
DBSession.add(rare)
monster = DiceType('monster unit', 4, 4)
DBSession.add(monster)

common = DiceType('common item', 1, 1.0)
DBSession.add(common)
uncommon = DiceType('uncommon item', 2, 1.5)
DBSession.add(uncommon)
rare = DiceType('rare item', 3, 2.0)
DBSession.add(rare)
artifact = DiceType('artifact item', 4, 4)
DBSession.add(artifact)

medallion = DiceType('medallion item', 4, 4)
DBSession.add(medallion)

DBSession.flush()

from business.dice.dice_role import DiceRole

#regular troop
hm = DiceRole('Heavy Melee', 1)
DBSession.add(hm)
lm = DiceRole('Light Melee', 2)
DBSession.add(lm)
mi = DiceRole('Archer', 4)
DBSession.add(mi)
mh = DiceRole('Heavy Archer', 5)
DBSession.add(mh)
ca = DiceRole('Cavalry', 6)
DBSession.add(ca)
ma = DiceRole('Mage', 8)
DBSession.add(ma)
lm = DiceRole('Mage Warrior', 7)
DBSession.add(lm)
sb = DiceRole('Shield Bearer', 3)
DBSession.add(sb)

#4-health dice
monster = DiceRole('Monster', 9)
DBSession.add(monster)
ch = DiceRole('Champion', 10)
DBSession.add(ch)

#magic items
sh = DiceRole('Magic Shoes', 11)
DBSession.add(sh)
sw = DiceRole('Magic Sword', 12)
DBSession.add(sw)
ar = DiceRole('Magic Arrow', 13)
DBSession.add(ar)
jw = DiceRole('Magic Jewelry', 14)
DBSession.add(jw)
shield = DiceRole('Magic Shield', 15)
DBSession.add(shield)

art = DiceRole('Artifact', 16)
DBSession.add(art)
med = DiceRole('Medallion', 17)
DBSession.add(med)

DBSession.flush()

from business.race import Race

coral_elves = Race('Coral Elf', 'CoralElf', 'ce', 1, '00FFFF')
DBSession.add(coral_elves)
lava_elves = Race('Lava Elf', 'LavaElf', 'le', 2, '7F0000')
DBSession.add(lava_elves)
dwarves = Race('Dwarf', 'Dwarf', 'dw', 3, 'FF4000')
DBSession.add(dwarves)
goblins = Race('Goblin', 'Goblin', 'go', 4, '404000')
DBSession.add(goblins)

amazon = Race('Amazon', 'Amazon', 'am', 5, 'DDDDDD')
DBSession.add(amazon)
firewalker = Race('Firewalker', 'FireWalker', 'fiw', 6, '7F007F')
DBSession.add(firewalker)
undead = Race('Undead', 'Undead', 'ud', 7, '333333')
DBSession.add(undead)
feral = Race('Feral', 'Feral', 'fe', 8, '00AC00')
DBSession.add(feral)
swamp_stalker = Race('Swamp Stalker', 'SwampStalker', 'ss', 9, '004000')
DBSession.add(swamp_stalker)

frostwing = Race('Frost Wing', 'FrostWing', 'frw', 10, '000080')
DBSession.add(frostwing)
scalder = Race('Scalder', 'Scalder', 'sc', 11, '7F4000')
DBSession.add(scalder)
treefolk = Race('treefolk', 'Treefolk', 'tf', 12, '00FF00')
DBSession.add(treefolk)

eldarim = Race('Eldarim', 'Eldarim', 'el', 13, 'FFFFFF', break_by_color=True)
DBSession.add(eldarim)

dragonkin = Race('Dragonkin', 'DragonKin', 'dk', 14, '888888', break_by_color=True)
DBSession.add(dragonkin)
magic_item = Race('Magic Items', 'MagicItems', 'mi', 15, '666666', break_by_color=True)
DBSession.add(magic_item)
medallion = Race('Medallion', 'Medallion', 'me', 16, '666666')
DBSession.add(medallion)

from business.army.position import ArmyPosition

regular = ArmyPosition('Army')
DBSession.add(regular)
reserve = ArmyPosition('Reserve Area', is_reserve=True)
DBSession.add(reserve)
dua = ArmyPosition('Dead Unit Area', is_dead=True)
DBSession.add(dua)
bua = ArmyPosition('Buried Unit Area', is_buried=True)
DBSession.add(bua)

DBSession.flush()
