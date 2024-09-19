from typing import List

import numpy
from numpy import ndarray

from src.classes.rover_mock import Rover


class IO:
    def __init__(
        self,
        plateauX: int = 10,
        plateauY: int = 10,
        roverCount: int = 2,
    ) -> None | int:
        if plateauX < 1:
            self.x = 10
        else:
            self.x = plateauX

        if plateauY < 1:
            self.y = 10
        else:
            self.y = plateauY

        self.roverCount: int = roverCount

    def createGrid(self) -> None:
        self.grid: ndarray = numpy.zeros(shape=(self.x, self.y))

    def createRovers(self) -> None:
        self.rovers: List[Rover] = [
            Rover(0, 0) for _ in range(self.roverCount)
        ]  # noqa: E501
