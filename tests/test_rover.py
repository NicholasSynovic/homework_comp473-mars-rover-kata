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
    assert rover.x == 10

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
    assert rover.y == 10

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

    assert rover.orientation.get() == "N"


def test_rover_placement() -> None:
    plateau: Plateau = Plateau()

    _: Rover = Rover(x=0, y=0, plateau=plateau, roverID=1)
    assert plateau.grid[0, 0] == 1

    _: Rover = Rover(x=0, y=0, plateau=plateau, roverID=2)
    assert plateau.grid[0, 0] == 1

    _: Rover = Rover(x=0, y=1, plateau=plateau, roverID=2)
    assert plateau.grid[1, 0] == 2

    _: Rover = Rover(x=1, y=0, plateau=plateau, roverID=3)
    assert plateau.grid[0, 1] == 3

    grid: ndarray = plateau.grid

    _: Rover = Rover(x=10, y=10, plateau=plateau, roverID=3)
    assert array_equal(a1=plateau.grid, a2=grid) is True

    _: Rover = Rover(x=10, y=0, plateau=plateau, roverID=3)
    assert array_equal(a1=plateau.grid, a2=grid) is True

    _: Rover = Rover(x=0, y=10, plateau=plateau, roverID=3)
    assert array_equal(a1=plateau.grid, a2=grid) is True


def test_rover_update() -> None:
    plateau: Plateau = Plateau()
    rover: Rover = Rover(x=0, y=0, plateau=plateau, roverID=1)

    assert rover.orientation.get() == "N"

    rover.update(cmd="R")
    assert rover.orientation.get() == "E"

    rover.update(cmd="L")
    assert rover.orientation.get() == "N"

    rover.update(cmd="LLR")
    assert rover.orientation.get() == "W"

    rover.update(cmd="M")
    assert rover.orientation.get() == "W"


def test_rover_move() -> None:
    plateau: Plateau = Plateau(columns=1, rows=1)
    rover: Rover = Rover(x=0, y=1, plateau=plateau, roverID=1)

    assert rover.orientation.get() == "N"
    assert rover.x == 0
    assert rover.y == 1

    rover.update(cmd="M")
    assert rover.x == 0
    assert rover.y == 0

    rover.update(cmd="MM")
    assert rover.x == 0
    assert rover.y == 0

    rover.orientation.next()
    assert rover.orientation.get() == "E"

    rover.update(cmd="M")
    assert rover.x == 1
    assert rover.y == 0

    rover.update(cmd="MM")
    assert rover.x == 1
    assert rover.y == 0
