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

dice_table = Table('dice', metadata,
    Column('id', Integer, primary_key=True),
    Column('nickname', String(50)),
    Column('army_id', Integer, ForeignKey('army.id')),
    Column('template_id', Integer, ForeignKey('dice_template.id'))
)


def dice_mapper():
    from models import get_all, get_by_id, save, delete
    from business.dice.dice import Dice
    from business.dice.dice_template import DiceTemplate
    from business.army.army import Army
    from sqlalchemy.orm import mapper, relationship

    Dice.get_all = classmethod(get_all)
    Dice.get_by_id = classmethod(get_by_id)
    Dice.save = save
    Dice.delete = delete

    mapper(Dice, dice_table, properties={
        'army': relationship(Army, backref='components'),
        'template': relationship(DiceTemplate),
    })

