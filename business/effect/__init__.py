#Base class
class Effect(object):
    def __init__(self, amount):
        self.amount = amount
        self.expired = False

    @property
    def name(self):
        return 'stockEffect'

    @property
    def key(self):
        return 'se'

    def stack(self, effect):
        if (effect.key == self.key):
            self.amount += effect.amount
        else:
            raise RuntimeError('Trying to stack two different effect')
        return True

    def before_resolution(self, army, opposing_armies):
        pass

from business.effect.cantrip import CantripEffect
from business.effect.halved_result import InflictHalvedResultEffect, HalvedResultEffect
from business.effect.no_retaliation_effect import InflictNoRetaliationEffect, NoRetaliationEffect
from business.effect.save_malus import InflictSaveMalusEffect, SaveMalusEffect
from business.effect.targeted_damage import TargetedDamageEffect
from business.effect.targeted_kill import TargetedKillEffect
from business.effect.unsaveable_damage import UnsaveableDamageEffect
from business.effect.unpreventable_damage import UnpreventableDamageEffect
from business.effect.versatile_icon import VersatileIconEffect
