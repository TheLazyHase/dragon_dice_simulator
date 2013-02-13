#SQLAlchemy stuff
from models import (
    DBSession,
    metadata
)

from sqlalchemy import create_engine
import settings
engine = create_engine('mysql+mysqldb://'+settings.db_user+':'+settings.db_password+'@'+settings.db_host+'/'+settings.db_name)
DBSession.configure(bind=engine)
metadata.bind = engine

import models
from business.race import Race
from business.army.roll import *
from business.dice.dice_template import DiceTemplate

health_conversion = {
    1: 'UC',
    2: 'UC',
    3: 'R ',
    4: 'M '
}

result_consistency = {}
result_concentration = {}

result_consistency_by_unit = {}
result_concentration_by_unit = {}

for race in Race.get_all():
    result_consistency[race.id] = {
        'UC': {'Melee': 0, 'Missile': 0, 'Maneuver': 0, 'Save': 0, 'Magic': 0},
        'R ': {'Melee': 0, 'Missile': 0, 'Maneuver': 0, 'Save': 0, 'Magic': 0},
        'M ': {'Melee': 0, 'Missile': 0, 'Maneuver': 0, 'Save': 0, 'Magic': 0},
    }
    result_concentration[race.id] = {
        'UC': {'Melee': 0, 'Missile': 0, 'Maneuver': 0, 'Save': 0, 'Magic': 0},
        'R ': {'Melee': 0, 'Missile': 0, 'Maneuver': 0, 'Save': 0, 'Magic': 0},
        'M ': {'Melee': 0, 'Missile': 0, 'Maneuver': 0, 'Save': 0, 'Magic': 0},
    }
    result_consistency_by_unit[race.id] = {}
    result_concentration_by_unit[race.id] = {}

    for dice_template in race.dices:
        melee_amount = 0
        missile_amount = 0
        maneuver_amount = 0
        save_amount = 0
        magic_amount = 0

        melee_faces = 0
        missile_faces = 0
        maneuver_faces = 0
        save_faces = 0
        magic_faces = 0

        i = 0

        for face_template in dice_template.faces:
            i += 1
            face = face_template.get_instance()

            face.type_roll = TestRoll()
            melee_amount += face.melee
            if (face.melee > 0):
                melee_faces += 1

            missile_amount += face.missile
            if (face.missile > 0):
                missile_faces += 1

            maneuver_amount += face.maneuver
            if (face.maneuver > 0):
                maneuver_faces += 1

            save_amount += face.save
            if (face.save > 0):
                save_faces += 1

            magic_amount += face.magic
            if (face.magic > 0):
                magic_faces += 1

        melee_rate = melee_faces*100/i
        missile_rate = missile_faces*100/i
        maneuver_rate = maneuver_faces*100/i
        save_rate = save_faces*100/i
        magic_rate = magic_faces*100/i

        melee_concentration = 4.0 * float(melee_amount)/(float(dice_template.type.health) * float(i))
        missile_concentration = 4.0 * float(missile_amount)/(float(dice_template.type.health) * float(i))
        maneuver_concentration = 4.0 * float(maneuver_amount)/(float(dice_template.type.health) * float(i))
        save_concentration = 4.0 * float(save_amount)/(float(dice_template.type.health) * float(i))
        magic_concentration = 4.0 * float(magic_amount)/(float(dice_template.type.health) * float(i))

        if melee_concentration > result_concentration[race.id][health_conversion[dice_template.type.health]]['Melee']:
            result_concentration[race.id][health_conversion[dice_template.type.health]]['Melee'] = melee_concentration
        if melee_rate > result_consistency[race.id][health_conversion[dice_template.type.health]]['Melee']:
            result_consistency[race.id][health_conversion[dice_template.type.health]]['Melee'] = melee_rate

        if missile_concentration > result_concentration[race.id][health_conversion[dice_template.type.health]]['Missile']:
            result_concentration[race.id][health_conversion[dice_template.type.health]]['Missile'] = missile_concentration
        if missile_rate > result_consistency[race.id][health_conversion[dice_template.type.health]]['Missile']:
            result_consistency[race.id][health_conversion[dice_template.type.health]]['Missile'] = missile_rate

        if maneuver_concentration > result_concentration[race.id][health_conversion[dice_template.type.health]]['Maneuver']:
            result_concentration[race.id][health_conversion[dice_template.type.health]]['Maneuver'] = maneuver_concentration
        if maneuver_rate > result_consistency[race.id][health_conversion[dice_template.type.health]]['Maneuver']:
            result_consistency[race.id][health_conversion[dice_template.type.health]]['Maneuver'] = maneuver_rate

        if save_concentration > result_concentration[race.id][health_conversion[dice_template.type.health]]['Save']:
            result_concentration[race.id][health_conversion[dice_template.type.health]]['Save'] = save_concentration
        if save_rate > result_consistency[race.id][health_conversion[dice_template.type.health]]['Save']:
            result_consistency[race.id][health_conversion[dice_template.type.health]]['Save'] = save_rate

        if magic_concentration > result_concentration[race.id][health_conversion[dice_template.type.health]]['Magic']:
            result_concentration[race.id][health_conversion[dice_template.type.health]]['Magic'] = magic_concentration
        if magic_rate > result_consistency[race.id][health_conversion[dice_template.type.health]]['Magic']:
            result_consistency[race.id][health_conversion[dice_template.type.health]]['Magic'] = magic_rate

        result_concentration_by_unit[race.id][dice_template.id] = {
            'Melee': melee_concentration,
            'Missile': missile_concentration,
            'Maneuver': maneuver_concentration,
            'Save': save_concentration,
            'Magic': magic_concentration,
        }

        result_consistency_by_unit[race.id][dice_template.id] = {
            'Melee': melee_rate,
            'Missile': missile_rate,
            'Maneuver': maneuver_rate,
            'Save': save_rate,
            'Magic': magic_rate,
        }

