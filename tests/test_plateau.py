from typing import List, Tuple

from src.classes.plateau import Plateau


def test_plateau_x() -> None:
    assert Plateau().x == 10
    assert Plateau(x=20).x == 20
    assert Plateau(x=1).x == 1
    assert Plateau(x=0).x == 10
    assert Plateau(x=-1).x == 10


def test_plateau_y() -> None:
    assert Plateau().y == 10
    assert Plateau(y=20).y == 20
    assert Plateau(y=1).y == 1
    assert Plateau(y=0).y == 10
    assert Plateau(y=-1).y == 10


def test_plateau_gridX() -> None:
    xValues: List[int] = [10, 20, 1, 0, -1]

    xVal: int
    for xVal in xValues:
        plateau: Plateau = Plateau(x=xVal)

        if xVal < 1:
            assert plateau.grid.shape == (10, 10)
        else:
            assert plateau.grid.shape == (xVal, 10)


def test_plateau_gridY() -> None:
    yValues: List[int] = [10, 20, 1, 0, -1]

    yVal: int
    for yVal in yValues:
        plateau: Plateau = Plateau(y=yVal)

        if yVal < 1:
            assert plateau.grid.shape == (10, 10)
        else:
            assert plateau.grid.shape == (10, yVal)


def test_plateau_createGridXY() -> None:
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
        plateau: Plateau = Plateau(x=pair[0], y=pair[1])

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
    assert plateau.checkEmptyCell(x=0, y=0) is True

    plateau.grid[[0, 0]] = 1
    assert plateau.checkEmptyCell(x=0, y=0) is False


# def test_check_move_invalid():
#     plateau = Plateau(5, 5)
#     rover = Rover(6, 6, "N")

#     assert plateau.checkMove(rover) == False


# def test_check_move_on_edge():
#     plateau = Plateau(5, 5)
#     rover = Rover(5, 5, "N")

#     assert plateau.checkMove(rover) == True
