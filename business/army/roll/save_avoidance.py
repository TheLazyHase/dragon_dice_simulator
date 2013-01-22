from business.army.roll import Roll
from business.dice.face import Face

class SaveAvoidanceRoll(Roll):
    @property   
    def is_save(self):
        return True

    @property   
    def is_avoidance(self):
        return True

    @property   
    def main_icon(self):
        return Face.ICON_SAVE
