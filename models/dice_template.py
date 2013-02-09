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

dice_template_table = Table('dice_template', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('race_id', Integer, ForeignKey('race.id')),
    Column('type_id', Integer, ForeignKey('dice_type.id')),
    Column('description', String(200)),
    Column('automelee', Integer),
    Column('automissile', Integer),
    Column('automaneuver', Integer),
    Column('automagic', Integer),
    Column('autosave', Integer)
)

dice_face_template_table = Table('dice_face_template', metadata,
    Column('id', Integer, primary_key=True),
    Column('dice_id', Integer, ForeignKey('dice_template.id')),
    Column('side_number', Integer),
    Column('class_name', String(25)),
    Column('amount', Integer),
    Column('picture', String(100))
)

dice_element_table = Table('dice_element', metadata,
    Column('id', Integer, primary_key=True),
    Column('dice_id', Integer, ForeignKey('dice_template.id')),
    Column('element_id', Integer, ForeignKey('element.id'))
)

def dice_template_mapper():
    from models import get_all, get_by_id, save, delete
    from business.dice.dice_template import DiceTemplate
    from business.dice.dice_face_template import DiceFaceTemplate
    from business.dice.dice_element import DiceElement
    from business.dice.dice_type import DiceType
    from business.element import Element
    from business.race import Race
    from sqlalchemy.orm import mapper, relationship, backref
    from sqlalchemy.ext.associationproxy import association_proxy

    DiceTemplate.get_all = classmethod(get_all)
    DiceTemplate.get_by_id = classmethod(get_by_id)
    DiceTemplate.save = save
    DiceTemplate.delete = delete

    mapper(DiceTemplate, dice_template_table, properties={
        'type': relationship(DiceType), 
        'race': relationship(Race, backref='dices'), 
    })

    mapper(DiceFaceTemplate, dice_face_template_table, properties={
        'dice': relationship(DiceTemplate, backref=backref('faces', order_by=dice_face_template_table.c.side_number)), 
    })

    mapper(DiceElement, dice_element_table, properties={
        'dice': relationship(DiceTemplate, backref='element_links'), 
        'element': relationship(Element), 
    })

    DiceTemplate.elements = association_proxy('element_links', 'element')
