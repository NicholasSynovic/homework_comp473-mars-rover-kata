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
        self.x: int
        self.y: int
        self.roverCount: int

        if plateauX < 1:
            self.x = 10
        else:
            self.x = plateauX

        if plateauY < 1:
            self.y = 10
        else:
            self.y = plateauY

        if roverCount < 1:
            self.roverCount = 2
        else:
            self.roverCount = roverCount

    def createGrid(self) -> None:
        self.grid: ndarray = numpy.zeros(shape=(self.x, self.y))

    def createRovers(self) -> None:
        self.rovers: List[Rover] = [
            Rover(0, 0) for _ in range(self.roverCount)
        ]  # noqa: E501
