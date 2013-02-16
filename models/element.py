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
    Column,
    Integer,
    String,
    ForeignKey,
    )

from models import metadata, DBSession

element_table = Table('element', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(25)),
    Column('element_name', String(25)),
    Column('element_short_name', String(5))
)

def element_mapper():
    from models import get_all, get_by_id, save, delete
    from business.element import Element
    from sqlalchemy.orm import mapper, relationship

    Element.get_all = classmethod(get_all)
    Element.get_by_id = classmethod(get_by_id)
    Element.save = save
    Element.delete = delete

    mapper(Element, element_table, properties={})
