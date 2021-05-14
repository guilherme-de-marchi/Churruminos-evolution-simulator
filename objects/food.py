from objects.object import Object

class Food(Object):
    def __init__(self, stored_energy: float, char: str):
        '''
        args: stored_energy -> n in cal
        '''

        assert isinstance(stored_energy, (float, int)), 'arg: "stored_energy" must be a float or int object'

        super().__init__(char)

        self.stored_energy = stored_energy