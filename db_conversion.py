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
    'FLY': 'Fly',
    'BULLSEYE': 'Bullseye',
    'CANTRIP': 'Cantrip',
    'DOUBLE_STRIKE': 'DoubleStrike',
    'FROST_BREATH': 'FrostBreath',
    'HOWL': 'Howl',
    'REND': 'Rend',
    'SMITE': 'Smite',
    'SWALLOW': 'Swallow',
    'SURPRISE': 'Surprise',
    'VOLLEY': 'Volley',
}

from business.element import Element
conversion_color = {
    'WATER': Element.get_by_id(3),
    'AIR': Element.get_by_id(1),
    'EARTH': Element.get_by_id(4),
    'FIRE': Element.get_by_id(2),
    'DEATH': Element.get_by_id(5),
    'IVORY': Element.get_by_id(6),
    'WHITE': Element.get_by_id(7),
}

from business.dice.dice_type import DiceType
conversion_type = {
    1: DiceType.get_by_id(1),
    2: DiceType.get_by_id(2),
    3: DiceType.get_by_id(3),
    4: DiceType.get_by_id(4),
}

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

import MySQLdb as mdb
connection = mdb.connect(settings.db_host, settings.db_user, settings.db_password, 'dragon_dice_origin')



cursor = connection.cursor(mdb.cursors.DictCursor)
cursor.execute("SELECT a.*, b.Element_ID_1, b.Element_ID_2, c.Health from Dice as a LEFT JOIN Dice_Races as b ON a.Race_ID = b.Race_ID LEFT JOIN Dice_Rarities as c ON a.Rarity_ID = c.Rarity_ID WHERE a.race_ID = 'FROSTWING' AND a.MajorType_ID = 'UNIT' ORDER BY c.health ASC, a.MinorType_ID ASC, a.name ASC")
dice_result = cursor.fetchall()
for dice_info in dice_result:
    dice = DiceTemplate(dice_info['Name'], dice_info['Description'], conversion_type[dice_info['Health']], conversion_race[dice_info['Race_ID']])

    DBSession.add(dice)

    #Add color
    if (dice_info['Element_ID_1'] != 'None'):
        color1 = DiceElement(dice, conversion_color[dice_info['Element_ID_1']])
        DBSession.add(color1)
    if (dice_info['Element_ID_2'] != 'None'):
        color2 = DiceElement(dice, conversion_color[dice_info['Element_ID_2']])
        DBSession.add(color2)

    cursor.execute("SELECT * from Dice_Sides as a LEFT JOIN Dice_Faces as b ON a.Face_ID = b.Face_ID WHERE a.Die_ID = '"+dice_info['Die_ID']+"'")
    face_result = cursor.fetchall()
    faces = []
    for face_info in face_result:
        face = DiceFaceTemplate(dice, face_info['SideNumber'], conversion_icon[face_info['Icon_ID']], face_info['Quantity'], face_info['Image'])
        faces.append(face)
        DBSession.add(face)
    DBSession.flush()
