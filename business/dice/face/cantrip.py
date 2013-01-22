from business.dice.face import Face
from business.effect import CantripEffect

class Cantrip(Face):
    @property   
    def type(self):
        return Face.TYPE_SAI

    @property
    def name(self):
        return '%s Cantrip' % self.amount

    icon = {
        Face.ICON_MELEE: 0,
        Face.ICON_MISSILE: 0,
        Face.ICON_MANEUVER: 0,
        Face.ICON_MAGIC: 1,
        Face.ICON_SAVE: 0,
    }

    @property
    def special_effect(self):
        value = None
        #Cantrip does not work on magic roll (well, it's regular magic then), and on maneuver roll (both avoidance and regular roll)
        if (not self.type_roll.is_magic and not self.type_roll.is_maneuver):
            value = CantripEffect(self.amount)
        return value
