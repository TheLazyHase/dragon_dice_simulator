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

from pyramid.events import subscriber
from pyramid.events import NewRequest

def cleanup_callback(request):
    from models import DBSession
    DBSession.flush()
    DBSession.remove()

@subscriber(NewRequest)
def add_cleanup_callback(event):
    event.request.add_finished_callback(cleanup_callback)

class BaseController(object):

    def __init__(self, request):
        self.request = request
