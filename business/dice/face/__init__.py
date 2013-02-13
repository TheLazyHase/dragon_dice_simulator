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

    def __init__(self, amount):
        self.amount = amount

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
    def special_effect(self):
        return None
    @property
    def is_rerolled(self):
        return False

#Regular
from business.dice.face.save import Save
from business.dice.face.melee import Melee
from business.dice.face.missile import Missile
from business.dice.face.maneuver import Maneuver
from business.dice.face.magic import Magic

from business.dice.face.id import ID
from business.dice.face.group_id import GroupID

#SAI
#templates
from business.dice.face.sai import SAI
from business.dice.face.melee_special_effect import MeleeSpecialEffect
from business.dice.face.missile_special_effect import MissileSpecialEffect
from business.dice.face.maneuver_special_effect import ManeuverSpecialEffect
from business.dice.face.save_special_effect import SaveSpecialEffect
from business.dice.face.magic_special_effect import MagicSpecialEffect

#True SAI
from business.dice.face.attune import Attune

from business.dice.face.bash import Bash
from business.dice.face.belly import Belly
from business.dice.face.breath import Breath
from business.dice.face.bullseye import Bullseye

from business.dice.face.cantrip import Cantrip
from business.dice.face.charge import Charge
from business.dice.face.charm import Charm
from business.dice.face.choke import Choke
from business.dice.face.coil import Coil
from business.dice.face.confuse import Confuse
from business.dice.face.convert import Convert
from business.dice.face.counter import Counter
from business.dice.face.create_fireminions import CreateFireminions
from business.dice.face.crush import Crush

from business.dice.face.decapitate import Decapitate
from business.dice.face.dispel_magic import DispelMagic
from business.dice.face.double_strike import DoubleStrike

from business.dice.face.elevate import Elevate
from business.dice.face.entangle import Entangle

from business.dice.face.ferry import Ferry
from business.dice.face.firecloud import Firecloud
from business.dice.face.firewalking import Firewalking
from business.dice.face.flame import Flame
from business.dice.face.flaming_arrow import FlamingArrow
from business.dice.face.flurry import Flurry
from business.dice.face.fly import Fly
from business.dice.face.frost_breath import FrostBreath

from business.dice.face.galeforce import Galeforce
from business.dice.face.gore import Gore

from business.dice.face.howl import Howl
from business.dice.face.hug import Hug

from business.dice.face.illusion import Illusion
from business.dice.face.impale import Impale

from business.dice.face.kick import Kick

from business.dice.face.logo import Logo

from business.dice.face.net import Net

from business.dice.face.plague import Plague
from business.dice.face.poison import Poison

from business.dice.face.regenerate import Regenerate
from business.dice.face.rend import Rend
from business.dice.face.rise_from_ashes import RiseFromAshes
from business.dice.face.roar import Roar

from business.dice.face.scare import Scare
from business.dice.face.screech import Screech
from business.dice.face.seize import Seize
from business.dice.face.slay import Slay
from business.dice.face.sleep import Sleep
from business.dice.face.smite import Smite
from business.dice.face.smother import Smother
from business.dice.face.sneak_attack import SneakAttack
from business.dice.face.sortie import Sortie
from business.dice.face.stomp import Stomp
from business.dice.face.stone import Stone
from business.dice.face.stun import Stun
from business.dice.face.summon_dragon import SummonDragon
from business.dice.face.surprise import Surprise
from business.dice.face.swallow import Swallow

from business.dice.face.tail import Tail
from business.dice.face.teleport import Teleport
from business.dice.face.trample import Trample
from business.dice.face.trumpet import Trumpet

from business.dice.face.vanish import Vanish
from business.dice.face.volley import Volley

from business.dice.face.wave import Wave
from business.dice.face.wayfare import Wayfare
from business.dice.face.web import Web
from business.dice.face.wild_growth import WildGrowth
from business.dice.face.wither import Wither
