# -*- coding: utf-8 *-*
" Copyright (c) 2013 Tisserant Pierre
"
" This file is part of Dragon dice simulator.
"
"    Foobar is free software: you can redistribute it and/or modify
"    it under the terms of the GNU Lesser General Public License as published by
"    the Free Software Foundation, either version 3 of the License, or
"    (at your option) any later version.
"
"    Foobar is distributed in the hope that it will be useful,
"    but WITHOUT ANY WARRANTY; without even the implied warranty of
"    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
"    GNU Lesser General Public License for more details.
"
"    You should have received a copy of the GNU Lesser General Public License
"    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

from business.dice.face import Face
from business.effect import VersatileIconEffect

class ID(Face):
    @property   
    def type(self):
        return Face.TYPE_ID

    @property
    def name(self):
        return '%s ID' % self.amount

    def icon_by_type(self, icon_type):
        value = 0
        #If the roll is combined, then do not count the ID yet, but create a effect to signale the choice to the player
        #Else, consider the ID as being the thing needed for the roll
        #(and nothing else, which help for racial substitution calculs)
        if ((not self.type_roll.is_combined) and (self.type_roll.main_icon == icon_type)):
            value = self.amount
        return value

    @property
    def special_effect(self):
        value = None
        if (self.type_roll.is_combined):
            value = VersatileIconEffect(self.amount, option=self.type_roll.allowed_icon)
        return value
