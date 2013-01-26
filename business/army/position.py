class ArmyPosition(object):
    def __init__(self, name, is_reserve=False, is_dead=False, is_buried=False):
        self.name = name
        self.is_reserve = is_reserve
        self.is_dead = is_dead
        self.is_buried = is_buried

