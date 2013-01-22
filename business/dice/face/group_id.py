from business.dice.face.id import ID

class GroupID(ID):
    @property
    def name(self):
        return '%s Group ID' % self.amount

    @property
    def is_rerolled(self):
        return True
