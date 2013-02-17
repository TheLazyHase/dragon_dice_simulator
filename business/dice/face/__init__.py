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
class Face(object):
    #Constant for face types
    TYPE_NORMAL = 1
    TYPE_ID = 2
    TYPE_SAI = 3

    ICON_MELEE = 1
    ICON_MISSILE = 2
    ICON_MANEUVER = 3
    ICON_MAGIC = 4
    ICON_SAVE = 5

    ICON_NAME = {
        ICON_MELEE: 'Melee',
        ICON_MISSILE: 'Missile',
        ICON_MANEUVER: 'Maneuver',
        ICON_MAGIC: 'Magic',
        ICON_SAVE: 'Save',
    }

    #type of icon
    icon = {
        ICON_MELEE: 0,
        ICON_MISSILE: 0,
        ICON_MANEUVER: 0,
        ICON_MAGIC: 0,
        ICON_SAVE: 0,
    }

    def __init__(self, amount, dice):
        self.amount = amount
        self.dice = dice

    @property   
    def type(self):
        return Face.TYPE_NORMAL

    @property
    def name(self):
        return 'nothing'

    def icons(self, icon_type):
        if (self.type_roll.is_test):
            return_value = self.test_value(icon_type)
        else:
            return_value = self.icon_by_type(icon_type)
        return return_value

    #This function is here to be overwritten to give meaningful value for statistic test rolls
    def test_value(self, icon_type):
        return self.icon_by_type(icon_type)

    def icon_by_type(self, icon_type):
        return self.amount * self.icon[icon_type]

    @property
    def melee(self):
        return self.icons(Face.ICON_MELEE)

    @property
    def missile(self):
        return self.icons(Face.ICON_MISSILE)

    @property
    def maneuver(self):
        return self.icons(Face.ICON_MANEUVER)

    @property
    def magic(self):
        return self.icons(Face.ICON_MAGIC)

    @property
    def save(self):
        return self.icons(Face.ICON_SAVE)

    @property
    def on_instant(self):
        return None

    @property
    def on_special(self):
        return None

    @property
    def on_normal(self):
        return None

    @property
    def on_late(self):
        return None

    @property
    def on_delayed(self):
        return None

    @property
    def is_rerolled(self):
        return False

#Regular
from business.dice.face.standard.save import Save
from business.dice.face.standard.melee import Melee
from business.dice.face.standard.missile import Missile
from business.dice.face.standard.maneuver import Maneuver
from business.dice.face.standard.magic import Magic

from business.dice.face.standard.id import ID
from business.dice.face.standard.group_id import GroupID

#SAI
#templates
from business.dice.face.sai import SAI
from business.dice.face.melee_with_special import MeleeWithSpecial
from business.dice.face.special_on_melee import SpecialOnMelee
from business.dice.face.missile_with_special import MissileWithSpecial
from business.dice.face.special_on_missile import SpecialOnMissile
from business.dice.face.special_on_non_maneuver import SpecialOnNonManeuver

#True SAI
from business.dice.face.attune import Attune

from business.dice.face.save_with_special.bash import Bash
from business.dice.face.belly import Belly
from business.dice.face.special_on_melee.breath import Breath
from business.dice.face.missile_with_special.bullseye import Bullseye

from business.dice.face.special_on_non_maneuver.cantrip import Cantrip
from business.dice.face.special_on_melee.charge import Charge
from business.dice.face.special_on_melee.charm import Charm
from business.dice.face.special_on_melee.choke import Choke
from business.dice.face.melee_with_special.coil import Coil
from business.dice.face.special_on_attack.confuse import Confuse
from business.dice.face.special_on_melee.convert import Convert
from business.dice.face.save_with_special.counter import Counter
from business.dice.face.versatile_result.create_fireminions import CreateFireminions
from business.dice.face.missile_with_special.crush import Crush

from business.dice.face.special_on_melee.decapitate import Decapitate
from business.dice.face.dispel_magic import DispelMagic
from business.dice.face.melee_with_reroll.double_strike import DoubleStrike

from business.dice.face.elevate import Elevate
from business.dice.face.special_on_melee.entangle import Entangle

from business.dice.face.special_on_non_maneuver.ferry import Ferry
from business.dice.face.special_on_missile.firecloud import Firecloud
from business.dice.face.special_on_non_maneuver.firewalking import Firewalking
from business.dice.face.special_on_melee.flame import Flame
from business.dice.face.missile_with_special.flaming_arrow import FlamingArrow
from business.dice.face.melee_with_reroll.flurry import Flurry
from business.dice.face.versatile_result.fly import Fly
from business.dice.face.special_on_attack.frost_breath import FrostBreath

from business.dice.face.special_on_action.galeforce import Galeforce
from business.dice.face.melee_with_special.gore import Gore

from business.dice.face.special_on_attack.howl import Howl
from business.dice.face.melee_with_special.hug import Hug

from business.dice.face.special_on_action.illusion import Illusion
from business.dice.face.special_on_missile.impale import Impale

from business.dice.face.melee_with_special.kick import Kick

from business.dice.face.logo import Logo

from business.dice.face.special_on_attack.net import Net

from business.dice.face.special_on_melee.plague import Plague
from business.dice.face.special_on_melee.poison import Poison

from business.dice.face.save_with_special.regenerate import Regenerate
from business.dice.face.melee_with_reroll.rend import Rend
from business.dice.face.save_with_special.rise_from_ashes import RiseFromAshes
from business.dice.face.special_on_melee.roar import Roar

from business.dice.face.special_on_melee.scare import Scare
from business.dice.face.special_on_melee.screech import Screech
from business.dice.face.special_on_missile.seize import Seize
from business.dice.face.special_on_melee.slay import Slay
from business.dice.face.special_on_melee.sleep import Sleep
from business.dice.face.melee_with_special.smite import Smite
from business.dice.face.special_on_melee.smother import Smother
from business.dice.face.sneak_attack import SneakAttack
from business.dice.face.save_with_special.sortie import Sortie
from business.dice.face.melee_with_special.stomp import Stomp
from business.dice.face.missile_with_special.stone import Stone
from business.dice.face.special_on_melee.stun import Stun
from business.dice.face.summon_dragon import SummonDragon
from business.dice.face.special_on_melee.surprise import Surprise
from business.dice.face.special_on_melee.swallow import Swallow

from business.dice.face.melee_with_reroll.tail import Tail
from business.dice.face.special_on_non_maneuver.teleport import Teleport
from business.dice.face.versatile_result.trample import Trample
from business.dice.face.special_on_melee.trumpet import Trumpet

from business.dice.face.save_with_special.vanish import Vanish
from business.dice.face.save_with_special.volley import Volley

from business.dice.face.wave import Wave
from business.dice.face.wayfare import Wayfare
from business.dice.face.special_on_melee.web import Web
from business.dice.face.save_with_special.wild_growth import WildGrowth
from business.dice.face.special_on_melee.wither import Wither
