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

from business.dice.face import SaveSpecialEffect
from business.effect import PromotionEffect, PromotionSaveEffect

class WildGrowth(SaveSpecialEffect):
    @property
    def name(self):
        return '%s Wild Growth' % self.amount

    def get_special(self):
        value = None
        #@TODO : restrict back damage to missile saving throw
        if (not self.type_roll.is_active_maneuver):
            value = PromotionSaveEffect(self.amount)
        return value
