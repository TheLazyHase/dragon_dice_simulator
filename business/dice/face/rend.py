from business.dice.face import Face

class Rend(Face):
    @property   
    def type(self):
        return Face.TYPE_SAI

    @property
    def name(self):
        return '%s Rend' % self.amount

    def icon_by_type(self, icon_type):
        value = 0
        if (icon_type == Face.ICON_MELEE):
            if (self.type_roll.is_melee):
                value = self.amount
        elif (icon_type == Face.ICON_MANEUVER):
            if (self.type_roll.is_maneuver):
                value = self.amount
        return value

    #Rend are rerolled on melee or melee avoidance rolls
    @property
    def is_rerolled(self):
        value = False
        if (self.type_roll.is_melee):
            value = True
        return value
