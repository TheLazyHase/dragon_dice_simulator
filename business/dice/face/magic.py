from business.dice.face import Face

class Magic(Face):
    @property
    def name(self):
        return '%s magic' % self.amount

    icon = {
        Face.ICON_MELEE: 0,
        Face.ICON_MISSILE: 0,
        Face.ICON_MANEUVER: 0,
        Face.ICON_MAGIC: 1,
        Face.ICON_SAVE: 0,
    }

