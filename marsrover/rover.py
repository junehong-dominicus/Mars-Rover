from .position import Position

"""
Co-ordinates and Orientation.

        Ex) Plateau:5 5
 (5,0) (5,1) (5,2) (5,3) (5,4) (5,5)
 (4,0) (4,1) (4,2) (4,3) (4,4) (4,5)
 (3,0) (3,1) (3,2) (3,3) (3,4) (3,5)
 (2,0) (2,1) (2,2) (2,3) (2,4) (2,5)
 (1,0) (1,1) (1,2) (1,3) (1,4) (1,5)
 (0,0) (0,1) (0,2) (0,3) (0,4) (0,5)
"""
"""
           N = 1
             |
             |
 W = 4 ------+------ E = 2
             |
             |
           S = 3
turn_right: heading + 1
turn_left: heading - 1
"""

class Rover(object):
    AVAILABLE_COMMANDS = {
        'M': 'move',
        'L': 'turn_left',
        'R': 'turn_right',
    }

    DIRECTIONS = {
        'N': 1,
        'E': 2,
        'S': 3,
        'W': 4,
    }

    heading = DIRECTIONS['N']

    def __init__(self, plateau, position, heading):
        """
        Initializing mars rover with below params
        :param plateau:
        :param position:
        :param heading:
        """
        self.plateau = plateau
        self.position = position
        self.heading = heading

    def __str__(self):
        return self.current_position

    def set_position(self, x, y, heading):
        if not isinstance(self.position, Position):
            self.position = Position(x, y)
        else:
            self.position.x = x
            self.position.y = y

        self.heading = heading

    @property
    def current_position(self):
        return '{} {} {}'.format(self.position.x, self.position.y, self.get_heading)

    @property
    def get_heading(self):
        directions = list(self.DIRECTIONS.keys())

        try:
            direction = directions[self.heading - 1]
        except IndexError:
            direction = 'N'
            print('Direction error...')

        return direction

    def process(self, commands):
        for i in range(len(commands)):
            self.run_command(commands[i])

    def run_command(self, command):
        if 'L' == command:
            self.turn_left()
        elif 'R' == command:
            self.turn_right()
        elif 'M' == command:
            if not self.move():
                print("Where are you trying to go?")
        else:  # Unrecognized instruction
            print("Wrong parameters!..")

    def move(self):
        if not self.plateau.move_available(self.position):
            return False

        if self.DIRECTIONS['N'] == self.heading:
            self.position.y += 1
        elif self.DIRECTIONS['E'] == self.heading:
            self.position.x += 1
        elif self.DIRECTIONS['S'] == self.heading:
            self.position.y -= 1
        elif self.DIRECTIONS['W'] == self.heading:
            self.position.x -= 1

        return True

    def turn_left(self):
        self.heading = self.DIRECTIONS['W'] if (self.heading - 1) < self.DIRECTIONS['N'] else self.heading - 1

    def turn_right(self):
        self.heading = self.DIRECTIONS['N'] if (self.heading + 1) > self.DIRECTIONS['W'] else self.heading + 1
