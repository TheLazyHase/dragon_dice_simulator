import json

from business.dice import face as faceDefinition
from business.dice.dice import Dice

class DiceTemplate(object):
    def __init__(self, name, description, dice_type, race, autosave=0, automelee=0, automissile=0, automaneuver=0, automagic=0):
        self.name = name
        self.description = description
        self.type = dice_type
        self.race = race

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
    def title(self):
        title = ("%s %s (#" % (self.race.name, self.name))+"%s"+(", %s" % self.type.name)
        if (len(self.elements) > 0):
            title += ", %s)" % '/'.join([element.name for element in self.elements])
        else:
            title += ")"
        return title

    @property
    def face_description(self):
        description_list = []
        for face in self.faces:
            description_list.append('<img src="http://www.sfr-inc.com/'+face.picture+'" /> '+face.name)
        return "<br />"+"<br />".join(description_list)
