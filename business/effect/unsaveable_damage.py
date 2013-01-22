from business.effect import Effect

class UnsaveableDamageEffect(Effect):

    @property
    def name(self):
        return 'Damage on which only magic save count : %s' % self.amount

    @property
    def key(self):
        return 'usd'

        
