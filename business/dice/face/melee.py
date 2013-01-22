from business.dice.face import Face

class Melee(Face):
    @property
    def name(self):
        return '%s melees' % self.amount

    icon = {
        Face.ICON_MELEE: 1,
        Face.ICON_MISSILE: 0,
        Face.ICON_MANEUVER: 0,
        Face.ICON_MAGIC: 0,
        Face.ICON_SAVE: 0,
    }

