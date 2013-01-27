# -*- coding: utf-8 *-*
from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    )

from models import metadata, DBSession

army_position_table = Table('army_position', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('is_reserve', Boolean, default=False),
    Column('is_dead', Boolean, default=False),
    Column('is_buried', Boolean, default=False),
)

def position_mapper():
    from models import get_all, get_by_id, save, delete
    from business.army.position import ArmyPosition
    from sqlalchemy.orm import mapper, relationship

    ArmyPosition.get_all = classmethod(get_all)
    ArmyPosition.get_by_id = classmethod(get_by_id)
    ArmyPosition.save = save
    ArmyPosition.delete = delete

    mapper(ArmyPosition, army_position_table, properties={})
