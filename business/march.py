from business.army.army import Army
from business.army.roll import *

class March(object):
    #Opposing_army is supposed to be a list
    def __init__(self, active_army, opposing_army):
        self.active_army = active_army
        self.opposing_army = opposing_army

    def do_maneuver(self):
        self.active_army.roll(ManeuverRoll())

        print(self.active_army.result_description)
        print(self.active_army.effect_description)

        self.active_army.do_before_resolution_effect(self.opposing_army)

        print('%s maneuver obtained\r\n' % self.active_army.maneuver)

        pro_maneuver = self.active_army.maneuver
        con_maneuver = 0
        
        for army in self.opposing_army:
            army.roll(CounterManeuverRoll())

            print(army.result_description)
            print(army.effect_description)

            army.do_before_resolution_effect([self.active_army])

            print('counter : %s maneuver obtained\r\n' % army.maneuver)
            if (con_maneuver < army.maneuver):
                con_maneuver = army.maneuver

        if (pro_maneuver < con_maneuver):
            print('Maneuver failed !')
        else:
            print('Maneuver sucessed !')

