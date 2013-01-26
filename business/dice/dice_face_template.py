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
