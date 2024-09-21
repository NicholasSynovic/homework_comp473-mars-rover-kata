from typing import List

import click
import numpy

from src.classes.io import IO
from src.classes.plateau import Plateau
from src.classes.rover import Rover


def createRover(plateau: Plateau) -> Rover:
    # TODO: Add test
    x: int = 0
    y: int = 0

    while True:
        if plateau.checkEmpty(x=x, y=y):
            break
        else:
            x += 1

    return Rover(x=x, y=y)


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
    if roverCount > plateauX * plateauY:
        print("Number of rovers exceeds the area of the palteau")
        quit(1)

    plateau: Plateau = Plateau(x=plateauX, y=plateauY)
    plateau.createGrid()

    rovers: List[Rover] = [
        createRover(plateau=plateau) for _ in range(roverCount)
    ]  # noqa: E501

    try:
        io: IO = IO(rovers=rovers)
    except ValueError as error:
        print(error)
        quit(1)

    while True:
        cmds: dict[Rover, str] = io.getInput()

        rover: Rover
        cmd: str
        for rover, cmd in cmds.items():
            print(rover, cmd)


if __name__ == "__main__":
    numpy.random.seed(42)
    main()
