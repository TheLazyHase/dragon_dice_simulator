from business.army.roll import Roll
from business.dice.face import Face

class ManeuverRoll(Roll):
    @property   
    def is_maneuver(self):
        return True

    @property   
    def main_icon(self):
        return Face.ICON_MANEUVER
