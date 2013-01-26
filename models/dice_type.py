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

dice_type_table = Table('dice_type', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(25)),
    Column('health', Integer),
    Column('cost', Integer)
)

def dice_type_mapper():
    from models import get_all, get_by_id
    from business.dice.dice_type import DiceType
    from sqlalchemy.orm import mapper, relationship

    DiceType.get_all = classmethod(get_all)
    DiceType.get_by_id = classmethod(get_by_id)

    mapper(DiceType, dice_type_table, properties={})
