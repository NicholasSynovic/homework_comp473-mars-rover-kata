import pytest

from src.classes.plateau import Plateau
from src.main import checkNumberOfRovers, findEmptyPlateauCell


def test_main_checkNumberOfRovers() -> None:
    assert checkNumberOfRovers(roverCount=0, columns=1, rows=1) is False
    assert checkNumberOfRovers(roverCount=1, columns=1, rows=1) is True
    assert checkNumberOfRovers(roverCount=1, columns=2, rows=1) is True
    assert checkNumberOfRovers(roverCount=2, columns=1, rows=1) is False


def test_main_checkEmptyPlateauCell() -> None:
    # Single value Plateau
    plateau: Plateau = Plateau(columns=1, rows=1)
    assert findEmptyPlateauCell(plateau=plateau) == (0, 0)

    # Single column, multi row Plateau
    plateau: Plateau = Plateau(columns=1, rows=2)
    assert findEmptyPlateauCell(plateau=plateau) == (0, 1)

    plateau.grid[1, 0] = 1
    assert findEmptyPlateauCell(plateau=plateau) == (0, 0)

    # Mult column, single row Plateau
    plateau: Plateau = Plateau(columns=2, rows=1)
    assert findEmptyPlateauCell(plateau=plateau) == (0, 0)

    plateau.grid[0, 0] = 1
    assert findEmptyPlateauCell(plateau=plateau) == (1, 0)

    # Square Plateau
    plateau: Plateau = Plateau(columns=10, rows=10)
    assert findEmptyPlateauCell(plateau=plateau) == (0, 9)

    plateau.grid[:, :] = 1
    plateau.grid[5, 3] = 0
    assert findEmptyPlateauCell(plateau=plateau) == (3, 5)
