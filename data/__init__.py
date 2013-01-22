from business.dice.dice import Dice
from business.dice import face as faceDefinition
from data import race

class UnitFactory(object):

    @classmethod
    def create(cls, unit_key):
        definition = race.definitions[unit_key]
        face = []
        for face_info in definition['faces']:
            face_class = getattr(faceDefinition, face_info['name'])
            face.append(face_class(face_info['amount']))
        dice = Dice(unit_key, definition['race'], face)
        race.sequence = race.sequence + 1
        dice.id = race.sequence
        return dice

