from pyramid.view import view_config
from controller import BaseController
from business.army.army import Army
from business.army.position import ArmyPosition

class ArmiesController(BaseController):
    @view_config(route_name='army_selection', renderer='controller.army:templates/selection.mako')
    def army_selection(self):
        army_list = Army.get_all()
        if (len(army_list) > 0):
            return_value = {'existing': True, 'choices': ('\r\n'.join(['<option value="%s">%s</option>' % (army.id, army.name) for army in Army.get_all()]))}
        else:
            return_value = {'existing': False}
        return return_value

    @view_config(route_name='army_creation', renderer='controller.army:templates/new.mako')
    def army_creation(self):
        army_position = ArmyPosition.get_by_id(1)
        army = Army(army_position)
        army.save()
        army.name = self.request.POST['army_name']
        return {'name': army.name}

    @view_config(route_name='army_modification', renderer='controller.army:templates/creation.mako')
    def do_army_creation(self):
        from business.dice.dice_template import DiceTemplate
        return {'name': "<hr />".join([dice_template.title+dice_template.face_description for dice_template in DiceTemplate.get_all()]), 'failed_attempt': True}
