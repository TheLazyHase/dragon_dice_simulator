from business.dice.face import Face
from business.effect import VersatileIconEffect

class ID(Face):
    @property   
    def type(self):
        return Face.TYPE_ID

    @property
    def name(self):
        return '%s ID' % self.amount

    def icon_by_type(self, icon_type):
        value = 0
        #If the roll is combined, then do not count the ID yet, but create a effect to signale the choice to the player
        #Else, consider the ID as being the thing needed for the roll
        #(and nothing else, which help for racial substitution calculs)
        if ((not self.type_roll.is_combined) and (self.type_roll.main_icon == icon_type)):
            value = self.amount
        return value

    @property
    def special_effect(self):
        value = None
        if (self.type_roll.is_combined):
            value = VersatileIconEffect(self.amount, option=self.type_roll.allowed_icon)
        return value
