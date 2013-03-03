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

game_table = Table('game', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(25))
)

game_player_table = Table('game_player', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(25)),
    Column('game_id', Integer, ForeignKey('game.id')),
    Column('buried_army_id', Integer, ForeignKey('army.id')),
    Column('dead_army_id', Integer, ForeignKey('army.id')),
    Column('reserve_army_id', Integer, ForeignKey('army.id')),
    Column('summon_army_id', Integer, ForeignKey('army.id')),
)

game_player_armies_table = Table('player_armies', metadata,
    Column('player_id', Integer, ForeignKey('game_player.id')),
    Column('army_id', Integer, ForeignKey('army.id'))
)


def game_mapper():
    from models import get_all, get_by_id, get_by_name, save, delete
    from business.army.army import Army
    from business.game import Game
    from business.game.player import PlayerGame
    from sqlalchemy.orm import mapper, relationship, backref

    Game.get_all = classmethod(get_all)
    Game.get_by_id = classmethod(get_by_id)
    Game.save = save
    Game.delete = delete

    mapper(Game, game_table, properties={})

    PlayerGame.get_all = classmethod(get_all)
    PlayerGame.get_by_id = classmethod(get_by_id)
    PlayerGame.get_by_name = classmethod(get_by_name)
    PlayerGame.save = save
    PlayerGame.delete = delete

    mapper(PlayerGame, game_player_table, properties={
        'game': relationship(Game),
        'buried_army': relationship(Army, foreign_keys=[game_player_table.c.buried_army_id]),
        'dead_army': relationship(Army, foreign_keys=[game_player_table.c.dead_army_id]),
        'reserve_army': relationship(Army, foreign_keys=[game_player_table.c.reserve_army_id]),
        'summon_army': relationship(Army, foreign_keys=[game_player_table.c.summon_army_id]),
        'armies': relationship(Army, secondary=game_player_armies_table, backref=backref('owner', uselist=False))
    })

