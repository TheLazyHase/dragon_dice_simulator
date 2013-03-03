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

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from business.user.root import Root, groupfinder

if __name__ == '__main__':
    auth_policy = ACLAuthorizationPolicy()
    authentication_policy = AuthTktAuthenticationPolicy('secrets', hashalg='sha512', callback=groupfinder)

    config = Configurator(
        authentication_policy=authentication_policy,
        authorization_policy=auth_policy,
        root_factory=Root
    )

    #SQLAlchemy stuff
    from models import (
        DBSession,
        metadata
    )

    from sqlalchemy import create_engine
    import settings
    engine = create_engine('mysql+mysqldb://'+settings.db_user+':'+settings.db_password+'@'+settings.db_host+'/'+settings.db_name)
    DBSession.configure(bind=engine)
    metadata.bind = engine

    import models

    #Add route here
    config.add_route('authentication', '/authenticate')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

    config.add_route('army_selection', '/army/selection', request_method="GET")
    config.add_route('do_army_selection', '/army/selection', request_method="POST")
    config.add_route('army_creation', '/army/new', request_method="POST")
    config.add_route('army_edition', '/army/{id:[0-9]+}/edition', request_method="GET")
    config.add_route('army_edition_alias', '/army/edition', request_method="GET")
    config.add_route('do_army_edition', '/army/{id:[0-9]+}/edition', request_method="POST")

    config.add_route('unit_view', '/unit/{id:[0-9]+}', request_method="GET")

    config.add_route('initiate_save_action', '/action/save', request_method="POST")
    config.add_route('save_action', '/action/save/{id:[0-9]+}')
    config.add_route('save_action_step_one', '/action/save/{id:[0-9]+}/step/1', request_method="GET")
    config.add_route('save_action_step_two', '/action/save/{id:[0-9]+}/step/2', request_method="GET")

    config.add_route('dragon_roll', '/army/{id:[0-9]+}/roll/dragon', request_method="GET")
    config.add_route('melee_roll', '/army/{id:[0-9]+}/roll/melee', request_method="GET")
    config.add_route('missile_roll', '/army/{id:[0-9]+}/roll/missile', request_method="GET")
    config.add_route('maneuver_roll', '/army/{id:[0-9]+}/roll/maneuver', request_method="GET")
    config.add_route('save_melee_roll', '/army/{id:[0-9]+}/roll/melee_save', request_method="GET")
    config.add_route('save_missile_roll', '/army/{id:[0-9]+}/roll/missile_save', request_method="GET")

    #Scan for route
    config.scan('controller')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
