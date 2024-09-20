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

    def _replaceLetters(self, string: str) -> str:
        return "".join(char if char in "RLM" else "" for char in string)

    def getInput(self) -> dict[Rover, str]:
        data: dict[Rover, str] = {}

        idx: int
        for idx in range(len(self.rovers)):
            rover: Rover = self.rovers[idx]

            roverX: int = self.rovers[idx].x
            roverY: int = self.rovers[idx].y

            cmd: str = (
                input(f"Rover {idx} (x: {roverX}, y: {roverY}): ")
                .strip()
                .upper()  # noqa: E501
            )

            cmd = self._replaceLetters(string=cmd)

            data[rover] = cmd

        return data
