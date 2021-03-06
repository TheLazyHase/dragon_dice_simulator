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

from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
    )

from models import metadata, DBSession

dice_table = Table('dice', metadata,
    Column('id', Integer, primary_key=True),
    Column('nickname', String(50)),
    Column('army_id', Integer, ForeignKey('army.id')),
    Column('template_id', Integer, ForeignKey('dice_template.id'))
)

dice_active_face_table = Table('dice_active_face', metadata,
    Column('id', Integer, primary_key=True),
    Column('dice_id', Integer, ForeignKey('dice.id')),
    Column('dice_face_template_id', Integer, ForeignKey('dice_face_template.id'))
)


def dice_mapper():
    from models import get_all, get_by_id, save, delete
    from business.dice.dice import Dice
    from business.dice.dice_template import DiceTemplate
    from business.dice.dice_face_template import DiceFaceTemplate
    from business.army.army import Army
    from sqlalchemy.orm import mapper, relationship

    Dice.get_all = classmethod(get_all)
    Dice.get_by_id = classmethod(get_by_id)
    Dice.save = save
    Dice.delete = delete

    mapper(Dice, dice_table, properties={
        'army': relationship(Army, backref='components'),
        'template': relationship(DiceTemplate),
        'active_faces': relationship(DiceFaceTemplate, secondary=dice_active_face_table)
    })

