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

from business.dice.face import SAI, Melee, Face
from business.effect import FlurryRerollEffect

class Flurry(SAI, Melee):
    @property
    def name(self):
        return '%s Flurry' % self.amount

    def icon_by_type(self, icon_type):
        value = 0
        if (icon_type == Face.ICON_MELEE):
            if (self.type_roll.is_melee):
                value = self.amount
        elif (icon_type == Face.ICON_SAVE):
            if (self.type_roll.is_melee_save):
                value = self.amount
        return value

    @property
    def is_rerolled(self):
        value = False
        if self.type_roll.is_melee and (not self.type_roll.is_dragon):
            value = True
        return value

    @property
    def on_instant(self):
        value = None
        if self.type_roll.is_dragon:
            value = FlurryRerollEffect(self.amount, self.dice)
        return value
