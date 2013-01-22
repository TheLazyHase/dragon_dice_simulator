from business.dice.face import Face
from business.effect import InflictHalvedResultEffect

class FrostBreath(Face):
    @property   
    def type(self):
        return Face.TYPE_SAI

    @property
    def name(self):
        return 'Frost Breath'

    def icon_by_type(self, icon_type):
        return 0

    @property
    def special_effect(self):
        value = None
        if (self.type_roll.is_melee or self.type_roll.is_missile):
            value = InflictHalvedResultEffect(1, division_type='frostbreath')
        return value
