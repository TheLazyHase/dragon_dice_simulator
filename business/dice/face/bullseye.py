from business.dice.face import Face
from business.effect import TargetedDamageEffect

class Bullseye(Face):
    @property   
    def type(self):
        return Face.TYPE_SAI

    @property
    def name(self):
        return '%s Bullseye' % self.amount

    def icon_by_type(self, icon_type):
        value = 0
        if (icon_type == Face.ICON_MISSILE):
            if (self.type_roll.is_dragon):
                value = self.amount
            elif (self.type_roll.is_missile):
                if (self.type_roll.is_avoidance):
                    #On avoidance, regular melee icon are generated
                    value = self.amount
                else:
                    value = 0 #But the Bull's eye special effect will be put on the stack
        return value

    @property
    def special_effect(self):
        value = None
        if (self.type_roll.is_missile and not self.type_roll.is_avoidance):
            value = TargetedDamageEffect(self.amount)
        return value
