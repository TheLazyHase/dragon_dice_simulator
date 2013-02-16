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

from business.dice.face import SpecialOnMelee

class Stun(SpecialOnMelee):
    @property
    def name(self):
        return '%s Stun' % self.amount

    #Stun are rerolled on melee or melee avoidance rolls
    @property
    def is_rerolled(self):
        value = False
        if (self.type_roll.is_active_melee):
            value = True
        return value

    def get_special(self):
        print 'NYI'
