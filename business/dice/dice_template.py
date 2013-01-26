import json

from business.dice import face as faceDefinition
from business.dice.dice import Dice

class DiceTemplate(object):
    def __init__(self, name, race, faces, autosave=0, automelee=0, automissile=0, automaneuver=0, automagic=0):
        self.name = name
        self.race = race
        self.json_faces = faces

        self.automelee = automelee
        self.automissile = automissile
        self.automaneuver = automaneuver
        self.automagic = automagic
        self.autosave = autosave

    def get_instance(self):
        face = []
        for face_template in self.face_list:
            face.append(face_template.get_instance())
        dice = Dice(self.name, self.race, face)
        dice.id = self.id
        return dice
