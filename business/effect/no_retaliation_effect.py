from business.effect import Effect

class InflictNoRetaliationEffect(Effect):
    @property
    def name(self):
        return 'Opposing army cannot counter-attack'

    @property
    def key(self):
        return 'itd'

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the surprise effect should be put on the opposing army'
        self.expired = True

    def stack(self, effect):
        return True

class NoRetaliationEffect(Effect):
    @property
    def name(self):
        return 'Cannot counter-attack'

    @property
    def key(self):
        return 'nr'

    def stack(self, effect):
        return True
