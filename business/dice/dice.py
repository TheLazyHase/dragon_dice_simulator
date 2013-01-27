from random import choice

from face import Face

from sqlalchemy.orm import reconstructor

class Dice(object):
    def __init__(self, template, army, nickname=''):
        self.active_faces = None
        self.nickname = nickname
        self.template = template
        self.army = army
        self.id = 0
        self.hydrate()

    @reconstructor
    def hydrate(self):
        self.faces = self.template.get_instancied_faces()
        self.autoresult = {
            Face.ICON_MELEE: self.template.automelee,
            Face.ICON_MISSILE: self.template.automissile,
            Face.ICON_MANEUVER: self.template.automaneuver,
            Face.ICON_MAGIC: self.template.automagic,
            Face.ICON_SAVE: self.template.autosave,
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
        if self.nickname != '':
            name = self.nickname+' ,'+self.template.name
        else:
            name = self.template.name
        return name

    @property
    def health(self):
        return self.template.type.health

    @property
    def race(self):
        return self.template.race

    @property
    def elements(self):
        return self.template.elements

    @property
    def description(self):
        return self.name+self.template.face_description

    @property
    def result_description(self):
        description = []
        for active_face in self.active_faces:
            description.append(active_face.name)
        return ('%s : ' % self.name)+' ; '.join(description)

    def get_result(self, icon_type, result_type = None):
        result = 0
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
