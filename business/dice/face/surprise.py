from business.dice.face import Face
from business.effect import InflictNoRetaliationEffect

class Surprise(Face):
    @property   
    def type(self):
        return Face.TYPE_SAI

    @property
    def name(self):
        return 'Surprise'

    def icon_by_type(self, icon_type):
        return 0

    @property
    def special_effect(self):
        value = None
        if (self.type_roll.is_melee and (not self.type_roll.is_avoidance)):
            value = InflictNoRetaliationEffect(1)
        return value
