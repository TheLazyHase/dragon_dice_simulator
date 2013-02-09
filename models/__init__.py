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

def save(self, explicit=False):
    DBSession.add(self)
    if explicit:
        DBSession.flush()
    return self

def delete(self, explicit=False):
    DBSession.delete(self)
    if explicit:
        DBSession.flush()
    del self

from models.element import element_mapper
element_mapper()

from models.race import race_mapper
race_mapper()

from models.dice_type import dice_type_mapper
dice_type_mapper()

from models.dice_template import dice_template_mapper
dice_template_mapper()

from models.army import army_mapper
army_mapper()

from models.position import position_mapper
position_mapper()

from models.dice import dice_mapper
dice_mapper()

