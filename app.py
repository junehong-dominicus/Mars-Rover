import sys

from marsrover import Plateau
from marsrover import Position
from marsrover import Rover
from hashmap import HashMap
from instruction_parser import InstructionParser

def main():
    plateau = None
    rover_table = HashMap()
    parser = InstructionParser()
    n = len(sys.argv)
    if n == 2:  # Check if input filename is passsed.
        input_file = open(sys.argv[1], 'r')
        Lines = input_file.readlines()
        for line in Lines:
            parameter, rovername, command, values = parser.parse_instruntion(line)
            if parameter == "Plateau":
                if plateau is None: # Initializing Plateau
                    plateau = Plateau(ord(values[0])-ord('0'), ord(values[1])-ord('0'))
                else:
                    print("Plateau is already set")
            else: # Landing / Instructions
                if plateau is None:
                    print("Plateau is not set")
                    continue
                if command == "Landing":
                    position = Position(ord(values[0])-ord('0'), ord(values[1])-ord('0'))
                    rover = Rover(plateau, position, Rover.DIRECTIONS.get(values[2]))
                    rover_table.add(rovername, rover)
                elif command == "Instructions":
                    rover = rover_table.get(rovername)
                    if rover is not None: # Check Landing position or previous position
                        rover.process(values[0])
                        rover_table.add(rovername, rover)
                        print(rovername + ":" + str(rover))
                    else:
                        print("No landing data")
                else: # Unrecognized parameter
                    print("Wrong Rover parameters")
    else:
        print("Wrong argument")

if __name__ == "__main__":
    main()
