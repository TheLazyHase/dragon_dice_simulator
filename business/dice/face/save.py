from business.dice.face import Face

class Save(Face):
    @property
    def name(self):
        return '%s save' % self.amount

    icon = {
        Face.ICON_MELEE: 0,
        Face.ICON_MISSILE: 0,
        Face.ICON_MANEUVER: 0,
        Face.ICON_MAGIC: 0,
        Face.ICON_SAVE: 1,
    }

