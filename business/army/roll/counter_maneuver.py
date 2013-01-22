from business.army.roll import Roll
from business.dice.face import Face

class CounterManeuverRoll(Roll):
    @property   
    def is_maneuver(self):
        return True

    @property   
    def is_counter(self):
        return True

    @property   
    def main_icon(self):
        return Face.ICON_MANEUVER
