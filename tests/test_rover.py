from numpy import array_equal, ndarray

from src.classes.plateau import Plateau
from src.classes.rover import Rover


def test_rover_x() -> None:
    plateau: Plateau = Plateau()
    rover: Rover = Rover(x=0, y=0, plateau=plateau, roverID=1)
    assert rover.x == 0

    rover = Rover(x=-1, y=0, plateau=plateau, roverID=1)
    assert rover.x == 0

    rover = Rover(x=10, y=0, plateau=plateau, roverID=1)
    assert rover.x == 0

    rover = Rover(x=11, y=0, plateau=plateau, roverID=1)
    assert rover.x == 0

    rover = Rover(x=5, y=0, plateau=plateau, roverID=1)
    assert rover.x == 5


def test_rover_y() -> None:
    plateau: Plateau = Plateau()
    rover: Rover = Rover(x=0, y=0, plateau=plateau, roverID=1)
    assert rover.y == 0

    rover = Rover(x=0, y=-1, plateau=plateau, roverID=1)
    assert rover.y == 0

    rover = Rover(x=0, y=10, plateau=plateau, roverID=1)
    assert rover.y == 0

    rover = Rover(x=0, y=11, plateau=plateau, roverID=1)
    assert rover.y == 0

    rover = Rover(x=0, y=5, plateau=plateau, roverID=1)
    assert rover.y == 5


def test_rover_plateau() -> None:
    plateau: Plateau = Plateau()
    rover: Rover = Rover(x=0, y=0, plateau=plateau, roverID=1)

    assert rover.plateau == plateau


def test_rover_roverID() -> None:
    plateau: Plateau = Plateau()
    rover: Rover = Rover(x=0, y=0, plateau=plateau, roverID=1)

    assert rover.roverID == 1


def test_rover_orientation() -> None:
    plateau: Plateau = Plateau()
    rover: Rover = Rover(x=0, y=0, plateau=plateau, roverID=1)

    assert rover.orientation == "N"


def test_rover_placement() -> None:
    plateau: Plateau = Plateau()

    _: Rover = Rover(x=0, y=0, plateau=plateau, roverID=1)
    assert plateau.grid[0, 0] == 1

    _: Rover = Rover(x=0, y=0, plateau=plateau, roverID=2)
    assert plateau.grid[0, 0] == 1

    _: Rover = Rover(x=1, y=0, plateau=plateau, roverID=2)
    assert plateau.grid[1, 0] == 2

    _: Rover = Rover(x=0, y=1, plateau=plateau, roverID=3)
    assert plateau.grid[0, 1] == 3

    grid: ndarray = plateau.grid

    _: Rover = Rover(x=10, y=10, plateau=plateau, roverID=3)
    assert array_equal(a1=plateau.grid, a2=grid) is True

    _: Rover = Rover(x=10, y=0, plateau=plateau, roverID=3)
    assert array_equal(a1=plateau.grid, a2=grid) is True

    _: Rover = Rover(x=0, y=10, plateau=plateau, roverID=3)
    assert array_equal(a1=plateau.grid, a2=grid) is True


# def test_convertCommand() -> None:
#     rover = Rover(0, 0)

#     # test looping backwards on a list
#     turn_left = rover._convertCommand("L")
#     assert rover.position == "W"
#     assert turn_left == [0, 0, "W"]

#     # test looping forward on a list
#     turn_right = rover._convertCommand("R")
#     assert rover.position == "N"
#     assert turn_right == [0, 0, "N"]


# def test_move() -> None:
#     rover = Rover(5, 6)

#     # rover starting position upon initialization is N
#     rover.move("M")
#     assert rover.y == 7

#     rover.position = "E"
#     rover.move("M")
#     assert rover.x == 6

#     rover.position = "S"
#     rover.move("M")
#     assert rover.y == 6

#     rover.position = "W"
#     rover.move("M")
#     assert rover.x == 5
