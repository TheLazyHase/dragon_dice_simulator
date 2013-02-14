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

class PromotionSaveEffect(Effect):
    @property
    def name(self):
        return '%s icon to chose between save or promoting one unit' % self.amount

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here human have to choose between icon type'
        self.expired = True

    @property
    def key(self):
        return 'pro'

class PromotionEffect(Effect):
    @property
    def name(self):
        return 'Promote %s units' % self.amount

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here human promote unit'
        self.expired = True

    @property
    def key(self):
        return 'pro'
