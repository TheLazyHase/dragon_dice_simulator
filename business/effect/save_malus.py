from business.effect import Effect

class InflictSaveMalusEffect(Effect):

    @property
    def name(self):
        return 'Inflict a save malus of %s' % self.amount

    @property
    def key(self):
        return 'ism'

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the malus should be put on the opposing army'
        self.expired = True

class SaveMalusEffect(Effect):

    @property
    def name(self):
        return 'Save malus : %s' % self.amount

    @property
    def key(self):
        return 'sm'
