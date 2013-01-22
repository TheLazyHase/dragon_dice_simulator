from business.effect import Effect

class UnpreventableDamageEffect(Effect):

    @property
    def name(self):
        return 'unpreventable damage : %s' % self.amount

    @property
    def key(self):
        return 'ud'
        
