from business.effect import Effect

class CantripEffect(Effect):

    @property
    def name(self):
        return 'Cantrip : %s' % self.amount

    @property
    def key(self):
        return 'ca'

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the cantrip effect should be resolved'
        self.expired = True
        
