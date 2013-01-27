from pyramid.view import view_config
from controller import BaseController

from business.army.army import Army
from business.army.position import ArmyPosition
from business.dice.dice import Dice
from business.dice.dice_template import DiceTemplate
from business.race import Race

import re

class ArmiesController(BaseController):
    @view_config(route_name='army_selection', renderer='controller.army:templates/selection.mako')
    def army_selection(self):
        army_list = Army.get_all()
        if (len(army_list) > 0):
            return_value = {'existing': True, 'choices': [{'id': army.id, 'name': army.name} for army in Army.get_all()]}
        else:
            return_value = {'existing': False}
        return return_value

    @view_config(route_name='army_creation', renderer='controller.army:templates/edition.mako')
    def do_army_creation(self):
        army_position = ArmyPosition.get_by_id(1)
        army = Army(army_position)
        army.name = self.request.POST['army_name']
        army.save()
        return army_edition(army, ('Army named %s succesfully created !' % army.name)

    @view_config(route_name='army_edition', renderer='controller.army:templates/edition.mako')
    @view_config(route_name='army_edition_alias', renderer='controller.army:templates/edition.mako')
    def army_edition(self, army=None, special_message=''):
        if (army == None):
            army = Army.get_by_id(self.request.matchdict.get('id'), self.request.GET['chosen_army'])
        dice_list = [{'id': dice.id, 'name': dice.title} for dice in army.components]
        template_list = [{'id': dice_template.id, 'name': dice_template.name, 'picture': dice_template.picture} for dice_template in DiceTemplate.get_all()]
        return {'special_message': special_message, 'templates': template_list, 'dices': dice_list, 'army_id': army.id}

    @view_config(route_name='do_army_edition', renderer='controller.army:templates/edition.mako')
    def do_army_edition(self, army=None, special_message=''):
        army = Army.get_by_id(self.request.matchdict.get('id'))

        removed_dice_id_list = self.request.POST['unit_to_remove']
        for dice_id in removed_dice_id_list:
            del Dice.get_by_id(int(dice_id))
        #Ugly, but how to do otherwise ?
        regexp = re.compile('^unit_amount_([1-9][0-9]{1-2})$')
        for element, amount in self.request.POST.items():
            m = regexp.match(element)
            if ((m != None) and (int(amount) > 0)):
                for i in range(1,int(amount)):
                    dice = Dice(DiceTemplate.get_by_id(m.group(1)), army)
                    dice.save()
        return army_edition(army, ('army %s succesfully modified !' % army.name)
