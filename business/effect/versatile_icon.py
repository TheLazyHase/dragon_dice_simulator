from business.effect import Effect
from business.dice.face import Face

class VersatileIconEffect(Effect):

    def __init__(self, amount, option=[]):
        self.amount = amount
        self.expired = False
        self.option = option

    @property
    def name(self):
        return '%s icon to choose between %s' % (self.amount, ', '.join(Face.ICON_NAME[face_type] for face_type in self.option))

    def stack(self, effect):
        stackable = False
        if (effect.key == self.key):
            if (self.option == effect.option):
                self.amount += effect.amount
                stackable = True
        else:
            raise RuntimeError('Trying to stack two different effect')
        return stackable

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here human have to choose between icon type'
        self.expired = True

    @property
    def key(self):
        return 'vi'
