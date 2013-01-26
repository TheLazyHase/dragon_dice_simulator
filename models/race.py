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

race_table = Table('race', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('racial_class', String(25)),
    Column('tag', String(5))
)

def race_mapper():
    from models import get_all, get_by_id, save
    from business.race import Race
    from sqlalchemy.orm import mapper, relationship

    Race.get_all = classmethod(get_all)
    Race.get_by_id = classmethod(get_by_id)
    Race.save = save

    mapper(Race, race_table, properties={})
