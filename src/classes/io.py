from typing import List

from src.classes.rover import Rover


class IO:
    def __init__(self, rovers: List[Rover]) -> None:
        # TODO: Update tests
        if len(rovers) == 0:
            raise ValueError("No Rovers availible")

        self.rovers: List[Rover] = rovers

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