print 'Concentration report :'
for race_id, race_value in result_concentration.items():
    race = Race.get_by_id(race_id).name
    print 'Race '+race+':'
    for category, category_value in race_value.items():
        string = '    Category '+category+': '
        for icon, value in category_value.items():
            string += icon+': '+str(round(value,2))+'; '
        print string

print 'Consistency report :'
for race_id, race_value in result_consistency.items():
    race = Race.get_by_id(race_id).name
    print 'Race '+race+':'
    for category, category_value in race_value.items():
        string = '    Category '+category+': '
        for icon, value in category_value.items():
            string += str(icon)+': '+str(value)+'%; '
        print string

print 'CSV Consistency :'
for race_id in sorted(result_consistency.iterkeys()):
    race = Race.get_by_id(race_id).name
    race_value = result_consistency[race_id]
    string = '%s,%s,%s,%s,%s,%s,' % (race, race_value['UC']['Melee'], race_value['UC']['Missile'],race_value['UC']['Maneuver'],race_value['UC']['Save'],race_value['UC']['Magic'])
    string += '%s,%s,%s,%s,%s,' % (race_value['R ']['Melee'], race_value['R ']['Missile'],race_value['R ']['Maneuver'],race_value['R ']['Save'],race_value['R ']['Magic'])
    string += '%s,%s,%s,%s,%s' % (race_value['M ']['Melee'], race_value['M ']['Missile'],race_value['M ']['Maneuver'],race_value['M ']['Save'],race_value['M ']['Magic'])
    print string

print 'Unit report :'
for race_id in sorted(result_concentration_by_unit.iterkeys()):
    print '========================================================='
    race = Race.get_by_id(race_id).name
    print race+':'
    race_value = result_concentration_by_unit[race_id]
    for dice_id in sorted(race_value.iterkeys()):
        dice_value = race_value[dice_id]
        dice_name = DiceTemplate.get_by_id(dice_id).name
        
        string = dice_name.ljust(30)+': '
        total = 0
        for icon, value in dice_value.items():
            total += value
            string += (str(icon)+': '+str(value)+'; ').ljust(12)
        string = dice_name.ljust(30)+': '+str(round(total * 6.0, 2))
        print string
