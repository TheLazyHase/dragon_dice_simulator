# -*- coding: utf-8 *-*
from sqlalchemy import (
    MetaData,
    Table,
    Column
    )

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

#from zope.sqlalchemy import ZopeTransactionExtension

#DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
DBSession = scoped_session(sessionmaker())

metadata = MetaData()

def get_all(cls):
    return DBSession.query(cls).order_by(cls.id).all()

def get_by_id(cls, id):
    return DBSession.query(cls).get(id)

from models.element import element_mapper
element_mapper()

from models.race import race_mapper
race_mapper()

from models.dice_type import dice_type_mapper
dice_type_mapper()

from models.dice_template import dice_template_mapper
dice_template_mapper()

