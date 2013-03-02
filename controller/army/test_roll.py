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
from business.army.roll import *

class DragonRollController(BaseController):
    def roll(self, army, roll):
        army.roll(roll)

        results = []
        for dice in army.components:
            list_icon = []
            list_desc = []
            for face in dice.active_faces:
                list_icon.append(face.picture)
                list_desc.append(face.name)
            results.append((dice.name, list_icon, list_desc))
        return (results, [(effect.name, effect.description) for effect in army.instant_effect], [(effect.name, effect.description) for effect in army.special_effect])

    @view_config(route_name='dragon_roll', renderer='controller.army:templates/roll.mako')
    def dragon_roll(self):
        army = Army.get_by_id(self.request.matchdict.get('id'))

        results, instants, specials = self.roll(army, DragonRoll())

        return {'army_id': army.id, 'results': results, 'instants': instants, 'specials': specials, 'sums': [('melee',army.get_melee_result()), ('missile',army.get_missile_result()), ('save', army.get_save_result())]}

    @view_config(route_name='melee_roll', renderer='controller.army:templates/roll.mako')
    def melee_roll(self):
        army = Army.get_by_id(self.request.matchdict.get('id'))

        results, instants, specials = self.roll(army, MeleeRoll())

        return {'army_id': army.id, 'results': results, 'instants': instants, 'specials': specials, 'sums': [('melee',army.get_melee_result())]}

    @view_config(route_name='missile_roll', renderer='controller.army:templates/roll.mako')
    def missile_roll(self):
        army = Army.get_by_id(self.request.matchdict.get('id'))

        results, instants, specials = self.roll(army, MissileRoll())

        return {'army_id': army.id, 'results': results, 'instants': instants, 'specials': specials, 'sums': [('missile',army.get_missile_result())]}

    @view_config(route_name='maneuver_roll', renderer='controller.army:templates/roll.mako')
    def maneuver_roll(self):
        army = Army.get_by_id(self.request.matchdict.get('id'))

        results, instants, specials = self.roll(army, ManeuverRoll())

        return {'army_id': army.id, 'results': results, 'instants': instants, 'specials': specials, 'sums': [('maneuver',army.get_maneuver_result())]}

    @view_config(route_name='save_melee_roll', renderer='controller.army:templates/roll.mako')
    def save_melee_edition(self):
        army = Army.get_by_id(self.request.matchdict.get('id'))

        results, instants, specials = self.roll(army, SaveMeleeRoll())

        return {'army_id': army.id, 'results': results, 'instants': instants, 'specials': specials, 'sums': [('save',army.get_save_result())]}

    @view_config(route_name='save_missile_roll', renderer='controller.army:templates/roll.mako')
    def save_missile_edition(self):
        army = Army.get_by_id(self.request.matchdict.get('id'))

        results, instants, specials = self.roll(army, SaveMissileRoll())

        return {'army_id': army.id, 'results': results, 'instants': instants, 'specials': specials, 'sums': [('save',army.get_save_result())]}
