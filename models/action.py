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

action_table = Table('action', metadata,
    Column('id', Integer, primary_key=True),
    Column('type', Integer, nullable=False),
    Column('game_id', Integer, ForeignKey('game.id')),
    Column('army_id', Integer, ForeignKey('army.id')),
    Column('step', Integer)
)

save_action_table = Table('save_action', metadata,
    Column('action_id', Integer, ForeignKey('action.id'), primary_key=True),
    Column('damage', Integer)
)


def action_mapper():
    from models import get_all, get_by_id, save, delete
    from business.game.action import Action
    from business.game import Game
    from business.army.army import Army
    from sqlalchemy.orm import mapper, relationship, backref

    Action.get_all = classmethod(get_all)
    Action.get_by_id = classmethod(get_by_id)
    Action.save = save
    Action.delete = delete

    mapper(Action, action_table, properties={
        'game': relationship(Game, backref='current_action'),
        'army': relationship(Army, backref=backref('current_action', uselist=False))
    }, polymorphic_on=action_table.c.type, polymorphic_identity=0)

    from business.game.action.save import SaveAction

    mapper(SaveAction, save_action_table, inherits=Action, polymorphic_identity=1)
