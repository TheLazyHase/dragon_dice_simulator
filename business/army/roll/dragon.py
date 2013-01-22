from business.army.roll import Roll
from business.dice.face import Face

class DragonRoll(Roll):
    @property   
    def is_missile(self):
        return True

    @property   
    def is_melee(self):
        return True

    @property   
    def is_save(self):
        return True

    @property   
    def is_dragon(self):
        return True

    @property   
    def is_combined(self):
        return True

    @property   
    def allowed_icon(self):
        return [Face.ICON_MELEE, Face.ICON_MISSILE, Face.ICON_SAVE]
