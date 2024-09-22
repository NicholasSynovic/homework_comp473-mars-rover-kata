from src.classes.plateau import Plateau
from src.main import checkNumberOfRovers, findEmptyPlateauCell


def test_main_checkNumberOfRovers() -> None:
    assert checkNumberOfRovers(roverCount=0, plateauX=1, plateauY=1) is False
    assert checkNumberOfRovers(roverCount=1, plateauX=1, plateauY=1) is True
    assert checkNumberOfRovers(roverCount=1, plateauX=2, plateauY=1) is True
    assert checkNumberOfRovers(roverCount=2, plateauX=1, plateauY=1) is False


def test_main_checkEmptyPlateauCell() -> None:
    plateau: Plateau = Plateau(x=10, y=10)
    assert findEmptyPlateauCell(plateau=plateau) == (0, 9)

    plateau.grid[[0, 9]] = 1
    assert findEmptyPlateauCell(plateau=plateau) == (1, 9)

    plateau.grid[:, :] = 1
    plateau.grid[5, 5] = 0
    assert findEmptyPlateauCell(plateau=plateau) == (5, 5)
