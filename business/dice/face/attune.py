# -*- coding: utf-8 *-*
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

from business.dice.face.magic import Magic
from business.dice.face.sai import SAI
from business.effect import AttuneEffect

class Attune(SAI, Magic):
    @property
    def name(self):
        return '%s Attune' % self.amount

    @property
    def special_effect(self):
        value = None
        if self.type_roll.is_active_magic:
            value = AttuneEffect(1)
        return value
