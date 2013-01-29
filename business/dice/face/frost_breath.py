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
from business.effect import InflictHalvedResultEffect

class FrostBreath(Face):
    @property   
    def type(self):
        return Face.TYPE_SAI

    @property
    def name(self):
        return 'Frost Breath'

    def icon_by_type(self, icon_type):
        return 0

    @property
    def special_effect(self):
        value = None
        if (self.type_roll.is_melee or self.type_roll.is_missile):
            value = InflictHalvedResultEffect(1, division_type='frostbreath')
        return value
