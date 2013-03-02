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

class Brawl(Effect):

    def __init__(self, amount, unit):
        self.amount = amount
        self.expired = False
        self.unit = unit

    def stack(self, effect):
        if (effect.key != self.key):
            raise RuntimeError('Trying to stack two different effect')
        return False

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the brawl should be resolved'
        self.expired = True

class SaveableBrawl(Brawl):

    @property
    def name(self):
        return '%s\'s Coil' % self.unit.name

    @property
    def description(self):
        return 'Chosen unit suffer %s damages ; melee result on its save roll are inflicted to %s.' % (self.amount, self.unit.name)


    @property
    def key(self):
        return 'saveable_brawl'

class UnsaveableBrawl(Brawl):

    @property
    def name(self):
        return '%s\'s Hug' % self.unit.name

    @property
    def description(self):
        return 'Chosen unit suffer %s damages with no save roll ; it can roll to counter-attack %s.' % (self.amount, self.unit.name)


    @property
    def key(self):
        return 'unsaveable_brawl'
