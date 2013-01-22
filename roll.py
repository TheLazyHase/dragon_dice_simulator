from business.dice.dice import Dice
from business.dice.face import *
from business.army.army import Army
from business.army.roll import *
from business.march import March
from data import UnitFactory

dice1 = UnitFactory.create('Dispatcher')
dice2 = UnitFactory.create('Dispatcher')
dice3 = UnitFactory.create('Magi')
dice4 = UnitFactory.create('Defender')

dice5 = UnitFactory.create('Defender')
dice6 = UnitFactory.create('Wolf Master')
dice7 = UnitFactory.create('Wolf Master')

army1 = Army()
army1.add(dice1)
army1.add(dice2)
army1.add(dice3)
army1.add(dice4)

army2 = Army()
army1.add(dice5)
army1.add(dice6)
army1.add(dice7)

#march = March(army1, [army2])
#march.do_maneuver()

army1.roll(DragonRoll())

print(army1.result_description)
print(army1.effect_description)

army1.do_before_resolution_effect(army2)

print('%s melee obtained\r\n' % army1.melee)
print('%s missile obtained\r\n' % army1.missile)
print('%s save obtained\r\n' % army1.save)

army1.roll(TidalWaveRoll())

print(army1.result_description)
print(army1.effect_description)

army1.do_before_resolution_effect(army2)

print('%s maneuver obtained\r\n' % army1.maneuver)
print('%s save obtained\r\n' % army1.save)
