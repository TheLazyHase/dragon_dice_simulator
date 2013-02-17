# -*- coding: utf-8 *-*
# Copyright (c) 2013 Tisserant Pierre
#
# This file is part of Dragon dice simulator.
#
#    Dragon dice simulator is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Dragon dice simulator is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Dragon dice simulator.  If not, see <http://www.gnu.org/licenses/>.

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

from business.effect.attune import AttuneEffect

from business.effect.brawl import UnsaveableBrawl, SaveableBrawl

from business.effect.cantrip import CantripEffect

from business.effect.dragon_summoning import DragonSummoningEffect

from business.effect.escape import EscapeAndSaveEffect
from business.effect.escape import EscapeItemEffect
from business.effect.elevate import ElevateSaveDoublingEffect, ElevateMissileDoublingEffect, ElevateSaveOrMissileDoublingEffect

from business.effect.flurry_reroll import FlurryRerollEffect

from business.effect.halved_result import InflictHalvedResultEffect, HalvedResultEffect

from business.effect.malus import BellyMalusEffect, InflictSaveMalusEffect, SaveMalusEffect,InflictManeuverMalusEffect, ManeuverMalusEffect

from business.effect.no_retaliation_effect import InflictNoRetaliationEffect, NoRetaliationEffect

from business.effect.racial_malus_choice import RacialMalusChoiceEffect
from business.effect.reflect_damage import ReflectDamageEffect
from business.effect.regeneration import RegenerationEffect

from business.effect.targeted import TargetedBuryEffect
from business.effect.targeted import TargetedDamageEffect
from business.effect.targeted import TargetedKillEffect
from business.effect.targeted import TargetedUnsecableDamageEffect
from business.effect.targeted import TargetedUnsecableBuryingDamageEffect
from business.effect.targeted import TargetedIDKillEffect
from business.effect.targeted import TargetedIDKillByHealthEffect
from business.effect.targeted import TargetedJawDragonKillEffect
from business.effect.targeted import TargetedUnsecableInstantBuryingDamageEffect
from business.effect.targeted import TargetedManeuverKillByHealthEffect
from business.effect.targeted import TargetedManeuverKillBuryingByHealthEffect
from business.effect.targeted import TargetedKillBuryingByHealthEffect

from business.effect.unsaveable_damage import UnsaveableDamageEffect
from business.effect.unpreventable_damage import UnpreventableDamageEffect, ArmyUnpreventableDamageEffect

from business.effect.versatile_icon import VersatileIconEffect

from business.effect.promotion import PromotionEffect, PromotionSaveEffect
