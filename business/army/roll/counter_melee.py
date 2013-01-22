from business.army.roll import Roll
from business.dice.face import Face

class CounterMeleeRoll(Roll):
    @property   
    def is_melee(self):
        return True

    @property   
    def is_counter(self):
        return True

    @property   
    def main_icon(self):
        return Face.ICON_MELEE
