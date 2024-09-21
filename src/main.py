import click

from src.classes.io import IO
from src.classes.rover import Rover


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
    help="The length of the plateu",
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
    try:
        io: IO = IO(
            plateauX=plateauX,
            plateauY=plateauY,
            roverCount=roverCount,
        )
    except ValueError as err:
        print(err)
        quit(1)

    io.createGrid()
    io.createRovers()

    while True:
        io.getInput()

        rover: Rover
        for rover in io.rovers:
            print(rover.position)


if __name__ == "__main__":
    main()
