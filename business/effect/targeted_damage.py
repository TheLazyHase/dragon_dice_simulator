from business.effect import Effect

class TargetedDamageEffect(Effect):

    @property
    def name(self):
        return 'targeted damage : %s' % self.amount

    @property
    def key(self):
        return 'td'

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the targeted damage should be resolved and saved by the opposing player'
        self.expired = True

