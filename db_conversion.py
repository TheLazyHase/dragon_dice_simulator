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

#This script suppose a precise db, which is not publicy available
from models import (
    DBSession,
    metadata
)

#First, load sql_alchemy
from sqlalchemy import create_engine
import settings
engine = create_engine('mysql+mysqldb://'+settings.db_user+':'+settings.db_password+'@'+settings.db_host+'/'+settings.db_name)
DBSession.configure(bind=engine)
metadata.bind = engine

import models
from business.dice.dice_template import DiceTemplate
from business.dice.dice_face_template import DiceFaceTemplate
from business.dice.dice_element import DiceElement
from business.dice.face import Face

#A conversion dictionary
conversion_icon = {
    'MELEE': 'Melee',
    'MISSILE': 'Missile',
    'MANEUVER': 'Maneuver',
    'MAGIC': 'Magic',
    'SAVE': 'Save',
    'ID': 'ID',
    'GROUPID': 'GroupID',

    'ATTUNE': 'Attune',

    'BASH': 'Bash',
    'DKIN_BELLY': 'Belly',
    'DKIN_BREATH': 'Breath',
    'BULLSEYE': 'Bullseye',

    'CANTRIP': 'Cantrip',
    'CHARGE': 'Charge',
    'CHARM': 'Charm',
    'CHOKE': 'Choke',
    'COIL': 'Coil',
    'COUNTER': 'Counter',
    'CONFUSE': 'Confuse',
    'CONVERT': 'Convert',
    'CREATE_FIREMINIONS': 'CreateFireminions',
    'CRUSH': 'Crush',

    'DECAPITATE': 'Decapitate',
    'DISPEL_MAGIC': 'DispelMagic',
    'DOUBLE_STRIKE': 'DoubleStrike',

    'ELEVATE': 'Elevate',
    'ENTANGLE': 'Entangle',

    'FERRY': 'Ferry',
    'FIRECLOUD': 'Firecloud',
    'FIREWALKING': 'Firewalking',
    'FLAME': 'Flame',
    'FLAMING_ARROW': 'FlamingArrow',
    'FLURRY': 'Flurry',
    'FLY': 'Fly',
    'FROST_BREATH': 'FrostBreath',

    'GALEFORCE': 'Galeforce',
    'GORE': 'Gore',

    'HOWL': 'Howl',
    'HUG': 'Hug',

    'ILLUSION': 'Illusion',
    'IMPALE': 'Impale',

    'KICK': 'Kick',

    'LOGO': 'Logo',

    'NET': 'Net',

    'PLAGUE': 'Plague',
    'POISON': 'Poison',

    'REGENERATE': 'Regenerate',
    'REND': 'Rend',
    'RISE_FROM_THE_ASHES': 'RiseFromAshes',
    'ROAR': 'Roar',

    'SCARE': 'Scare',
    'SCREECH': 'Screech',
    'SEIZE': 'Seize',
    'SLAY': 'Slay',
    'SLEEP': 'Sleep',
    'SMITE': 'Smite',
    'SMOTHER': 'Smother',
    'SNEAKATTACK': 'SneakAttack',
    'SORTIE': 'Sortie',
    'STOMP': 'Stomp',
    'STONE': 'Stone',
    'STUN': 'Stun',
    'SUMMON_DRAGON': 'SummonDragon',
    'SURPRISE': 'Surprise',
    'SWALLOW': 'Swallow',

    'TAIL': 'Tail',
    'TELEPORT': 'Teleport',
    'TRAMPLE': 'Trample',
    'TRUMPET': 'Trumpet',

    'VANISH': 'Vanish',
    'VOLLEY': 'Volley',

    'WAVE': 'Wave',
    'WAYFARE': 'Wayfare',
    'WEB': 'Web',
    'WILD_GROWTH': 'WildGrowth',
    'WITHER': 'Wither',

    #For non released stuff
    'NONE': 'Melee',
}

from business.element import Element
conversion_color = {
    'WATER': Element.get_by_id(3),
    'AIR': Element.get_by_id(1),
    'EARTH': Element.get_by_id(4),
    'FIRE': Element.get_by_id(2),
    'DEATH': Element.get_by_id(5),
    'IVORY': Element.get_by_id(6),
    'WHITE': Element.get_by_id(7)
}

from business.dice.dice_type import DiceType
conversion_unit_type = {
    1: DiceType.get_by_id(1),
    2: DiceType.get_by_id(2),
    3: DiceType.get_by_id(3),
    4: DiceType.get_by_id(4),
}

conversion_item_type = {
    1: DiceType.get_by_id(5),
    2: DiceType.get_by_id(6),
    3: DiceType.get_by_id(7),
    4: DiceType.get_by_id(8),
}
medallion_type = DiceType.get_by_id(9)

from business.race import Race
conversion_race = {
    'CORALELF': Race.get_by_id(1),
    'DWARF': Race.get_by_id(3),
    'GOBLIN': Race.get_by_id(4),
    'LAVAELF': Race.get_by_id(2),
    'AMAZON': Race.get_by_id(5),
    'FIREWALKER': Race.get_by_id(6),
    'UNDEAD': Race.get_by_id(7),
    'FERAL': Race.get_by_id(8),
    'SWAMPSTALKER': Race.get_by_id(9),
    'SCALDER': Race.get_by_id(11),
    'FROSTWING': Race.get_by_id(10),
    'TREEFOLK': Race.get_by_id(12),
    #All color of eldarim are eldarim
    'ELDARIM_WATER': Race.get_by_id(13),
    'ELDARIM_AIR': Race.get_by_id(13),
    'ELDARIM_FIRE': Race.get_by_id(13),
    'ELDARIM_EARTH': Race.get_by_id(13),
    'ELDARIM_DEATH': Race.get_by_id(13),
    'ELDARIM_WHITE': Race.get_by_id(13),
    #All color of dragonkin are dragonkin
    'RED': Race.get_by_id(14),
    'GOLD': Race.get_by_id(14),
    'GREEN': Race.get_by_id(14),
    'BLACK': Race.get_by_id(14),
    'BLUE': Race.get_by_id(14),
    #Make the color in the sky
}

