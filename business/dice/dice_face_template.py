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

import json

from business.dice import face as faceDefinition
from business.dice.dice import Dice

class DiceFaceTemplate(object):
    def __init__(self, dice, side_number, class_name, amount, picture):
        self.dice = dice
        self.side_number = side_number
        self.class_name = class_name
        self.amount = amount
        self.picture = picture

    def get_instance(self):
        face_class = getattr(faceDefinition, self.class_name)
        face = face_class(self.amount)
        face.side_number = self.side_number
        face.picture = self.picture
        return face

    #A bit convoluted :x
    @property
    def name(self):
        face_class = getattr(faceDefinition, self.class_name)
        face = face_class(self.amount)
        return face.name
