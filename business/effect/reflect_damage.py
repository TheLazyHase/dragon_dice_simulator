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

class ReflectDamageEffect(Effect):
    @property
    def name(self):
        return 'Chose %s opposing unit or dragons that produced normal melee damage. Generate this amount of save and inflict this amount of damage to the chosen unit or dragon ; units may be rolled to save against thoses damages' % self.amount

    @property
    def key(self):
        return 'itd'

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the reflect damage should be handled'
        self.expired = True

    def stack(self, effect):
        return True

