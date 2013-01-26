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

from business.dice.dice_template import DiceTemplate
import json
dice_template = DiceTemplate('Remorhaz', 'fw', json.dumps([
            {'name': 'ID', 'amount': 4},
            {'name': 'Swallow', 'amount': 4},
            {'name': 'Swallow', 'amount': 4},
            {'name': 'Maneuver', 'amount': 4},
            {'name': 'Maneuver', 'amount': 4},
            {'name': 'Save', 'amount': 4},
            {'name': 'Save', 'amount': 4},
            {'name': 'Save', 'amount': 4},
            {'name': 'Melee', 'amount': 4},
            {'name': 'Melee', 'amount': 4}
        ]))

dice8 = dice_template.get_instance()
dice9 = dice_template.get_instance()
dice10 = dice_template.get_instance()

army1 = Army()
army1.add(dice1)
army1.add(dice2)
army1.add(dice3)
army1.add(dice4)

army2 = Army()
army1.add(dice5)
army1.add(dice6)
army1.add(dice7)

army1.add(dice8)
army1.add(dice9)
army1.add(dice10)

#march = March(army1, [army2])
#march.do_maneuver()

army1.roll(DragonRoll())

print(army1.result_description)
print(army1.effect_description)

army1.do_before_resolution_effect(army2)

print('%s melee obtained\r\n' % army1.melee)
print('%s missile obtained\r\n' % army1.missile)
print('%s save obtained\r\n' % army1.save)
