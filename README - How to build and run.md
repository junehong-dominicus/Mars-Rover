### 0. Building and Running Environment
- macOS Big Sur Version 11.6
- Python 3.9.6 and virtualenv 20.7.1

This is a sketch of the Mars-Rover project directory structure:
```
Mars-Rover\ ............. The "Mars-Rover root directory"
  app.py
  hashmap.py
  input.text
  input_1.text
  input_2.text
  input_10.text
  README - EventMobi Assessment.md
  README - How to build and run.md
  README.md
  marsrover\
    __init__.py
    plateau.py
    position.py
    rover.py
  tests\
    __init__.py
    test_mars_rover.py
```

### 1. How to run
Go to the Mars-Rover project root directory and just run:
```
$ cd /path/to/your/Mars-Rover/dir
$ python app.py input.txt
```

### 2. How to run unit tests
Go to the Mars-Rover project root directory and just run:
```
$ cd /path/to/your/Mars-Rover/dir
$ python -m unittest tests/test_mars_rover.py
```
