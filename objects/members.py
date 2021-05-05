from functools import reduce
import objects.food
from objects.object import Object

class Member(Object):
    def __init__(self, size: tuple, weight: float):
        '''
        args: size -> (x, y, z) in meters
        weight -> n in Kg
        '''

        assert isinstance(size, tuple) and len(size) == 3, 'arg: "size" must be a tuple object with len 3'
        assert isinstance(weight, (float, int)), 'arg: "weight" must be a float or int object'
        
        super().__init__()

        self.SIZE = size
        self.WEIGHT = weight

class ReproductiveOrgan(Member):
    def __init__(self, size: tuple, weight: float):
        '''
        args: size -> (x, y, z) in meters
        weight -> n in Kg
        '''

        super().__init__(size, weight)

        self.MAXIMUM_GENERATION_CAPACITY = round(sum(self.SIZE) * 2)

    def generateDescendants(self) -> tuple:
        pass

class Body(Member):
    def __init__(self, size: tuple, weight: float, initial_energy: float):
        '''
        args: size -> (x, y, z) in meters
        weight -> n in Kg
        initial_energy -> n in cal
        '''

        super().__init__(size, weight)

        self.ENERGY_STORAGE_CAPACITY = round(sum(self.SIZE) * 100)
        self.stored_energy = initial_energy

    def supplyEnergy(self, food: 'Food'):
        assert isinstance(food, objects.food.Food)

        self.stored_energy += food.energy

    def spendEnergy(self, energy: float):
        assert isinstance(energy, (float, int)), 'arg: "energy" must be a float or int object'

        self.stored_energy -= energy

class Legs(Member):
    def __init__(self, size: tuple, weight: float):
        '''
        args: size -> (x, y: height, z) in meters
        weight -> n in Kg
        '''

        super().__init__(size, weight)

        self.HEIGHT = self.SIZE[1]
        self.MAXIMUM_SPEED = self.HEIGHT

class Eyes(Member):
    def __init__(self, size: tuple, weight: float):
        '''
        args: size -> (x, y, z) in meters
        weight -> n in Kg
        '''

        super().__init__(size, weight)

        self.VISION_RANGE = round(sum(self.SIZE) + 1)