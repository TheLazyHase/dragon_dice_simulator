from pyramid.view import view_config
from controller import BaseController

class ArmyCreationController(BaseController):
    @view_config(route_name='army_creation', renderer='controller.army:templates/creation.mako')
    def army_creation(self):
        from business.dice.dice_template import DiceTemplate
        return {'name': "<hr />".join([dice_template.get_instance().description for dice_template in DiceTemplate.get_all()]), 'failed_attempt': True}
