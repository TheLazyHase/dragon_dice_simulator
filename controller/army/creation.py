# -*- coding: utf-8 *-*
" Copyright (c) 2013 Tisserant Pierre
"
" This file is part of Dragon dice simulator.
"
"    Foobar is free software: you can redistribute it and/or modify
"    it under the terms of the GNU Lesser General Public License as published by
"    the Free Software Foundation, either version 3 of the License, or
"    (at your option) any later version.
"
"    Foobar is distributed in the hope that it will be useful,
"    but WITHOUT ANY WARRANTY; without even the implied warranty of
"    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
"    GNU Lesser General Public License for more details.
"
"    You should have received a copy of the GNU Lesser General Public License
"    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

from pyramid.view import view_config
from controller import BaseController

from business.army.army import Army
from business.army.position import ArmyPosition
from business.dice.dice import Dice
from business.dice.dice_template import DiceTemplate
from business.race import Race

from models import DBSession

import re

class ArmiesController(BaseController):
    @view_config(route_name='army_selection', renderer='controller.army:templates/selection.mako')
    def army_selection(self):
        army_list = Army.get_all()
        if (len(army_list) > 0):
            return_value = {'existing': True, 'choices': [{'id': army.id, 'name': army.name} for army in Army.get_all()]}
        else:
            return_value = {'existing': False}
        return return_value

    @view_config(route_name='army_creation', renderer='controller.army:templates/edition.mako')
    def do_army_creation(self):
        army_position = ArmyPosition.get_by_id(1)
        army = Army(army_position)
        army.name = self.request.POST['army_name']
        army.save()
        return self.army_edition(army, ('Army named %s succesfully created !' % army.name))

    @view_config(route_name='army_edition', renderer='controller.army:templates/edition.mako')
    @view_config(route_name='army_edition_alias', renderer='controller.army:templates/edition.mako')
    def army_edition(self, army=None, special_message=''):
        if (army == None):
            import pprint
            army_id = self.request.matchdict.get('id', 0)
            if army_id == 0:
                army_id = self.request.GET['chosen_army']
            army = Army.get_by_id(army_id)
        from pprint import pprint
        
        dice_list = [{'id': dice.id, 'name': dice.name, 'picture': dice.template.picture} for dice in army.components]
        template_list = [{'id': dice_template.id, 'name': dice_template.name, 'picture': dice_template.picture} for dice_template in DiceTemplate.get_all()]
        return {'special_message': special_message, 'templates': template_list, 'dices': dice_list, 'army_id': army.id}

    @view_config(route_name='do_army_edition', renderer='controller.army:templates/edition.mako')
    def do_army_edition(self, army=None, special_message=''):
        army = Army.get_by_id(self.request.matchdict.get('id'))

        from pprint import pprint
        pprint(self.request.POST)
        pprint('=======================================')
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
