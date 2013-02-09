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

from business.dice.face import Face, Magic, SAI

class MagicSpecialEffect(SAI, Magic):

    def icon_by_type(self, icon_type):
        value = 0
        if (icon_type == Face.ICON_MAGIC):
            if (self.type_roll.is_magic):
                if (self.type_roll.is_avoidance):
                    #On avoidance, regular melee icon are generated
                    value = self.amount
                else:
                    value = 0 #But the special effect will be put on the stack
        return value

    @property
    def special_effect(self):
        value = None
        if (self.type_roll.is_magic and self.type_roll.is_action):
            value = self.get_special()
        return value