item_race = Race.get_by_id(15)
medallion_race = Race.get_by_id(16)

from business.dice.dice_role import DiceRole as Role
conversion_minor_type = {
    'HEAVYMELEE': Role.get_by_name('Heavy Melee'),
    'LIGHTMELEE': Role.get_by_name('Light Melee'),
    'MISSILE': Role.get_by_name('Archer'),
    'CAVALRY': Role.get_by_name('Cavalry'),
    'MAGIC': Role.get_by_name('Mage'),
    'SKIRMISHER': Role.get_by_name('Cavalry'),
    'HEAVYMISSILE': Role.get_by_name('Heavy Archer'),
    'LIGHTMISSILE': Role.get_by_name('Archer'),
    'HEAVYMAGIC': Role.get_by_name('Mage'),
    'LIGHTMAGIC': Role.get_by_name('Mage Warrior'),
    'MONSTER': Role.get_by_name('Monster'),
    'MAGICITEMSAVE': Role.get_by_name('Magic Shield'),
    'MAGICITEMMANEUVER': Role.get_by_name('Magic Shoes'),
    'MAGICITEMMELEE': Role.get_by_name('Magic Sword'),
    'MAGICITEMMAGIC': Role.get_by_name('Magic Jewelry'),
    'MAGICITEMMISSILE': Role.get_by_name('Magic Arrow'),
    'CHAMPION': Role.get_by_name('Champion'),
    'ARTIFACTMELEE': Role.get_by_name('Artifact'),
    'ARTIFACTMISSILE': Role.get_by_name('Artifact'),
    'ARTIFACTSAVE': Role.get_by_name('Artifact'),
    'ARTIFACTMAGIC': Role.get_by_name('Artifact'),
    'ARTIFACTMANEUVER': Role.get_by_name('Artifact'),
    'SHIELDBEARER': Role.get_by_name('Shield Bearer'),
    'MEDALLION': Role.get_by_name('Medallion')
}

import MySQLdb as mdb
connection = mdb.connect(settings.db_host, settings.db_user, settings.db_password, 'dragon_dice_origin')

cursor = connection.cursor(mdb.cursors.DictCursor)
cursor.execute("SELECT a.*, b.Element_ID_1, b.Element_ID_2, c.Health from Dice as a LEFT JOIN Dice_Races as b ON a.Race_ID = b.Race_ID LEFT JOIN Dice_Rarities as c ON a.Rarity_ID = c.Rarity_ID WHERE  -(a.MajorType_ID = 'UNIT' OR a.majorType_ID = 'DRAGONKIN' OR a.MajorType_ID = 'MAGICITEM' OR a.MajorType_ID = 'ARTIFACT' OR a.MajorType_ID = 'MEDALLION') ORDER BY b.id ASC, c.health ASC, a.MinorType_ID ASC, a.name ASC")
dice_result = cursor.fetchall()
for dice_info in dice_result:
    if dice_info['MinorType_ID'] != 'NONE':
        role = conversion_minor_type[dice_info['MinorType_ID']]
        if dice_info['MajorType_ID'] == 'UNIT' or dice_info['MajorType_ID'] == 'DRAGONKIN':
            dice_type = conversion_unit_type[dice_info['Health']]
            race = conversion_race[dice_info['Race_ID']]
        elif dice_info['MajorType_ID'] == 'MAGICITEM' or dice_info['MajorType_ID'] == 'ARTIFACT':
            dice_type = conversion_item_type[dice_info['Health']]
            race = item_race
        else:
            dice_type = medallion_type
            race = medallion_race

        if race.break_by_color:
            #We remove the first element (it's alway a color and we neither need nor want it), and we reverse again
            name = dice_info['Name'].split(' ', 1)[1]
        else:
            name = dice_info['Name']

        #Dragonkin autosave
        if race.id == 14:
            autosave = dice_info['Health']
        else:
            autosave = 0

        dice = DiceTemplate(name, dice_info['Description'], dice_type, race, role, autosave=autosave)

        DBSession.add(dice)

        #Add color
        if (dice_info['Element_ID_1'] != 'NONE'):
            color1 = DiceElement(dice, conversion_color[dice_info['Element_ID_1']])
            DBSession.add(color1)
        if (dice_info['Element_ID_2'] != 'NONE'):
            color2 = DiceElement(dice, conversion_color[dice_info['Element_ID_2']])
            DBSession.add(color2)

        cursor.execute("SELECT * from Dice_Sides as a LEFT JOIN Dice_Faces as b ON a.Face_ID = b.Face_ID WHERE a.Die_ID = '"+dice_info['Die_ID']+"'")
        face_result = cursor.fetchall()
        faces = []
        for face_info in face_result:
            
            if face_info['Icon_ID'] == 'ID' and name == 'Wolf Pack':
                face = 'GroupID'
            else:
                face = conversion_icon[face_info['Icon_ID']]
            if face_info['Icon_ID'] == 'GALEFORCE' or face_info['Icon_ID'] == 'ILLUSION':
                amount = 1
            else:
                amount = face_info['Quantity']
            face = DiceFaceTemplate(dice, face_info['SideNumber'], conversion_icon[face_info['Icon_ID']], amount, face_info['Image'])
            faces.append(face)
            DBSession.add(face)
        DBSession.flush()
