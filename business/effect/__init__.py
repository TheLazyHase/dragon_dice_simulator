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

#Turn format : Turn*10000 + Player*100 + Phase
#For each roll, the first number indicate the substep of the roll :
# xx0 : roll not done yet
# xx1 : roll done, instant effect
# xx2 : roll done, SAI effect
# xx3 : roll done and result finalized
# xx4 : aftereffect, if any (wall of thorn f.e.)
# xx5 : roll done and result finalized
#Phase number :
# 000 : initial effect expiration phase
# 100 : racial/ ability phase
# 200 : 8th face phase
# 300 : Royalty phase
# 400 : Dragon attack phase
# 500 : First march phase
# 501 : army chosen, wait for counter-maneuver
# 511 : maneuver roll instant effect, skipped if no counter-maneuver
# 512 : maneuver roll special effect, skipped if no counter-maneuver
# 540 : maneuver roll instant effect, skipped if no counter-maneuver
# 550 : maneuver roll special effect, skipped if no counter-maneuver
# 550 : action
# 600 : Second march phase
# 700 : Reinforce
# 800 : Retreat
# 900 : final effect expiration phase

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

from business.effect.galeforce import GaleforceEffect

from business.effect.halved_result import InflictHalvedResultEffect, HalvedResultEffect
from business.effect.illusion import IllusionEffect

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
