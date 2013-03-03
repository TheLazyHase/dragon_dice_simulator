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

from pyramid.view import view_config,forbidden_view_config
from pyramid.security import remember, forget
from controller import BaseController

from pyramid.httpexceptions import HTTPFound

from business.user import User

class ArmiesController(BaseController):
    @view_config(route_name='authentication')
    def authentication(self):
        user_id = int(self.request.POST['id'])
        user = User(user_id)
        headers = remember(self.request, user.id)
        url = self.request.route_url('army_selection')
        return HTTPFound(location=url, headers = headers)

    @view_config(route_name='login', renderer='controller.user:templates/login.mako')
    @forbidden_view_config(renderer='controller.user:templates/failed_login.mako')
    def login(self):
        return {'authentication_route': self.request.route_url('authentication'), 'user_ids': range(5)}

    @view_config(route_name='logout')
    def logout(self):
        headers = forget(self.request, user.id)
        url = self.request.route_url('login')
        return HTTPFound(location=url, headers = headers)
