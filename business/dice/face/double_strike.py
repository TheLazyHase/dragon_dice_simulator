from business.dice.face import Melee
from business.dice.face import Face

class DoubleStrike(Melee):
    @property   
    def type(self):
        return Face.TYPE_SAI

    @property
    def name(self):
        return '%s Double Strike' % self.amount

    @property
    def is_rerolled(self):
        value = False
        if (self.type_roll.is_melee):
            value = True
        return value
