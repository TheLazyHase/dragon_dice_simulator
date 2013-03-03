# -*- coding: utf-8 *-*
# Copyright (c) 2013 Tisserant Pierre
#
# This file is part of Dragon dice simulator.
#
#    Dragon dice simulator is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Dragon dice simulator is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Dragon dice simulator.  If not, see <http://www.gnu.org/licenses/>.

from pyramid.view import view_config
from controller import BaseController

from business.army.army import Army
from business.game.player import PlayerGame
from business.army.roll import *
from business.army.position import ArmyPosition
from business.dice.dice import Dice
from business.dice.dice_template import DiceTemplate
from business.race import Race
from business.element import Element

from models import DBSession

import re

class ArmiesController(BaseController):
    @view_config(route_name='army_edition',  permission='use', renderer='controller.army:templates/edition.mako')
    def army_edition(self, army=None, special_message=''):
        if (army == None):
            army_id = self.request.matchdict.get('id', 0)
            army = Army.get_by_id(army_id)
        
        dice_list = [{'id': dice.id, 'name': dice.name, 'picture': dice.template.picture} for dice in army.components]

        template_list = []
        for race in Race.get_all():
            if race.break_by_color:
                for color in Element.get_all():
                    sub_race = []
                    for dice in race.dices:
                        if color in dice.elements:
                            sub_race.append(dice)
                    if sub_race != []:
                        template_list.append((color.name+' '+race.name, color.element_short_name+' '+race.tag, race.color, [{'id': dice.id, 'name': dice.name, 'picture': dice.picture} for dice in sub_race]))
            else:
                template_list.append((race.name, race.tag, race.color, [{'id': dice_template.id, 'name': dice_template.name, 'picture': dice_template.picture} for dice_template in race.dices]))

        return {'special_message': special_message, 'races': template_list, 'dices': dice_list, 'army_id': army.id}

    @view_config(route_name='do_army_edition',  permission='use', renderer='controller.army:templates/edition.mako')
    def do_army_edition(self, army=None, special_message=''):
        army = Army.get_by_id(self.request.matchdict.get('id'))

        if 'unit_to_remove[]' in self.request.POST:
            for dice_id in self.request.POST.getall('unit_to_remove[]'):
                Dice.get_by_id(int(dice_id)).delete()
        #Ugly, but how to do otherwise ?
        regexp = re.compile('unit_amount_([1-9][0-9]{0,2})')
        for element, amount in self.request.POST.items():
            m = regexp.search(element)
            if ((m != None) and (int(amount) > 0)):
                for i in range(int(amount)):
                    dice = Dice(DiceTemplate.get_by_id(m.group(1)), army)
                    dice.save()

        return self.army_edition(army, ('army %s succesfully modified !' % army.name))

