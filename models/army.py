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

