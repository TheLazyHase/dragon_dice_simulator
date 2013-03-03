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
from pyramid.httpexceptions import HTTPFound
from controller import BaseController

from business.army.army import Army
from business.dice.dice import Dice
from business.game.action.save import SaveAction

from business.army.roll import SaveMeleeRoll

from models import DBSession

class SaveActionController(BaseController):
    @view_config(route_name='initiate_save_action', permission='use')
    def initiate_save_action(self):
        army_id = self.request.POST['chosen_army']
        army = Army.get_by_id(army_id)
        from pprint import pprint
        pprint(army.current_action)
        if army.current_action != None:
            raise RuntimeError('There is already a current action')
        action = SaveAction(army.owner.game, army, self.request.POST['damage'])
        action.save(explicit=True)
        url = self.request.route_url('save_action', id=action.id)
        return HTTPFound(location=url)

    @view_config(route_name='save_action', permission='use', renderer='controller.action:templates/save/step_three.mako')
    def save_action(self):
        action = SaveAction.get_by_id(self.request.matchdict.get('id'))
        damage = action.damage
        army = action.army
        army.set_roll_type(SaveMeleeRoll())

        #Step 0 : nothing done. Let's roll the army.
        if action.step == 0:
            army.roll(SaveMeleeRoll())
            action.step = 1

        #Step 1 : check if some effect can be resolved. Else go to step 2.
        if action.step == 1:
            #For now, automatically assume that everything is fine
            action.step = 2

        #Step 2 : require that enough unit are taken as casualty
        if action.step == 2:
            saves = army.get_save_result()
            min_health = 4
            if damage < saves:
                remaining = 0
            else:
                remaining = damage - saves

            #We beed to know what is the smallest unit (in health) in the army
            for unit in army.components:
                if unit.health < min_health:
                    min_health = unit.health

            #if damage cannot kill any dice, it's discarded
            if remaining < min_health:
                action.step = 3
                casualty = []
            elif 'unit_to_kill[]' in self.request.POST:
                casualty = []
                sum_health = 0
                for dice_id in self.request.POST.getall('unit_to_kill[]'):
                    unit = Dice.get_by_id(int(dice_id))
                    if not(unit in army.components):
                        raise RuntimeError('Trying to kill an unit outside of the army !')
                    casualty.append(unit)
                    sum_health += unit.health

                if (sum_health <= remaining) and (min_health > (remaining - sum_health)):
                    #It's a valid casualty removal
                    action.step = 3
                    

        if action.step == 3:
            #Prepare the view before altering the result.
            results = []
            for dice in army.components:
                list_icon = []
                list_desc = []
                for face in dice.active_faces:
                    list_icon.append(face.picture)
                    list_desc.append(face.name)
                results.append((dice.name, list_icon, list_desc))
            dead_army = army.owner.dead_army

            #We remove the casualty now
            for unit in casualty:
                unit.army = dead_army

            dice_list = [(dice.name, dice.template.picture) for dice in army.components]
            dead_dice_list = [(dice.name, dice.template.picture) for dice in casualty]
            action.delete(explicit=True)
        else:
            action.save()

        #Now, dispatch to the good view
        if action.step == 1:
            #resolve SAI
            url = self.request.route_url('save_action_step_one', id=action.id)
            return_value = HTTPFound(location=url)
        elif action.step == 2:
            #remove casualties
            url = self.request.route_url('save_action_step_two', id=action.id)
            return_value = HTTPFound(location=url)
        else:
            #save finished
            #We do the view without redirection to avoid having to store silly thing.
            return_value = {'results': results, 'dices': dice_list, 'dead_dices': dead_dice_list, 'save': saves, 'damage': damage, 'remaining': remaining, 'route_next_step': self.request.route_url('army_selection')}
        return return_value

    @view_config(route_name='save_action_step_one', permission='use', renderer='controller.action:templates/save/step_one.mako')
    def step_one(self):
        action = SaveAction.get_by_id(self.request.matchdict.get('id'))
        #What are the result ?
        results = []
        for dice in army.components:
            list_icon = []
            list_desc = []
            for face in dice.active_faces:
                list_icon.append(face.picture)
                list_desc.append(face.name)
            results.append((dice.name, list_icon, list_desc))
        return {'results': results, 'route_next_step': self.request.route_url('save_action', id=action.id)}
    
    @view_config(route_name='save_action_step_two', permission='use', renderer='controller.action:templates/save/step_two.mako')
    def step_two(self):
        action = SaveAction.get_by_id(self.request.matchdict.get('id'))
        action.army.set_roll_type(SaveMeleeRoll())
        #What are the result ?
        results = []
        for dice in action.army.components:
            list_icon = []
            list_desc = []
            for face in dice.active_faces:
                list_icon.append(face.picture)
                list_desc.append(face.name)
            results.append((dice.name, list_icon, list_desc))
        #What is the army ?
        dice_list = [(dice.id, dice.name, dice.template.picture) for dice in action.army.components]
        if action.damage > action.army.get_save_result():
            remaining = action.damage - action.army.get_save_result()
        else:
            remaining = 0
        return {'results': results, 'dices': dice_list, 'save': action.army.get_save_result(), 'damage': action.damage, 'remaining': remaining, 'route_next_step': self.request.route_url('save_action', id=action.id)}

