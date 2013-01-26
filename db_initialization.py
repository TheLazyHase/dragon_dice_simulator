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

from business.element import Element

blue = Element('blue', 'air')
DBSession.add(blue)
red = Element('red', 'fire')
DBSession.add(red)
green = Element('green', 'water')
DBSession.add(green)
gold = Element('gold', 'earth')
DBSession.add(gold)
black = Element('black', 'death')
DBSession.add(black)
ivory = Element('ivory', 'none')
DBSession.add(ivory)
#Well, white could be represented by having the 5 element, but having a white element mean it's easier to know everything is here
white = Element('white', 'all') 
DBSession.add(white)

DBSession.flush()

from business.dice.dice_type import DiceType

common = DiceType('common', 1, 1)
DBSession.add(common)
uncommon = DiceType('uncommon', 2, 2)
DBSession.add(uncommon)
rare = DiceType('rare', 3, 3)
DBSession.add(rare)
monster = DiceType('monster', 4, 4)
DBSession.add(monster)

DBSession.flush()

from business.race import Race

coral_elves = Race('Coral Elf', 'CoralElf', 'ce')
DBSession.add(coral_elves)
lava_elves = Race('Lava Elf', 'LavaElf', 'le')
DBSession.add(lava_elves)
dwarves = Race('Dwarf', 'Dwarf', 'dw')
DBSession.add(dwarves)
goblins = Race('Goblin', 'Goblin', 'go')
DBSession.add(goblins)

amazon = Race('Amazon', 'Amazon', 'am')
DBSession.add(amazon)
firewalker = Race('Firewalker', 'FireWalker', 'fw')
DBSession.add(firewalker)
undead = Race('Undead', 'Undead', 'ud')
DBSession.add(undead)
feral = Race('Feral', 'Feral', 'fe')
DBSession.add(feral)
swamp_stalker = Race('Swamp Stalker', 'SwampStalker', 'ss')
DBSession.add(swamp_stalker)

frostwing = Race('Frost Wing', 'FrostWing', 'fw')
DBSession.add(frostwing)
scalder = Race('Scalder', 'Scalder', 'sc')
DBSession.add(scalder)
treefolk = Race('treefolk', 'Treefolk', 'tf')
DBSession.add(treefolk)

dragonkin = Race('Dragonkin', 'DragonKin', 'dk')
DBSession.add(dragonkin)
eldarim = Race('Eldarim', 'Eldarim', 'el')
DBSession.add(eldarim)

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
