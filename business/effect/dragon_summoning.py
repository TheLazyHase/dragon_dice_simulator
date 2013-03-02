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

class DragonSummoningEffect(Effect):

    def __init__(self, amount, color):
        self.amount = amount
        self.expired = False
        self.color = color

    @property
    def name(self):
        return '%s %s Summon Dragon' % (self.amount, '/'.join([element.name for element in unit.elements]))

    @property
    def description(self):
        return 'Summon %s non-white dragon(s) of color %s to any terrain ' % (self.amount, ' or '.join([element.name for element in unit.elements]))

    @property
    def key(self):
        return 'dragon_summoning'

    def stack(self, effect):
        stackable = False
        if (effect.key == self.key):
            #If
            if (effect.type == self.type):
                stackable = True
        else:
            raise RuntimeError('Trying to stack two different effect')
        return stackable

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the frost breath effect should be put on the opposing army'
        self.expired = True

