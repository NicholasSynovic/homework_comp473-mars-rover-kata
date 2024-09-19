from typing import List

import numpy
from numpy import ndarray

from src.classes.rover_mock import Rover


class IO:
    def __init__(
        self,
        plateauX: int,
        plateauY: int,
        roverCount: int = 2,
    ) -> None:
        self.x: int = plateauX
        self.y: int = plateauY
        self.roverCount: int = roverCount

        self.grid: ndarray = numpy.zeros(shape=(self.x, self.y))
        self.rovers: List[Rover] = [
            Rover(0, 0) for _ in range(self.roverCount)
        ]  # noqa: E501

        print(self.rovers)
        print(self.grid)
