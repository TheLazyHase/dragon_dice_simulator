from business.dice.face import Face

class Maneuver(Face):
    @property
    def name(self):
        return '%s maneuver' % self.amount

    icon = {
        Face.ICON_MELEE: 0,
        Face.ICON_MISSILE: 0,
        Face.ICON_MANEUVER: 1,
        Face.ICON_MAGIC: 0,
        Face.ICON_SAVE: 0,
    }

