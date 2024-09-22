from typing import List, Tuple

from src.classes.io import IO


def test_io_createRovers() -> None:
    rovers: List[int] = [10, 1, 0, -1]

    rover: int
    for rover in rovers:
        io: IO = IO(roverCount=rover)
        io.createRovers()

        if rover < 1:
            assert len(io.rovers) == 2
        else:
            assert len(io.rovers) == rover
