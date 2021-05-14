class Map:
    def __init__(self, size: tuple, void_char: 'str'):
        '''
        args: size -> (width, height)
        '''

        assert isinstance(size, tuple), 'arg: "size" must be a tuple object'
        assert isinstance(void_char, str), 'arg: "void_char" must be a str object'
        
        self.map = [[[] for x in range(size[0])] for y in range(size[1])]
        self.SIZE = size
        self.void_char = void_char

    def validatePosition(self, position: tuple) -> bool:
        '''
        args: position -> (width, height)
        '''

        assert isinstance(position, tuple), 'arg: "position" must be a tuple object'

        if position[0] < 0 or position[1] < 0:
            return False

        try:
            test = self.map[position[1]][position[0]]
            return True

        except IndexError:
            return False

    def getPosition(self, position: tuple):
        '''
        args: position -> (width, height)
        '''

        assert isinstance(position, tuple), 'arg: "position" must be a tuple object'

        if self.validatePosition(position):
            return self.map[position[1]][position[0]]

        raise IndexError('invalid position')

    def setPosition(self, target_position: tuple, target_object: 'Object'):
        '''
        args: position -> (width, height)
        '''

        assert isinstance(target_position, tuple), 'arg: "target_position" must be a tuple object'

        if self.validatePosition(target_position):
            self.map[target_position[1]][target_position[0]].append(target_object)
            target_object.updatePosition(target_position)

    def moveTo(self, target_position: tuple, target_object: 'Object'):
        '''
        args: position -> (width, height)
        '''

        assert isinstance(target_position, tuple), 'arg: "target_position" must be a tuple object'

        if self.validatePosition(target_position):
            self.map[target_object.position[1]][target_object.position[0]].remove(target_object)
            self.setPosition(target_position, target_object)

    def render(self):
        return [[column[-1].char if len(column) else self.void_char for column in row] for row in self.map]

    def __str__(self):
        return '\n'.join([str(row) for row in self.map])
