from objects.object import Object

class Food:
    def __init__(self, stored_energy: float):
        '''
        args: stored_energy -> n in cal
        '''

        assert isinstance(stored_energy, (float, int)), 'arg: "stored_energy" must be a float or int object'

        super().__init__()