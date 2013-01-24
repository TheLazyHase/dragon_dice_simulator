from business.effect import Effect

class RacialMalusChoiceEffect(Effect):

    def __init__(self, amount, race=[]):
        self.amount = amount
        self.expired = False
        self.race = race

    @property
    def name(self):
        return '-%s malus to allocate between %s' % (self.amount, ', '.join(self.race))

    def stack(self, effect):
        stackable = False
        if (effect.key == self.key):
            if (self.race == effect.race):
                self.amount += effect.amount
                stackable = True
        else:
            raise RuntimeError('Trying to stack two different effect')
        return stackable

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here human have to choose the race to hamper'
        self.expired = True

    @property
    def key(self):
        return 'rmc'
