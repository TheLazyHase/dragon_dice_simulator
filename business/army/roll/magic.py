from business.army.roll import Roll
from business.dice.face import Face

class MagicRoll(Roll):
    @property   
    def is_magic(self):
        return True

    @property   
    def main_icon(self):
        return Face.ICON_MAGIC
