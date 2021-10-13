import unittest
from marsrover import *
from hashmap import HashMap
from instruction_parser import InstructionParser

class TestInstructionParser(unittest.TestCase):
    def testInstructionParserConstructor(self):
        parser = InstructionParser()

        parameter, rovername, command, values = parser.parse_instruntion("Plateau:5 5")
        self.assertEqual(parameter, "Plateau")
        self.assertEqual(rovername, None)
        self.assertEqual(command, None)
        self.assertEqual(values[0], "5")
        self.assertEqual(values[1], "5")

        parameter, rovername, command, values = parser.parse_instruntion("Rover1 Landing:1 2 N")
        self.assertEqual(parameter, "Rover1 Landing")
        self.assertEqual(rovername, "Rover1")
        self.assertEqual(command, "Landing")
        self.assertEqual(values[0], "1")
        self.assertEqual(values[1], "2")
        self.assertEqual(values[2], "N")

        parameter, rovername, command, values = parser.parse_instruntion("Rover2 Instructions:MMRMMRMRRM")
        self.assertEqual(parameter, "Rover2 Instructions")
        self.assertEqual(rovername, "Rover2")
        self.assertEqual(command, "Instructions")
        self.assertEqual(values[0], "MMRMMRMRRM")

        parameter, rovername, command, values = parser.parse_instruntion("")
        self.assertEqual(parameter, None)
        self.assertEqual(rovername, None)
        self.assertEqual(command, None)
        self.assertEqual(values, None)

        parameter, rovername, command, values = parser.parse_instruntion("Rover2 abc:MMRMMRMRRM")
        self.assertEqual(parameter, "Rover2 abc")
        self.assertEqual(rovername, "Rover2")
        self.assertEqual(command, "abc")
        self.assertEqual(values[0], "MMRMMRMRRM")

        parameter, rovername, command, values = parser.parse_instruntion("Rover1 abc:1 2 N")
        self.assertEqual(parameter, "Rover1 abc")
        self.assertEqual(rovername, "Rover1")
        self.assertEqual(command, "abc")
        self.assertEqual(values[0], "1")
        self.assertEqual(values[1], "2")
        self.assertEqual(values[2], "N")

class TestPosition(unittest.TestCase):
    def testPositionConstructor(self):
        # Create position instance with default values
        position = Position()
        self.assertEqual(position.x, 0)
        self.assertEqual(position.y, 0)

        # Create position instance with values
        position = Position(1, 2)
        self.assertEqual(position.x, 1)
        self.assertEqual(position.y, 2)

class TestPlateau(unittest.TestCase):
    def testPlateauConstructor(self):
        plateau = Plateau(7, 10)

        self.assertEqual(plateau.width, 7)
        self.assertEqual(plateau.height, 10)

class TestRover(unittest.TestCase):
    def testRoverConstructor(self):
        plateau = Plateau(7, 7)
        position = Position(0, 0)

        rover = Rover(plateau, position, Rover.DIRECTIONS.get('W'))

        self.assertEqual(Position(0, 0), rover.position)
        self.assertEqual(plateau, rover.plateau)

class TestHashMap(unittest.TestCase):
    def testHashMapConstructor(self):
        hmap = HashMap()
        hmap.add("1", "Alice")
        hmap.add("2", "Bob")
        hmap.add("3", "Carol")
        hmap.add("4", "Chuck")
        hmap.add("5", "Craig")
        hmap.add("6", "Dan")
        hmap.add("7", "Eve")
        hmap.add("8", "Frank")
        hmap.add("9", "Grace")
        hmap.add("10", "Heidi")
        self.assertEqual(hmap.get("1"), "Alice")
        self.assertEqual(hmap.get("2"), "Bob")
        self.assertEqual(hmap.get("3"), "Carol")
        self.assertEqual(hmap.get("4"), "Chuck")
        self.assertEqual(hmap.get("5"), "Craig")
        self.assertEqual(hmap.get("6"), "Dan")
        self.assertEqual(hmap.get("7"), "Eve")
        self.assertEqual(hmap.get("8"), "Frank")
        self.assertEqual(hmap.get("9"), "Grace")
        self.assertEqual(hmap.get("10"), "Heidi")
        hmap.delete("7")
        self.assertEqual(hmap.get("7"), None)
        hmap.add("8", "Judy")
        self.assertEqual(hmap.get("8"), "Judy")

class TestInstruction1(unittest.TestCase):
    def testInstruction1(self):
        plateau = Plateau(5, 5)
        position = Position(1, 2)

        rover = Rover(plateau, position, Rover.DIRECTIONS.get('N'))
        rover.process("LMLMLMLMM")

        self.assertEqual(str(rover), "1 3 N")

class TestInstruction2(unittest.TestCase):
    def testInstruction2(self):
        plateau = Plateau(5, 5)
        position = Position(3, 3)

        rover = Rover(plateau, position, Rover.DIRECTIONS.get('E'))
        rover.process("MMRMMRMRRM")

        self.assertEqual(str(rover), "5 1 E")

if __name__ == '__main__':
    unittest.main()
