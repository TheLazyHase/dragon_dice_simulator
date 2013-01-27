from business.dice.face import Face
from math import floor
from business.effect import RacialMalusChoiceEffect

class Army(object):
    def __init__(self, position=None):
        self.components = []
        self.position = position

        #Modifiers
        self.malus = {
            Face.ICON_MELEE: 0,
            Face.ICON_MISSILE: 0,
            Face.ICON_MANEUVER: 0,
            Face.ICON_MAGIC: 0,
            Face.ICON_SAVE: 0,
        }

        #For spell, dragon breath, or SAI multiplier or diviser
        self.regular_diviser = {
            Face.ICON_MELEE: 1,
            Face.ICON_MISSILE: 1,
            Face.ICON_MANEUVER: 1,
            Face.ICON_MAGIC: 1,
            Face.ICON_SAVE: 1,
        }

        self.regular_multiplier = {
            Face.ICON_MELEE: 1,
            Face.ICON_MISSILE: 1,
            Face.ICON_MANEUVER: 1,
            Face.ICON_MAGIC: 1,
            Face.ICON_SAVE: 1,
        }

        #For land or other special multiplier or diviser
        self.special_multiplier = {
            Face.ICON_MELEE: 1,
            Face.ICON_MISSILE: 1,
            Face.ICON_MANEUVER: 1,
            Face.ICON_MAGIC: 1,
            Face.ICON_SAVE: 1,
        }

        self.special_diviser = {
            Face.ICON_MELEE: 1,
            Face.ICON_MISSILE: 1,
            Face.ICON_MANEUVER: 1,
            Face.ICON_MAGIC: 1,
            Face.ICON_SAVE: 1,
        }

        self.bonus = {
            Face.ICON_MELEE: 0,
            Face.ICON_MISSILE: 0,
            Face.ICON_MANEUVER: 0,
            Face.ICON_MAGIC: 0,
            Face.ICON_SAVE: 0,
        }

        #Racial multiplier or substitution
        self.racial_modifier = {}

        #Racial substitution are put in this again to make thing simpler
        self.racial_substitution = {}

        self.effect = []

    @property
    def result_description(self):
        result = ''
        for dice in self.components:
            result = result + dice.result_description + "\r\n"
        return result

    def add_bonus(self, icon_type, value=1):
        self.bonus[icon_type] += value
        if (self.bonus[icon_type] < 0):
            self.bonus[icon_type] = 0
        return self

    def reset_bonus(self, icon_type, value=1):
        self.bonus[icon_type] = 0
        return self

    def add_malus(self, icon_type, value=1):
        self.malus[icon_type] += value
        if (self.malus[icon_type] < 0):
            self.malus[icon_type] = 0
        return self

    def reset_malus(self, icon_type, value=1):
        self.malus[icon_type] = 0
        return self

    def add_multiplier(self, icon_type, value=2):
        self.regular_multiplier[icon_type] *= value
        if (self.regular_multiplier[icon_type] < 0):
            self.regular_multiplier[icon_type] = 0
        return self

    def reset_multiplier(self, icon_type, value=1):
        self.regular_multiplier[icon_type] = 0
        return self

    def add_diviser(self, icon_type, value=2):
        self.regular_diviser[icon_type] *= value
        if (self.regular_diviser[icon_type] < 1):
            self.regular_diviser[icon_type] = 1
        return self

    def reset_diviser(self, icon_type, value=1):
        self.regular_diviser[icon_type] = 0
        return self

    def add_special_multiplier(self, icon_type, value=2):
        self.special_multiplier[icon_type] *= value
        if (self.special_multiplier[icon_type] < 0):
            self.special_multiplier[icon_type] = 0
        return self

    def reset_special_multiplier(self, icon_type, value=1):
        self.special_multiplier[icon_type] = 0
        return self

    def add_special_diviser(self, icon_type, value=2):
        self.special_diviser[icon_type] *= value
        if (self.special_diviser[icon_type] < 1):
            self.special_diviser[icon_type] = 1
        return self

    def reset_special_diviser(self, icon_type, value=1):
        self.special_diviser[icon_type] = 0
        return self

    def reset_racial_multiplier(self):
        self.racial_modifier = []

    def add_racial_multiplier(self, race, icon_type):
        self.racial_modifier[icon_type][race].append('x2')
        return self
            
    def add_racial_substitution(self, race, icon_type_from, icon_type_to):
        self.racial_modifier[icon_type_from][race].append(icon_type_to)
        self.racial_substitution[icon_type_to][race].append(icon_type_from)
        return self


    def modifier_description(self, icon_type):
        result = ''
        if self.malus[icon_type] > 0:
            result +=  "\r\n" + ('* %s malus to the roll ' % self.malus[icon_type])
        if self.regular_multiplier[icon_type] > 1:
            result +=  "\r\n" + ('* Roll multiplied by %s' % self.regular_multiplier[icon_type])
        if self.regular_diviser[icon_type] > 1:
            result +=  "\r\n" + ('* Roll divided by %s ' % self.regular_diviser[icon_type])
        if self.special_multiplier[icon_type] > 1:
            result +=  "\r\n" + ('* Terrain effect : roll multiplied by %s' % self.special_multiplier[icon_type])
        if self.special_diviser[icon_type] > 1:
            result +=  "\r\n" + ('* Disaster effect : roll divided by %s ' % self.special_diviser[icon_type])
        if self.bonus[icon_type] > 0:
            result +=  "\r\n" + ('* %s bonus to the roll ' % self.bonus[icon_type])
        for racial in self.racial_multiplier:
            if (racial['doubled_icon'] == icon_type):
                result += "\r\n" + ('* %s dices %s are doubled ' % (racial['race'], Face.ICON_NAME[racial['doubled_icon']]))
        for racial in self.racial_substitution:
            if (racial['icon_to'] == icon_type):
                result += "\r\n" + ('* %s dices %s count as %s ' % (racial['race'], Face.ICON_NAME[racial['icon_from']], Face.ICON_NAME[racial['icon_to']]))

        if (result == ''):
            result = 'None'

        return result

    def roll(self, type_roll):
        self.type_roll = type_roll
        for dice in self.components:
            dice.roll(type_roll)

        #Check rolled effect
        for dice in self.components:
            if (dice.special_effect != None):
                for effect in dice.special_effect:
                    #We hope an army will not drown under special effect here :x
                    have_stacked = False
                    for old_effect in self.effect:
                        if (old_effect.key == effect.key):
                            have_stacked = old_effect.stack(effect)
                    if (not have_stacked):
                        self.effect.append(effect)
        return self

    def get_rolled_effect(self):

        return instant_effect

    @property
    def effect_description(self):
        result = ''
        for effect in self.effect:
            result +=  "\r\n" + ('* %s' % effect.name)

        return result

    def do_before_resolution_effect(self, opposing_armies):
        cleaned_effect_list = []
        for effect in self.effect:
            effect.before_resolution(self, opposing_armies)
            if not effect.expired:
                cleaned_effect_list.append(effect)
        self.effect = cleaned_effect_list
        return self

    #desired_race is used to get result for a particular race
    #it does not use racial icon replacement, because it is used by racial icon replacement, and this could lead to infinite loop
    def get_result(self, icon_type, desired_race=None):
        result = 0
        result_by_race = {}

        #Non SAI result
        for dice in self.components:
            result += dice.get_result(icon_type, Face.TYPE_NORMAL) + dice.get_result(icon_type, Face.TYPE_ID)
            if (dice.race.tag in result_by_race):
                result_by_race[dice.race.tag] += dice.get_result(icon_type, Face.TYPE_NORMAL) + dice.get_result(icon_type, Face.TYPE_ID)
            else:
                result_by_race[dice.race.tag] = dice.get_result(icon_type, Face.TYPE_NORMAL) + dice.get_result(icon_type, Face.TYPE_ID)

        #Malus
        result -= self.malus[icon_type]
        #Now, apply malus to race

        # @TODO : take into account choice made (and saved as an effect)
        #First case : only one race, we apply the malus to it
        if len(result_by_race.keys()) < 2:
            for race in result_by_race.keys():
                result_by_race[race] -= self.malus[icon_type]
                if result_by_race[race] < 0:
                    result_by_race[race] = 0
        else:
            #Complicated thing start, since we have multiple race
            remaining_malus = self.malus[icon_type]
            race_with_relevant_racial = []
            #We start by trying to remove the malus from races who have no relevant racial bonus
            for race in result_by_race.keys():
                #Once the remaining_malus is liquidated, we can just skip all that.
                if remaining_malus > 0:
                    if (not icon_type in self.racial_modifier):
                        #No racial on the icon type ? Malus can be put anywhere.
                        if (remaining_malus < result_by_race[race]):
                            result_by_race[race] -= remaining_malus
                            remaining_malus = 0
                        else:
                            remaining_malus -= result_by_race[race]
                            result_by_race[race] = 0
                    elif (not race in self.racial_modifier[icon_type]):
                        #This race have no relevant racial ? Malus can be put on it
                        if (remaining_malus < result_by_race[race]):
                            result_by_race[race] -= remaining_malus
                            remaining_malus = 0
                        else:
                            remaining_malus -= result_by_race[race]
                            result_by_race[race] = 0
                    elif (('x2' not in self.racial_modifier[icon_type][race]) and (self.racial_modifier[icon_type][race] not in self.type_roll.allowed_icon)):
                        #This is a racial that substitute current icon to useless icon for the roll. Malus can be put on it
                        if (remaining_malus < result_by_race[race]):
                            result_by_race[race] -= remaining_malus
                            remaining_malus = 0
                        else:
                            remaining_malus -= result_by_race[race]
                            result_by_race[race] = 0
                    else:
                        #This race have (at least) one racial relevant to the situation at hand.
                        race_with_relevant_racial.append(race)
            if remaining_malus > 0:
                if len(race_with_relevant_racial) == 0:
                    #No race remaining for the malus
                    pass
                elif len(race_with_relevant_racial) == 1:
                    #Only one race with relevant racial, must put malus on it
                    #We purposefully don't substract remaining malus, so that the player see the total count for thoses
                    result_by_race[race] -= remaining_malus
                    if result_by_race[race] < 0:
                        result_by_race[race] = 0
                else:
                    #Choice cannot be done automatically so add a effect for that
                    self.effect.append(RacialMalusChoiceEffect(remaining_malus, relevant_race))
        #Diviser
        result = floor(result/self.regular_diviser[icon_type])
        for race, total in result_by_race.items():
            #Race result are not floored, for some specifics doubling scenario
            #(namely, when on a counter-maneuver roll with dwarves and treefolks on a highland, there is no separate rounding for each races)
            result_by_race[race] = total/self.regular_diviser[icon_type]
        #Multiplier
        result = result * self.regular_multiplier[icon_type]
        for race, total in result_by_race.items():
            result_by_race[race] = total * self.regular_multiplier[icon_type]
        if (result < 0):
            result = 0

        #SAI result, which are unaffected by spell, breath, and SAI are added now
        for dice in self.components:
            result = result + dice.get_result(icon_type, Face.TYPE_SAI)
            if (dice.race.tag in result_by_race):
                result_by_race[dice.race.tag] += dice.get_result(icon_type, Face.TYPE_SAI)
            else:
                result_by_race[dice.race.tag] = dice.get_result(icon_type, Face.TYPE_SAI)

        #Land diviser (catastrophs on minor terrain)
        result = floor(result/self.special_diviser[icon_type])
        for race, total in result_by_race.items():
            result_by_race[race] = floor(total/self.special_diviser[icon_type])
        #Land Multiplier (8th faces and minor terrains)
        result = result * self.special_multiplier[icon_type]
        for race, total in result_by_race.items():
            result_by_race[race] = total * self.special_multiplier[icon_type]
        #Racial multiplier
        if (icon_type in self.racial_modifier):
            for race in self.racial_modifier.items():
                if ('x2' in racials):
                    result += result_by_race[racial['race']]

        #Racial substitution
        if (icon_type in self.racial_substitution):
            for race, racial in self.racial_substitution.items():
                for icon_from in racial:
                    result += self.get_result(icon_from, desired_race=race)
        #dice-wide additive bonus (dragonkin autosave)
        for dice in self.components:
            result += dice.autoresult[icon_type]
            result[dice.race.tag] += dice.autoresult[icon_type]
        #Army-wide additive bonus
        #If we want race-based result, we switch the total with the racial total
        if (desired_race == None):
            result += self.bonus[icon_type]
        else:
            result = result_by_race[desired_race] + self.bonus[icon_type]

        #Sanity check
        if (result < 0):
            result = 0

        return int(floor(result))

    def get_melee_result(self):
        return self.get_result(Face.ICON_MELEE)

    def get_missile_result(self):
        return self.get_result(Face.ICON_MISSILE)

    def get_maneuver_result(self):
        return self.get_result(Face.ICON_MANEUVER)

    def get_magic_result(self):
        return self.get_result(Face.ICON_MAGIC)

    def get_save_result(self):
        return self.get_result(Face.ICON_SAVE)
