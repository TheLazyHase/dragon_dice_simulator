from business.dice.face import Face
from math import floor

class Army(object):
    def __init__(self):
        self.components = []

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

        #Racial multiplier
        self.racial_multiplier = []

        #Racial substitution
        self.racial_substitution = []

        self.effect = []

    def add(self, dice):
        self.components.append(dice)

    #TBI
    def remove():
        pass

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
        self.racial_multiplier = []

    def add_racial_multiplier(self, race, icon_type):
        self.racial_multiplier.append({'race': race, 'doubled_icon': icon_type})

    def reset_racial_substitution(self):
        self.racial_substitution = []

    def add_racial_substitution(self, race, icon_type_from, icon_type_to):
        self.racial_substitution.append({'race': race, 'icon_from': icon_type_from, 'icon_to': icon_type_to})

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
    def get_result(self, icon_type, desired_race=None, count_id = True):
        result = 0
        result_by_race = {}

        if (count_id):
            ID_multiplier = 1
        else:
            ID_multiplier = 0
        #Non SAI result
        for dice in self.components:
            result += dice.get_result(icon_type, Face.TYPE_NORMAL) + ID_multiplier * dice.get_result(icon_type, Face.TYPE_ID)
            if (dice.race in result_by_race):
                result_by_race[dice.race] += dice.get_result(icon_type, Face.TYPE_NORMAL) + ID_multiplier * dice.get_result(icon_type, Face.TYPE_ID)
            else:
                result_by_race[dice.race] = dice.get_result(icon_type, Face.TYPE_NORMAL) + ID_multiplier * dice.get_result(icon_type, Face.TYPE_ID)
        result = result - self.malus[icon_type]
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
            if (dice.race in result_by_race):
                result_by_race[dice.race] += dice.get_result(icon_type, Face.TYPE_SAI)
            else:
                result_by_race[dice.race] = dice.get_result(icon_type, Face.TYPE_SAI)

        #Land diviser (catastrophs on minor terrain)
        result = floor(result/self.special_diviser[icon_type])
        for race, total in result_by_race.items():
            result_by_race[race] = floor(total/self.special_diviser[icon_type])
        #Land Multiplier (8th faces and minor terrains)
        result = result * self.special_multiplier[icon_type]
        for race, total in result_by_race.items():
            result_by_race[race] = total * self.special_multiplier[icon_type]
        #Racial multiplier
        #We consider each and every racial multiplier to be x2
        #We also consider that malus are substracted from the other races when possible
        #(I.E., if they are more remaining result than racially generated result, we consider all racially generated result have been kept)
        #This cause two bugs :
        # * malus can be considered removed from SAI result of other races
        # * on counter-maneuver in highland, treefolk and dwarves both have a x2 on maneuver, and then treefolk consider dwarves to have absorbed malus, while dwarve consider the opposite
        for racial in self.racial_multiplier:
            if (racial['doubled_icon'] == icon_type):
                result += min(result_by_race[racial['race']], result)

        #Now, racial substitution
        for racial in self.racial_substitution:
            #We do not check for racial substitution if we are checking icon for a racial substitution
            if (desired_race == None):
                if (racial['icon_to'] == icon_type):
                    result += self.get_result(racial['icon_from'], desired_race=racial['race'], count_id=False)
        #Additive bonus
        result = result + self.bonus[icon_type]
        if (result < 0):
            result = 0

        #If we want race-based result, we switch the total with the racial total
        if (desired_race != None):
            result = result_by_race[desired_race] + self.bonus[icon_type]

        return int(floor(result))

    @property
    def melee(self):
        return self.get_result(Face.ICON_MELEE)

    @property
    def missile(self):
        return self.get_result(Face.ICON_MISSILE)

    @property
    def maneuver(self):
        return self.get_result(Face.ICON_MANEUVER)

    @property
    def magic(self):
        return self.get_result(Face.ICON_MAGIC)

    @property
    def save(self):
        return self.get_result(Face.ICON_SAVE)
