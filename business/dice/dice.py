from random import choice

from face import Face

class Dice(object):
    def __init__(self, title, race, faces, health, elements, autosave=0, automelee=0, automissile=0, automaneuver=0, automagic=0):
        self.active_faces = None
        self.race = race
        self.faces = faces
        self.title = title
        self.health = health
        self.elements = elements
        self.id = 0

        self.autoresult = {
            Face.ICON_MELEE: automelee,
            Face.ICON_MISSILE: automissile,
            Face.ICON_MANEUVER: automaneuver,
            Face.ICON_MAGIC: automagic,
            Face.ICON_SAVE: autosave,
        }

    def roll(self, type_roll):
        self.active_faces = []

        active_face = choice(self.faces)
        active_face.type_roll = type_roll
        self.active_faces.append(active_face)
        #Reroll ? (rend, for example)
        while(active_face.is_rerolled):
            active_face = choice(self.faces)
            active_face.type_roll = type_roll
            self.active_faces.append(active_face)
        return self

    @property
    def name(self):
        return "%s %s (#%s, %s health, %s)" % (self.race.name, self.title, self.id, self.health, '/'.join([element.name for element in self.elements]))

    @property
    def description(self):
        description_list = []
        for face in self.faces:
            description_list.append('<img src="http://www.sfr-inc.com/'+face.picture+'" /> '+face.name)
        return self.name+"<br />"+"<br />".join(description_list)

    @property
    def result_description(self):
        description = []
        for active_face in self.active_faces:
            description.append(active_face.name)
        return ('%s : ' % self.name)+' ; '.join(description)

    def get_result(self, icon_type, result_type = None):
        result = 0
        if (result_type == None or result_type == Face.TYPE_NORMAL):
            result += self.autoresult[icon_type]
        for active_face in self.active_faces:
            if (result_type == None or result_type == active_face.type):
                result += active_face.icon_by_type(icon_type)
        if (result < 0):
            result = 0
        return result

    def get_melee(self, result_type = None):
        return self.get_result(Face.ICON_MELEE)

    def get_missile(self, result_type = None):
        return self.get_result(Face.ICON_MISSILE)

    def get_maneuver(self, result_type = None):
        return self.get_result(Face.ICON_MANEUVER)

    def get_magic(self, result_type = None):
        return self.get_result(Face.ICON_MAGIC)

    def get_save(self, result_type = None):
        return self.get_result(Face.ICON_SAVE)

    @property
    def special_effect(self):
        effect = []
        for active_face in self.active_faces:
            if (active_face.special_effect != None):
                effect.append(active_face.special_effect)
        return effect
