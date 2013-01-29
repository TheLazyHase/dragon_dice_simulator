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

from business.dice.face import Face
from business.effect import UnsaveableDamageEffect

class Volley(Face):
    @property   
    def type(self):
        return Face.TYPE_SAI

    @property
    def name(self):
        return '%s Volley' % self.amount

    def icon_by_type(self, icon_type):
        value = 0
        if (icon_type == Face.ICON_MISSILE):
            if (self.type_roll.is_missile or self.type_roll.is_dragon):
                value = self.amount
        elif (icon_type == Face.ICON_SAVE):
            if (self.type_roll.is_save or self.type_roll.is_dragon):
                value = self.amount
        return value

    @property
    def special_effect(self):
        value = None
        if (self.type_roll.is_save):
            value = UnsaveableDamageEffect(self.amount)
        return value
