from business.effect import Effect

class InflictHalvedResultEffect(Effect):
    @property
    def name(self):
        return ('Opposing results are divided by %s because of %s until next turn' % (pow(2, self.amount), self.type))

    def __init__(self, amount, division_type='None'):
        self.amount = amount
        self.expired = False
        self.type = division_type

    @property
    def key(self):
        return 'itd'

    def stack(self, effect):
        stackable = False
        if (effect.key == self.key):
            #If
            if (effect.type == self.type):
                stackable = True
                #No amount change, because while the effect can be combined into one, it's still only divide by two
        else:
            raise RuntimeError('Trying to stack two different effect')
        return stackable

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the frost breath effect should be put on the opposing army'
        self.expired = True

class HalvedResultEffect(Effect):
    @property
    def name(self):
        return ('Results are divided by %s until next turn' % pow(2, self.amount))

    @property
    def key(self):
        return 'td'

    def stack(self, effect):
        if (effect.key == self.key):
            self.amount = self.amount + effect.amount
        else:
            raise RuntimeError('Trying to stack two different effect')
