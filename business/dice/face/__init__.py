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

#Base class
class Face(object):
    #Constant for face types
    TYPE_NORMAL = 1
    TYPE_ID = 2
    TYPE_SAI = 3

    ICON_MELEE = 1
    ICON_MISSILE = 2
    ICON_MANEUVER = 3
    ICON_MAGIC = 4
    ICON_SAVE = 5

    ICON_NAME = {
        ICON_MELEE: 'Melee',
        ICON_MISSILE: 'Missile',
        ICON_MANEUVER: 'Maneuver',
        ICON_MAGIC: 'Magic',
        ICON_SAVE: 'Save',
    }

    #nb. of icon on the empty face
    icon = {
        ICON_MELEE: 0,
        ICON_MISSILE: 0,
        ICON_MANEUVER: 0,
        ICON_MAGIC: 0,
        ICON_SAVE: 0,
    }

    def __init__(self, amount):
        self.amount = amount

    @property   
    def type(self):
        return Face.TYPE_NORMAL

    @property
    def name(self):
        return 'nothing'

    def icon_by_type(self, icon_type):
        return self.amount * self.icon[icon_type]

    @property
    def melee(self):
        return self.icon_by_type(Face.ICON_MELEE)

    @property
    def missile(self):
        return self.icon_by_type(Face.ICON_MISSILE)

    @property
    def maneuver(self):
        return self.icon_by_type(Face.ICON_MANEUVER)

    @property
    def magic(self):
        return self.icon_by_type(Face.ICON_MAGIC)

    @property
    def save(self):
        return self.icon_by_type(Face.ICON_SAVE)

    @property
    def special_effect(self):
        return None
    @property
    def is_rerolled(self):
        return False

#Regular
from business.dice.face.save import Save
from business.dice.face.melee import Melee
from business.dice.face.missile import Missile
from business.dice.face.maneuver import Maneuver
from business.dice.face.magic import Magic

from business.dice.face.id import ID
from business.dice.face.group_id import GroupID

#SAI
from business.dice.face.bullseye import Bullseye
from business.dice.face.cantrip import Cantrip
from business.dice.face.double_strike import DoubleStrike
from business.dice.face.frost_breath import FrostBreath
from business.dice.face.fly import Fly
from business.dice.face.howl import Howl
from business.dice.face.rend import Rend
from business.dice.face.smite import Smite
from business.dice.face.surprise import Surprise
from business.dice.face.swallow import Swallow
from business.dice.face.volley import Volley
