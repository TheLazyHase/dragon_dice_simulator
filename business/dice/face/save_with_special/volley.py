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

from business.dice.face import Face, SAI, Missile, Save
from business.effect import UnsaveableDamageEffect

class Volley(SAI, Missile, Save):
    @property
    def name(self):
        return '%s Volley' % self.amount

    def icon_by_type(self, icon_type):
        value = 0
        if (icon_type == Face.ICON_MISSILE):
            if (self.type_roll.is_missile):
                value = self.amount
        elif (icon_type == Face.ICON_SAVE):
            if (self.type_roll.is_save):
                value = self.amount
        return value

    @property
    def on_special(self):
        value = None
        if (self.type_roll.is_missile_save):
            value = UnsaveableDamageEffect(self.amount)
        return value

    icon = {
        Face.ICON_MELEE: 0,
        Face.ICON_MISSILE: 1,
        Face.ICON_MANEUVER: 0,
        Face.ICON_MAGIC: 0,
        Face.ICON_SAVE: 1,
    }
