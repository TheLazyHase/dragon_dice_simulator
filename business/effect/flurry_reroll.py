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

from business.effect import Effect

class FlurryRerollEffect(Effect):

    def __init__(self, amount, unit):
        self.amount = amount
        self.expired = False
        self.unit = unit

    @property
    def name(self):
        return '%s Flurry' % self.unit.name

    @property
    def description(self):
        return 'Can produce %s save, or %s melee and reroll the dice %s' %(self.amount, self.amount, self.unit.name)

    @property
    def key(self):
        return 'flurry_reroll'

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the choice between save and melee should be done'
        self.expired = True

    def stack(self, effect):
        return True

