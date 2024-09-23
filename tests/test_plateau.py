from typing import List, Tuple

from src.classes.plateau import Plateau


def test_plateau_columns() -> None:
    assert Plateau().columns == 11
    assert Plateau(columns=20).columns == 21
    assert Plateau(columns=1).columns == 2
    assert Plateau(columns=0).columns == 1
    assert Plateau(columns=-1).columns == 10


def test_plateau_rows() -> None:
    assert Plateau().rows == 11
    assert Plateau(rows=20).rows == 21
    assert Plateau(rows=1).rows == 2
    assert Plateau(rows=0).rows == 1
    assert Plateau(rows=-1).rows == 10


def test_plateau_gridColumns() -> None:
    columns: List[int] = [10, 20, 1, 0, -1]

    columns: int
    for column in columns:
        plateau: Plateau = Plateau(columns=column)

        if column < 0:
            assert plateau.grid.shape == (11, 10)
        else:
            assert plateau.grid.shape == (11, column + 1)


def test_plateau_gridRows() -> None:
    rows: List[int] = [10, 20, 1, 0, -1]

    row: int
    for row in rows:
        plateau: Plateau = Plateau(rows=row)

        if row < 0:
            assert plateau.grid.shape == (10, 11)
        else:
            assert plateau.grid.shape == (row + 1, 11)


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

        if (pair[0] < 0) and (pair[1] >= 0):
            assert plateau.grid.shape == (pair[1] + 1, 10)
        elif (pair[0] >= 0) and (pair[1] < 0):
            assert plateau.grid.shape == (10, pair[0] + 1)
        elif (pair[0] < 0) and (pair[1] < 0):
            assert plateau.grid.shape == (10, 10)
        else:
            assert plateau.grid.shape == (pair[1] + 1, pair[0] + 1)


def test_plateau_checkEmptyCell() -> None:
    plateau: Plateau = Plateau()
    assert plateau.checkEmptyCell(column=11, row=0) is False
    assert plateau.checkEmptyCell(column=0, row=11) is False

    assert plateau.checkEmptyCell(column=0, row=0) is True

    plateau.grid[0, 0] = 1
    assert plateau.checkEmptyCell(column=0, row=0) is False


def test_plateau_validateCoordinate() -> None:
    plateau: Plateau = Plateau()

    assert plateau.validateCoordinate(column=0, row=0) is True
    assert plateau.validateCoordinate(column=-1, row=0) is False
    assert plateau.validateCoordinate(column=0, row=-1) is False
    assert plateau.validateCoordinate(column=11, row=0) is True
    assert plateau.validateCoordinate(column=0, row=11) is True
    assert plateau.validateCoordinate(column=12, row=0) is False
    assert plateau.validateCoordinate(column=0, row=12) is False


def test_plateau_updateGrid() -> None:
    plateau: Plateau = Plateau()

    assert plateau.updateGrid(column=0, row=0, roverID=1) is True
    assert plateau.updateGrid(column=0, row=0, roverID=2) is False
    assert plateau.grid[0, 0] == 1

    assert plateau.updateGrid(column=12, row=0, roverID=3) is False
    assert plateau.updateGrid(column=0, row=12, roverID=4) is False

    assert plateau.updateGrid(column=5, row=0, roverID=5) is True
    assert plateau.updateGrid(column=0, row=5, roverID=6) is True
    assert plateau.grid[0, 5] == 5
    assert plateau.grid[5, 0] == 6
