from typing import List, Tuple

from src.classes.plateau import Plateau


def test_plateau_columns() -> None:
    assert Plateau().columns == 10
    assert Plateau(columns=20).columns == 20
    assert Plateau(columns=1).columns == 1
    assert Plateau(columns=0).columns == 10
    assert Plateau(columns=-1).columns == 10


def test_plateau_rows() -> None:
    assert Plateau().rows == 10
    assert Plateau(rows=20).rows == 20
    assert Plateau(rows=1).rows == 1
    assert Plateau(rows=0).rows == 10
    assert Plateau(rows=-1).rows == 10


def test_plateau_gridX() -> None:
    xValues: List[int] = [10, 20, 1, 0, -1]

    xVal: int
    for xVal in xValues:
        plateau: Plateau = Plateau(columns=xVal)

        if xVal < 1:
            assert plateau.grid.shape == (10, 10)
        else:
            assert plateau.grid.shape == (xVal, 10)


def test_plateau_gridY() -> None:
    yValues: List[int] = [10, 20, 1, 0, -1]

    yVal: int
    for yVal in yValues:
        plateau: Plateau = Plateau(rows=yVal)

        if yVal < 1:
            assert plateau.grid.shape == (10, 10)
        else:
            assert plateau.grid.shape == (10, yVal)


def test_plateau_grid() -> None:
    pairs: List[Tuple[int, int]] = [
        (10, 10),
        (10, 20),
        (20, 10),
        (20, 20),
        (1, 10),
        (10, 1),
        (1, 1),
        (0, 10),
        (10, 0),
        (0, 0),
        (-1, 10),
        (10, -1),
        (-1, -1),
    ]

    pair: Tuple[int, int]
    for pair in pairs:
        plateau: Plateau = Plateau(columns=pair[0], rows=pair[1])

        if (pair[0] < 1) and (pair[1] >= 1):
            assert plateau.grid.shape == (10, pair[1])
        elif (pair[0] >= 1) and (pair[1] < 1):
            assert plateau.grid.shape == (pair[0], 10)
        elif (pair[0] < 1) and (pair[1] < 1):
            assert plateau.grid.shape == (10, 10)
        else:
            assert plateau.grid.shape == (pair[0], pair[1])


def test_plateau_checkEmptyCell() -> None:
    plateau: Plateau = Plateau()
    assert plateau.checkEmptyCell(columns=10, rows=0) is False
    assert plateau.checkEmptyCell(columns=0, rows=10) is False

    assert plateau.checkEmptyCell(columns=0, rows=0) is True

    plateau.grid[[0, 0]] = 1
    assert plateau.checkEmptyCell(columns=0, rows=0) is False


def test_plateau_updateGrid() -> None:
    plateau: Plateau = Plateau()

    assert plateau.updateGrid(columns=0, rows=0, roverID=1) is True
    assert plateau.updateGrid(columns=0, rows=0, roverID=2) is False
    assert plateau.grid[0, 0] == 1

    assert plateau.updateGrid(columns=10, rows=0, roverID=3) is False
    assert plateau.updateGrid(columns=0, rows=10, roverID=4) is False

    assert plateau.updateGrid(columns=5, rows=0, roverID=5) is True
    assert plateau.updateGrid(columns=0, rows=5, roverID=6) is True
    assert plateau.grid[5, 0] == 5
    assert plateau.grid[0, 5] == 6


# def test_check_move_invalid():
#     plateau = Plateau(5, 5)
#     rover = Rover(6, 6, "N")

#     assert plateau.checkMove(rover) == False


# def test_check_move_on_edge():
#     plateau = Plateau(5, 5)
#     rover = Rover(5, 5, "N")

#     assert plateau.checkMove(rover) == True
