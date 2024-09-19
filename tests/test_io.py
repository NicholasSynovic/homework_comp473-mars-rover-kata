from typing import List, Tuple

from src.classes.io import IO


def test_io_plateauX() -> None:
    assert IO().x == 10
    assert IO(plateauX=20).x == 20
    assert IO(plateauX=1).x == 1
    assert IO(plateauX=0).x == 10
    assert IO(plateauX=-1).x == 10


def test_io_plateauY() -> None:
    assert IO().y == 10
    assert IO(plateauY=20).y == 20
    assert IO(plateauY=1).y == 1
    assert IO(plateauY=0).y == 10
    assert IO(plateauY=-1).y == 10


def test_io_createGridX() -> None:
    xValues: List[int] = [10, 20, 1, 0, -1]

    xVal: int
    for xVal in xValues:
        io: IO = IO(plateauX=xVal)
        io.createGrid()

        if xVal < 1:
            assert io.grid.shape == (10, 10)
        else:
            assert io.grid.shape == (xVal, 10)


def test_io_createGridY() -> None:
    yValues: List[int] = [10, 20, 1, 0, -1]

    yVal: int
    for yVal in yValues:
        io: IO = IO(plateauY=yVal)
        io.createGrid()

        if yVal < 1:
            assert io.grid.shape == (10, 10)
        else:
            assert io.grid.shape == (10, yVal)


def test_io_createGridXY() -> None:
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
        io: IO = IO(plateauX=pair[0], plateauY=pair[1])
        io.createGrid()

        if (pair[0] < 1) and (pair[1] >= 1):
            assert io.grid.shape == (10, pair[1])
        elif (pair[0] >= 1) and (pair[1] < 1):
            assert io.grid.shape == (pair[0], 10)
        elif (pair[0] < 1) and (pair[1] < 1):
            assert io.grid.shape == (10, 10)
        else:
            assert io.grid.shape == (pair[0], pair[1])
