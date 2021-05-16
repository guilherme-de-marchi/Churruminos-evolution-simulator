from functools import reduce
from objects import members
from objects.object import Object
from simulationEnvironment.map import Map

class Churrumino(Object):
    def __init__(self, reproductive_organ: members.ReproductiveOrgan,
                        body: members.Body,
                        legs: members.Legs,
                        inclination: float,
                        char: str,
                        map: Map):
        '''
        args: inclination -> n in degrees
        '''

        assert isinstance(reproductive_organ, members.ReproductiveOrgan), 'arg: "reproductive_organ" must be a ReproductiveOrgan object'
        assert isinstance(body, members.Body), 'arg: "body" must be a Body object'
        assert isinstance(legs, members.Legs), 'arg: "legs" must be a Legs object'
        assert isinstance(inclination, (float, int)), 'arg: "inclination" must be a float or int object'

        super().__init__(char)

        self.reproductive_organ = reproductive_organ
        self.body = body
        self.legs = legs
        self.inclination = inclination

        self.WEIGHT = sum([member.WEIGHT for member in [
            self.reproductive_organ,
            self.body,
            self.legs
        ]])

        self.attractiveness = reduce(lambda a, b: a * b, self.reproductive_organ.SIZE) + self.legs.HEIGHT
        self.target = None

        self.map = map

    def walk(self, direction: tuple):
        '''
        arg: direction -> ([-1: left, 1: right], [-1: up, 1: down])
        '''

        assert isinstance(direction, tuple), 'arg: "direction" must be a tuple object'

        target_position = (self.position[0] + direction[0], self.position[1] + direction[1])
        self.map.moveTo(target_position, self)
        self.body.spendEnergy(self.WEIGHT / 4)

    def goTo(self, target: 'Object'):
        '''
        arg: target -> an "Object"
        '''

        assert(target, Object), 'arg: "target" must be an Object object'

        direction = []

        for n in range(len(self.position)):
            value = 0
            subtraction = self.position[n] - target.position[n]

            if subtraction:
                value = -subtraction / abs(subtraction)

            direction.append(int(value))
        
        return tuple(direction)

    def whatNeed(self):
        return 'food' if self.body.stored_energy <= self.body.ENERGY_STORAGE_CAPACITY / 2 else 'churrumino'
        
    def useTarget(self):
        what_need = self.whatNeed()

        if what_need == 'food':
            self.body.supplyEnergy(self.target)
            self.map.removeFrom(self.target.position, self.target)
        
        elif what_need == 'churrumino':
            self.target = None