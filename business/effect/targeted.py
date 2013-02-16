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

from business.effect import Effect

class TargetedKillEffect(Effect):

    @property
    def name(self):
        return '%s targeted ennemy units must roll ID or die' % self.amount

    @property
    def key(self):
        return 'targeted_kill'

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the targeted death effect should be resolved and saved against'
        self.expired = True

class TargetedBuryEffect(Effect):

    @property
    def name(self):
        return '%s targeted ennemy units must roll ID or be killed and buried' % self.amount

    @property
    def key(self):
        return 'targeted_bury'

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the targeted death effect should be resolved and saved against'
        self.expired = True

class TargetedDamageEffect(Effect):

    @property
    def name(self):
        return '%s damage targeted as the active player choose' % self.amount

    @property
    def key(self):
        return 'targeted_damage'

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the targeted damage should be resolved and saved by the opposing player'
        self.expired = True

class TargetedUnsecableDamageEffect(Effect):

    def __init__(self, amount, increment):
        self.amount = amount
        self.expired = False
        self.increment = increment

    @property
    def name(self):
        return '%s chosen unit suffer %s damages' % (self.amount, self.increment)

    def stack(self, effect):
        stackable = False
        if (effect.key == self.key):
            if (self.increment == effect.increment):
                self.amount += effect.amount
                stackable = True
        else:
            raise RuntimeError('Trying to stack two different effect')
        return stackable

    @property
    def key(self):
        return 'targeted_unsecable_damage'

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the targeted damage should be resolved and saved by the opposing player'
        self.expired = True

class TargetedUnsecableBuryingDamageEffect(Effect):

    def __init__(self, amount, increment):
        self.amount = amount
        self.expired = False
        self.increment = increment

    @property
    def name(self):
        return '%s chosen unit suffer %s damages ; killed unit must save or be buried' % (self.amount, self.increment)

    def stack(self, effect):
        stackable = False
        if (effect.key == self.key):
            if (self.increment == effect.increment):
                self.amount += effect.amount
                stackable = True
        else:
            raise RuntimeError('Trying to stack two different effect')
        return stackable

    @property
    def key(self):
        return 'targeted_unsecable_burying_damage'

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the targeted damage should be resolved and saved by the opposing player'
        self.expired = True

class TargetedIDKillEffect(Effect):

    @property
    def name(self):
        return 'After save are rolled, as an Instant effect, choose and kill %s unit(s) that rolled an ID' % (self.amount)


    @property
    def key(self):
        return 'targeted_ID_kill'

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the targeted damage should be resolved and saved by the opposing player'
        self.expired = True

class TargetedIDKillByHealthEffect(Effect):

    @property
    def name(self):
        return 'After save are rolled, as an Instant effect, choose and kill up to %s worth of unit(s) that rolled an ID' % (self.amount)


    @property
    def key(self):
        return 'targeted_ID_kill'

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the targeted damage should be resolved and saved by the opposing player'
        self.expired = True

class TargetedJawDragonKillEffect(Effect):

    def __init__(self, amount, default_damage):
        self.amount = amount
        self.expired = False
        self.increment = increment

    def stack(self, effect):
        stackable = False
        if (effect.key == self.key):
            if (self.default_damage == effect.default_damage):
                self.amount += effect.amount
                stackable = True
        else:
            raise RuntimeError('Trying to stack two different effect')
        return stackable

    @property
    def name(self):
        return 'Kill up to %s dragon(s) that rolled jaw ; if there is not enough targets, inflict %s damage to any dragon' % (self.amount, self.default_damage)


    @property
    def key(self):
        return 'targeted_ID_kill'

    def before_resolution(self, army, opposing_armies):
        print 'Placeholder - here the targeted damage should be resolved and saved by the opposing player'
        self.expired = True
