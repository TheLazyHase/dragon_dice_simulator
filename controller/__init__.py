# -*- coding: utf-8 *-*

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
