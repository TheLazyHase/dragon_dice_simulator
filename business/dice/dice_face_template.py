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

import json

from business.dice import face as faceDefinition
from business.dice.dice import Dice

from sqlalchemy.orm import reconstructor

class DiceFaceTemplate(object):
    def __init__(self, dice, side_number, class_name, amount, picture):
        self.dice = dice
        self.side_number = side_number
        self.class_name = class_name
        self.amount = amount
        self.picture = picture
        self.hydrate()

    @reconstructor
    def hydrate(self):
        face_class = getattr(faceDefinition, self.class_name)
        self.face = face_class(self.amount)

    @property
    def name(self):
        return self.face.name
