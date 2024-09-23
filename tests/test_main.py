from typing import List

from src.classes.plateau import Plateau
from src.classes.rover import Rover
from src.main import checkNumberOfRovers, createRovers, findEmptyPlateauCell


def test_main_checkNumberOfRovers() -> None:
    assert checkNumberOfRovers(roverCount=0, columns=1, rows=1) is False
    assert checkNumberOfRovers(roverCount=1, columns=1, rows=1) is True
    assert checkNumberOfRovers(roverCount=1, columns=2, rows=1) is True
    assert checkNumberOfRovers(roverCount=2, columns=1, rows=1) is False


def test_main_findEmptyPlateauCell() -> None:
    # Single value Plateau
    plateau: Plateau = Plateau(columns=0, rows=0)
    assert findEmptyPlateauCell(plateau=plateau) == (0, 0)

    # Single column, multi row Plateau
    plateau: Plateau = Plateau(columns=0, rows=1)
    assert findEmptyPlateauCell(plateau=plateau) == (0, 1)

    plateau.grid[1, 0] = 1
    assert findEmptyPlateauCell(plateau=plateau) == (0, 0)

    # Mult column, single row Plateau
    plateau: Plateau = Plateau(columns=1, rows=0)
    assert findEmptyPlateauCell(plateau=plateau) == (0, 0)

    plateau.grid[0, 0] = 1
    assert findEmptyPlateauCell(plateau=plateau) == (1, 0)

    # Square Plateau
    plateau: Plateau = Plateau(columns=9, rows=9)
    assert findEmptyPlateauCell(plateau=plateau) == (0, 9)

    plateau.grid[:, :] = 1
    plateau.grid[5, 3] = 0
    assert findEmptyPlateauCell(plateau=plateau) == (3, 5)


def test_main_createRovers() -> None:
    rovers: List[Rover] = createRovers(plateau=Plateau(), roverCount=2)

    assert len(rovers) == 2

    assert rovers[0].x == 0
    assert rovers[0].y == 10

    assert rovers[-1].x == 1
    assert rovers[-1].y == 10
