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
from business.game.player import PlayerGame
from business.army.position import ArmyPosition

from models import DBSession

class ArmiesController(BaseController):
    @view_config(route_name='army_selection', permission='use', renderer='controller.army:templates/selection.mako')
    def army_selection(self):
        player_game = PlayerGame.get_by_name('Me')
        army_list = player_game.armies
        if army_list != None and len(army_list) > 0:
            return_value = {'existing': True, 'choices': [{'id': army.id, 'name': army.name} for army in army_list]}
        else:
            return_value = {'existing': False}
        return return_value

    @view_config(route_name='army_creation')
    def do_army_creation(self):
        army_position = ArmyPosition.get_by_id(1)
        army = Army(army_position)
        army.name = self.request.POST['army_name']
        player_game = PlayerGame.get_by_name('Me')
        if player_game.armies == None:
            player_game.armies = [army]
        else:
            player_game.armies.append(army)
        army.save(explicit=True)
        url = self.request.route_url('army_edition', id=army.id)
        return HTTPFound(location=url)

    @view_config(route_name='do_army_selection', permission='use')
    def do_army_selection(self, army=None, special_message=''):
        army_id = self.request.POST['chosen_army']
        army = Army.get_by_id(army_id)
        if army.current_action != None:
            url = self.request.route_url('save_action', id=army.current_action.id)
        else:
            url = self.request.route_url('army_edition', id=army.id)
        return HTTPFound(location=url)

