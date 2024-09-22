from typing import List

import click
import numpy

from src.classes.io import IO
from src.classes.plateau import Plateau
from src.classes.rover import Rover


def checkNumberOfRovers(
    roverCount: int,
    plateauX: int,
    plateauY: int,
) -> bool:
    if roverCount < 1:
        return False

    area: int = plateauX * plateauY

    if roverCount <= area:
        return True
    else:
        return False


def createRovers(plateau: Plateau, roverCount: int = 1) -> bool:
    # Rovers are instantiated starting in the bottom left corner and then moving across the x axis, followed by moving up the y axis
    idxLeft: int = 0
    bottomIndex: int = plateau.y - 1

    roverIDCounter: int = 1

    roverIDX: int
    for roverIDX in range(roverCount):
        # For each roverIDX, check if the space is open prior to insertion
        pass


@click.command()
@click.option(
    "-x",
    "plateauX",
    type=click.IntRange(min=1, max_open=True),
    required=False,
    default=100,
    help="The width of the plateau",
    show_default=True,
)
@click.option(
    "-y",
    "plateauY",
    type=click.IntRange(min=1, max_open=True),
    required=False,
    default=100,
    help="The length of the plateau",
    show_default=True,
)
@click.option(
    "-r",
    "--rover-count",
    "roverCount",
    type=click.IntRange(min=1, max_open=True),
    required=False,
    default=2,
    help="The number of rovers to deploy",
    show_default=True,
)
def main(plateauX: int, plateauY: int, roverCount: int) -> None:
    # Steps:
    # 1. Ensure that the number of rovers specified fit into the plateau area
    if (
        checkNumberOfRovers(
            roverCount=roverCount,
            plateauX=plateauX,
            plateauY=plateauY,
        )
        is False
    ):
        print("Too many rovers on the plateau:", roverCount)
        quit(1)

    # 2. Instantiate the plateau with the specified width and length
    plateau: Plateau = Plateau(x=plateauX, y=plateauY)

    # 3. Create rovers

    rovers: List[Rover] = [
        createRover(
            plateau=plateau,
            roverID=10,
        )
        for _ in range(roverCount)
    ]  # noqa: E501

    print(plateau.grid)
    # try:
    #     io: IO = IO(rovers=rovers)
    # except ValueError as error:
    #     print(error)
    #     quit(1)

    # while True:
    #     cmds: dict[Rover, str] = io.getInput()

    #     rover: Rover
    #     cmd: str
    #     for rover, cmd in cmds.items():
    #         print(rover, cmd)


if __name__ == "__main__":
    numpy.random.seed(42)
    main()
