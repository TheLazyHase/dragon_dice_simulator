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

from business.dice.face import Face, SAI
from business.effect import DragonSummoningEffect

class SummonDragon(SAI, Face):
    @property
    def name(self):
        return 'Summon Dragon'

    def is_rerolled(self):
        value = False
        if self.type_roll.is_active_magic:
            value = True
        return value

    @property
    def on_special(self):
        value = None
        if self.type_roll.is_active_magic:
            value = DragonSummoningEffect(1, self.dice.elements)
        return value
