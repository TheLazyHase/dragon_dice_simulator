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

element_table = Table('element', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(25)),
    Column('element_name', String(25))
)

def element_mapper():
    from models import get_all, get_by_id
    from business.element import Element
    from sqlalchemy.orm import mapper, relationship

    Element.get_all = classmethod(get_all)
    Element.get_by_id = classmethod(get_by_id)

    mapper(Element, element_table, properties={})
