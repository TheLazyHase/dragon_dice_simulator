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

class DiceTemplate(object):
    def __init__(self, name, description, dice_type, race, role, autosave=0, automelee=0, automissile=0, automaneuver=0, automagic=0):
        self.name = name
        self.description = description
        self.type = dice_type
        self.race = race
        self.role = role

        self.automelee = automelee
        self.automissile = automissile
        self.automaneuver = automaneuver
        self.automagic = automagic
        self.autosave = autosave

        self.elements = []

    def get_instancied_faces(self):
        faces = []
        for face_template in self.faces:
            faces.append(face_template.get_instance())
        return faces        

    @property
    def role_name(self):
        return self.role.name

    @property
    def type_name(self):
        return self.type.name

    @property
    def title(self):
        title = ("%s %s, %s" % (self.race.name, self.name, self.type.name))
        if (len(self.elements) > 0):
            title += " (%s)" % '/'.join([element.name for element in self.elements])
        return title

    @property
    def picture(self):
        return self.faces[0].picture

    @property
    def face_description(self):
        description_list = []
        for face in self.faces:
            description_list.append('<img src="http://www.sfr-inc.com/'+face.picture+'" /> '+face.name)
        return "<br />"+"<br />".join(description_list)
