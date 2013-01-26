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

    def get_instance(self):
        face = []
        for face_template in self.faces:
            face.append(face_template.get_instance())
        dice = Dice(self.name, self.race, face, self.type.health, self.elements)
        dice.id = self.id
        return dice
