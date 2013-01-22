#Base class
class Roll(object):
    @property   
    def is_avoidance(self):
        return False

    @property   
    def is_melee(self):
        return False

    @property   
    def is_missile(self):
        return False

    @property   
    def is_maneuver(self):
        return False

    @property   
    def is_magic(self):
        return False

    @property   
    def is_save(self):
        return False

    @property   
    def is_counter(self):
        return False

    #mixed refere to roll where different icon are required and provide the same effect
    @property   
    def is_combined(self):
        return False

    #mixed refere to roll where different icon are required and provide different effects
    @property   
    def is_mixed(self):
        return False

    @property   
    def main_icon(self):
        return None

    @property   
    def allowed_icon(self):
        return [self.main_icon]

    @property   
    def is_dragon(self):
        return False

#Regular roll
from business.army.roll.melee import MeleeRoll
from business.army.roll.counter_melee import CounterMeleeRoll
from business.army.roll.missile import MissileRoll
from business.army.roll.maneuver import ManeuverRoll
from business.army.roll.counter_maneuver import CounterManeuverRoll
from business.army.roll.magic import MagicRoll

#Avoidance roll
from business.army.roll.melee_avoidance import MeleeAvoidanceRoll
from business.army.roll.maneuver_avoidance import ManeuverAvoidanceRoll
from business.army.roll.save_avoidance import SaveAvoidanceRoll

#Special roll
from business.army.roll.dragon import DragonRoll

#Spell-specific roll
from business.army.roll.tidal_wave import TidalWaveRoll
