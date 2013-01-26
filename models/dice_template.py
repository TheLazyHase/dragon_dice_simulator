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
    Column('race', String(5)),
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


#insert into dice_template (name, race) VALUES ('Advocate', 'fw'), ('Destroyer', 'fw');
#insert into dice_face_template (dice_id, side_number, class_name, amount) VALUES (1, 1, 'ID', 1), (1, 2, 'Melee', 2), (1, 3, 'Melee', 1), (1, 4, 'Fly', 1), (1, 5, 'Melee', 1), (1, 6, 'Maneuver', 1);
#insert into dice_face_template (dice_id, side_number, class_name, amount) VALUES (2, 1, 'ID', 1), (2, 2, 'Missile', 2), (2, 3, 'Melee', 1), (2, 4, 'Fly', 1), (2, 5, 'Missile', 1), (2, 6, 'Save', 1);

def dice_template_mapper():
    from models import get_all
    from business.dice.dice_template import DiceTemplate
    from business.dice.dice_face_template import DiceFaceTemplate
    from sqlalchemy.orm import mapper, relationship

    DiceTemplate.get_all = classmethod(get_all)

    mapper(DiceTemplate, dice_template_table)

    mapper(DiceFaceTemplate, dice_face_template_table, properties={
        'dice': relationship(DiceTemplate, backref='face_list'), 
    })
