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
from business.dice.face import Face

class VersatileIconEffect(Effect):

    @property
    def name(self):
        return 'Choose result'

    def __init__(self, amount, option=[]):
        self.amount = amount
        self.expired = False
        self.option = option

    @property
    def description(self):
        return '%s icon to choose between %s' % (self.amount, ', '.join(Face.ICON_NAME[face_type] for face_type in self.option))

    def stack(self, effect):
        stackable = False
        if (effect.key == self.key):
            if (self.option == effect.option):
                self.amount += effect.amount
                stackable = True
        else:
            raise RuntimeError('Trying to stack two different effect')
        return stackable

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here human have to choose between icon type'
        self.expired = True

    @property
    def key(self):
        return 'versatile_icon'
