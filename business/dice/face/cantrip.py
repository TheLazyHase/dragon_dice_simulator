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

from business.dice.face import Magic, SAI
from business.effect import CantripEffect

class Cantrip(SAI, Magic):
    @property
    def name(self):
        return '%s Cantrip' % self.amount

    @property
    def special_effect(self):
        value = None
        #Cantrip does not work on magic roll (well, it's regular magic then), and on maneuver roll (both avoidance and regular roll)
        if (not self.type_roll.is_magic and not self.type_roll.is_maneuver):
            value = CantripEffect(self.amount)
        return value
