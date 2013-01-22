from business.dice.face import Face

class Missile(Face):
    @property
    def name(self):
        return '%s missile' % self.amount

    icon = {
        Face.ICON_MELEE: 0,
        Face.ICON_MISSILE: 1,
        Face.ICON_MANEUVER: 0,
        Face.ICON_MAGIC: 0,
        Face.ICON_SAVE: 0,
    }

