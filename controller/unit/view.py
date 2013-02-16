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

from business.dice.dice_template import DiceTemplate
from business.race import Race

from models import DBSession

import re

class ArmiesController(BaseController):
    @view_config(route_name='unit_view', renderer='controller.unit:templates/view.mako')
    def unit_view(self):
        unit = DiceTemplate.get_by_id(self.request.matchdict.get('id', 0))
        if (len(unit.elements) > 0):
            info = '%s ' % '/'.join([element.name for element in unit.elements])
        else:
            info = ''
        if (unit.type.health < 4):
            #We reverse the type_name string, we remove the first element (it's alway "unit" or "items" and we neither need nor want it), and we reverse again
            info += '%s ' % unit.type_name[::-1].split(' ', 1)[1][::-1]


        info += '%s' % unit.role_name
        return {'name': unit.name, 'info': info, 'faces': [{'name': face.name, 'picture': face.picture} for face in unit.faces]}

