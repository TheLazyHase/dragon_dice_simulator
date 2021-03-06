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

class CantripEffect(Effect):

    @property
    def name(self):
        return '%s Cantrip' % self.amount

    @property
    def description(self):
        return 'Cantrip : %s' % self.amount

    @property
    def key(self):
        return 'cantrip'

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the cantrip effect should be resolved'
        self.expired = True
        
