from business.dice.face import Face
from business.effect import UnsaveableDamageEffect

class Volley(Face):
    @property   
    def type(self):
        return Face.TYPE_SAI

    @property
    def name(self):
        return '%s Volley' % self.amount

    def icon_by_type(self, icon_type):
        value = 0
        if (icon_type == Face.ICON_MISSILE):
            if (self.type_roll.is_missile or self.type_roll.is_dragon):
                value = self.amount
        elif (icon_type == Face.ICON_SAVE):
            if (self.type_roll.is_save or self.type_roll.is_dragon):
                value = self.amount
        return value

    @property
    def special_effect(self):
        value = None
        if (self.type_roll.is_save):
            value = UnsaveableDamageEffect(self.amount)
        return value
