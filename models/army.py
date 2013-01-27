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

army_table = Table('army', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(25)),
    Column('position_id', Integer, ForeignKey('army_position.id'))
)


def army_mapper():
    from models import get_all, get_by_id, save, delete
    from business.army.army import Army
    from business.army.position import ArmyPosition
    from sqlalchemy.orm import mapper, relationship

    Army.get_all = classmethod(get_all)
    Army.get_by_id = classmethod(get_by_id)
    Army.save = save
    Army.delete = delete

    mapper(Army, army_table, properties={
        'position': relationship(ArmyPosition)
    })

