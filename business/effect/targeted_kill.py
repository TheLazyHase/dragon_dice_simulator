from business.effect import Effect

class TargetedKillEffect(Effect):

    @property
    def name(self):
        return '%s targeted ennemy units must roll ID or die' % self.amount

    @property
    def key(self):
        return 'tk'

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the targeted death effect should be resolved and saved against'
        self.expired = True
