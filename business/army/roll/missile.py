from business.army.roll import Roll
from business.dice.face import Face

class MissileRoll(Roll):
    @property   
    def is_missile(self):
        return True

    @property   
    def main_icon(self):
        return Face.ICON_MISSILE