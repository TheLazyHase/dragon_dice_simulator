from business.army.roll import Roll
from business.dice.face import Face

class ManeuverAvoidanceRoll(Roll):
    @property   
    def is_maneuver(self):
        return True

    @property   
    def is_avoidance(self):
        return True

    @property   
    def main_icon(self):
        return Face.ICON_MANEUVER
