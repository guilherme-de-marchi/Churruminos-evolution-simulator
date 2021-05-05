class Map:
    def __init__(self, size: tuple, default: list = None):
        '''
        args: size -> (width, height)
        default -> [
            [n, n, n, n, ...],
            [n, n, n, n, ...],
            [n, n, n, n, ...],
            ...
        ]
        '''

        assert isinstance(size, tuple), 'arg: "size" must be a tuple object'
        if default:
            assert isinstance(default, list), 'arg: "default" must be a list object'

            self.map = default
        
        else:
            self.map = [[None for x in range(size[0])] for y in range(size[1])]

        self.SIZE = (len(self.map[0]), len(self.map))

    def validatePosition(self, position: tuple) -> bool:
        '''
        args: position -> (width, height)
        '''

        assert isinstance(position, tuple), 'arg: "position" must be a tuple object'

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

        self.setPosition(target_position, target_object)
        self.map[target_object.position[1]][target_object.position[0]].remove(target_object)