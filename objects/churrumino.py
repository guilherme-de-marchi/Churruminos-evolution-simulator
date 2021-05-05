from functools import reduce
from objects import members
from objects.object import Object

class Churrumino(Object):
    def __init__(self, reproductive_organ: 'ReproductiveOrgan',
                        body: 'Body',
                        legs: 'Legs',
                        eyes: 'Eyes',
                        inclination: float):
        '''
        args: inclination -> n in degrees
        '''

        assert isinstance(reproductive_organ, members.ReproductiveOrgan), 'arg: "reproductive_organ" must be a ReproductiveOrgan object'
        assert isinstance(body, members.Body), 'arg: "body" must be a Body object'
        assert isinstance(legs, members.Legs), 'arg: "legs" must be a Legs object'
        assert isinstance(eyes, members.Eyes), 'arg: "eyes" must be an Eyes object'
        assert isinstance(inclination, (float, int)), 'arg: "inclination" must be a float or int object'

        super().__init__()

        self.reproductive_organ = reproductive_organ
        self.body = body
        self.legs = legs
        self.eyes = eyes
        self.inclination = inclination

        self.ENERGY_EXPENDITURE_PER_MOVIMENT = sum([member.WEIGHT for member in [
            self.reproductive_organ,
            self.body,
            self.legs,
            self.eyes
        ]])

        self.attractiveness = reduce(lambda a, b: a * b, self.reproductive_organ.SIZE) + self.legs.HEIGHT