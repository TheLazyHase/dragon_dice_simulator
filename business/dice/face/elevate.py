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

from business.dice.face import SAI, Face
from business.effect import ElevateSaveDoublingEffect, ElevateMissileDoublingEffect, ElevateSaveOrMissileDoublingEffect

class Elevate(SAI, Face):
    @property
    def name(self):
        return '%s Elevate' % self.amount

    def icon_by_type(self, icon_type):
        value = 0
        if (icon_type == Face.ICON_MANEUVER):
            if (self.type_roll.is_maneuver):
                value = self.amount
        return value

    @property
    def on_special(self):
        value = None
        if self.type_roll.is_dragon:
            value = ElevateSaveOrMissileDoublingEffect(1)
        elif self.type_roll.is_active_missile:
            value = ElevateMissileDoublingEffect(1)
        elif self.type_roll.is_melee_save:
            value = ElevateSaveDoublingEffect(1)
        return value
