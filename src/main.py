from typing import List, Tuple

import click
import numpy

from src.classes.io import IO
from src.classes.plateau import Plateau
from src.classes.rover import Rover


def checkNumberOfRovers(
    columns: int,
    rows: int,
    roverCount: int,
) -> bool:
    if roverCount < 1:
        return False

    area: int = columns * rows

    if roverCount <= area:
        return True
    else:
        return False


def findEmptyPlateauCell(plateau: Plateau) -> Tuple[int, int]:
    """
    Finds the first instance of an empty cell within a Plateau grid.

    This algorithm starts at the bottom most cell (column: 0, row: n -1) and iterates column wise to identify cells that are equal to 0 (i.e. empty).

    If the algorithm reaches the end of the grid column wise, it decrements the row and starts back at column 0.

    This is done until the first empty cell is identified.

    :param plateau: _description_
    :type plateau: Plateau
    :return: Returns the coordinates in (column, row) format
    :rtype: Tuple[int, int]
    """  # noqa: E501
    columnIdx: int = 0
    rowIdx: int = plateau.rows - 1

    while True:
        if plateau.checkEmptyCell(column=columnIdx, row=rowIdx):
            break
        else:
            columnIdx += 1

            if columnIdx == plateau.columns:
                columnIdx = 0
                rowIdx -= 1

    return (columnIdx, rowIdx)


def createRovers(plateau: Plateau, roverCount: int = 1) -> List[Rover]:
    # Rovers are instantiated starting in the bottom left corner and then
    # moving across the x axis, followed by moving up the y axis
    rovers: List[Rover] = []

    roverID: int
    for roverID in range(roverCount):
        coordinates: Tuple[int, int] = findEmptyPlateauCell(plateau=plateau)

        rover: Rover = Rover(
            x=coordinates[0],
            y=coordinates[1],
            plateau=plateau,
            roverID=roverID + 1,
        )

        rovers.append(rover)

    return rovers


@click.command()
@click.option(
    "-c",
    "--columns",
    "plateauColumns",
    type=click.IntRange(min=1, max_open=True),
    required=False,
    default=100,
    help="Number of columns (i.e. width) of the plateau",
    show_default=True,
)
@click.option(
    "-r",
    "--rows",
    "plateauRows",
    type=click.IntRange(min=1, max_open=True),
    required=False,
    default=100,
    help="Number of rows (i.e. height) of the plateau",
    show_default=True,
)
@click.option(
    "--rover-count",
    "roverCount",
    type=click.IntRange(min=1, max_open=True),
    required=False,
    default=2,
    help="The number of rovers to deploy",
    show_default=True,
)
def main(plateauColumns: int, plateauRows: int, roverCount: int) -> None:
    # Steps:
    # 1. Ensure that the number of rovers specified fit into the plateau area
    if (
        checkNumberOfRovers(
            columns=plateauColumns,
            rows=plateauRows,
            roverCount=roverCount,
        )
        is False
    ):
        print("Too many rovers on the plateau:", roverCount)
        quit(1)

    # 2. Instantiate the plateau with the specified width and length
    plateau: Plateau = Plateau(columns=plateauColumns, rows=plateauRows)

    # 3. Create rovers
    rovers: List[Rover] = createRovers(plateau=plateau, roverCount=roverCount)

    # 4. Instantiate IO
    io: IO = IO(rovers=rovers)

    while True:
        print(plateau.grid)
        io.getInput()
        io.sendCommands()
        print()


if __name__ == "__main__":
    numpy.random.seed(42)
    main()
