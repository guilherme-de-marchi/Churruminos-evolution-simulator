class Object:
    def __init__(self, char: str):
        self.char = char
        self.position = (None, None)

    def updatePosition(self, target_position: tuple):
        '''
        args: target_position -> (x, y)
        '''

        assert isinstance(target_position, tuple), 'arg: "target_position" must be a tuple object'

        self.position = target_position