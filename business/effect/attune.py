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

class AttuneEffect(Effect):

    @property
    def name(self):
        return '%s Attune' % self.amount

    @property
    def description(self):
        return 'The magic object and %s dice produce magic of any color.' % self.amount

    @property
    def key(self):
        return 'attune'

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the attune effect should be resolved'
        self.expired = True
        
