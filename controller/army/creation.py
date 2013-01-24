from pyramid.view import view_config
from controller import BaseController

class ArmyCreationController(BaseController):
    @view_config(route_name='army_creation', renderer='controller.army:templates/creation.mako')
    def army_creation(self):
        return {'name': 'test1', 'failed_attempt': True}
