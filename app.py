import sys

from marsrover import Plateau
from marsrover import Position
from marsrover import Rover
from hashmap import HashMap

def main():
    plateau = None
    rover_table = HashMap()
    n = len(sys.argv)
    if n == 2:  # Check if input filename is passsed. 
        input_file = open(sys.argv[1], 'r')
        Lines = input_file.readlines()
        for line in Lines:
            received_data = line.strip().split(":")
            if len(received_data) < 2:  # Check if Line has Parameter and Values.
                continue

            if received_data[0] == "Plateau":
                if plateau is None: # Initializing Plateau
                    received_values = received_data[1].split(" ")
                    plateau = Plateau(ord(received_values[0])-ord('0'), ord(received_values[1])-ord('0'))
                else:
                    print("Plateau is already set")
            else:
                if plateau is None:
                    print("Plateau is not set")
                    continue
                # Landing / Instructions
                received_params = received_data[0].split(" ")
                if received_params[1] == "Landing":
                    received_values = received_data[1].split(" ")
                    position = Position(ord(received_values[0])-ord('0'), ord(received_values[1])-ord('0'))
                    if rover_table.get(received_params[0]) is not None: # delete and set again
                        rover_table.delete(received_params[0])
                    rover = Rover(plateau, position, Rover.DIRECTIONS.get(received_values[2]))
                    rover_table.add(received_params[0], rover)
                elif received_params[1] == "Instructions":
                    rover = rover_table.get(received_params[0])
                    if rover is not None: # Check Landing position is set
                        rover.process(received_data[1])
                        rover_table.update(received_params[0], rover)
                        print(received_params[0] + ":" + str(rover))
                    else:
                        print("No landing data")
                else: # Unrecognized parameter
                    print("Wrong Rover parameters")
    else:
        print("Wrong argument")

if __name__ == "__main__":
    main()
