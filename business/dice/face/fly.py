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

class Fly(Face):
    allowed_icon = [Face.ICON_MANEUVER, Face.ICON_SAVE]
    #If a combined roll that use both maneuver and save for the same effect is rolled, fly is considered save
    #It's not a meaningful decision anyway
    main_icon = Face.ICON_SAVE

    @property   
    def type(self):
        return Face.TYPE_SAI

    @property
    def name(self):
        return '%s fly' % self.amount

    def icon_by_type(self, icon_type):
        value = 0

        #What is the intersection between fly icon and required icon ?
        type_intersection = list(set(Fly.allowed_icon) & set(self.type_roll.allowed_icon))

        if (self.type_roll.is_combined):
        #Combined roll that allow for save, maneuver, or both
            #Combined roll that allow for either save or maneuver but not both
            if len(type_intersection) == 1:
                if (icon_type in type_intersection):
                    value = self.amount
                else:
                    value = 0
            #Combined roll that allow for both save and maneuver
            elif len(list(type_intersection)) > 1:
                #Must be chosen (by effect)
                value = 0
            #Combined roll that allow for neither save nor maneuver
            else:
                #Normally we should not need to know what Fly is, but in case of racial swap, it's both :
                # @warning : it will break if you somehow convert both save and maneuver to something else on the same dice
                if (icon_type in Fly.allowed_icon):
                    value = self.amount
                else:
                    value = 0
        #If the roll is not combined, we do not need human input
        elif(self.type_roll.is_mixed):
            #No useful contribution ; count as both in case of substitution
            if len(type_intersection) == 0:
                if (icon_type in Fly.allowed_face):
                    value = self.amount
                else:
                    value = 0
            #Count as exactly one of the needed icon
            elif len(type_intersection) == 1:
                if (icon_type in type_intersection):
                    value = self.amount
                else:
                    value = 0
            #Count as at least two of the needed icon ; considered as Fly.main_icon and nothing else
            else:
                if (icon_type == Fly.main_icon):
                    value = self.amount
                else:
                    value = 0
        else:
            #If the roll is about save or maneuver, then fly is of the adaptated type
            if (self.type_roll.main_icon == Face.ICON_SAVE or self.type_roll.main_icon == Face.ICON_MANEUVER):
                if (icon_type == self.type_roll.main_icon):
                    value = self.amount
                else:
                    #Since it's the main roll type, it's not anything else
                    value = 0
            #Else, normally we should not need to know what Fly is, but in case of racial swap, it's both :
            # @warning : it will break if you somehow convert both save and maneuver to something else on the same dice
            else:
                if (icon_type in Fly.allowed_icon):
                    value = self.amount
                else:
                    value = 0

        return value

    @property
    def special_effect(self):
        value = None
        
        #Calculate how many icon from fly are needed on this roll
        #If more than one, a versatile effect have to be created
        type_intersection = list(set(Fly.allowed_icon) & set(self.type_roll.allowed_icon))
        if (self.type_roll.is_combined and len(type_intersection) > 1):
            value = VersatileIconEffect(self.amount, option=type_intersection)
        return value
