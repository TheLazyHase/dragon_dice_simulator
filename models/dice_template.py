# -*- coding: utf-8 *-*
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
    Column('name', String(25)),
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
    from models import get_all, get_by_id
    from business.dice.dice_template import DiceTemplate
    from business.dice.dice_face_template import DiceFaceTemplate
    from business.dice.dice_element import DiceElement
    from business.dice.dice_type import DiceType
    from business.element import Element
    from business.race import Race
    from sqlalchemy.orm import mapper, relationship
    from sqlalchemy.ext.associationproxy import association_proxy

    DiceTemplate.get_all = classmethod(get_all)
    DiceTemplate.get_by_id = classmethod(get_by_id)

    mapper(DiceTemplate, dice_template_table, properties={
        'type': relationship(DiceType), 
        'race': relationship(Race), 
    })

    mapper(DiceFaceTemplate, dice_face_template_table, properties={
        'dice': relationship(DiceTemplate, backref='faces'), 
    })

    mapper(DiceElement, dice_element_table, properties={
        'dice': relationship(DiceTemplate, backref='element_links'), 
        'element': relationship(Element), 
    })

    DiceTemplate.elements = association_proxy('element_links', 'element')
