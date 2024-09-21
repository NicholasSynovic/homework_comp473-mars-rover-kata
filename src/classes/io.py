from typing import List

from src.classes.rover import Rover


class IO:
    def __init__(
        self,
        plateauX: int = 10,
        plateauY: int = 10,
        roverCount: int = 2,
    ) -> None:
        if roverCount < 1:
            self.roverCount = 2
        else:
            self.roverCount = roverCount

        # TODO: Add test case
        if self.roverCount > (self.x * self.y):
            raise ValueError("Number of rovers exceeds plateau area")

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
