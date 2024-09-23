from typing import List

from src.classes.rover import Rover


class IO:
    def __init__(self, rovers: List[Rover]) -> None:
        if len(rovers) == 0:
            raise ValueError("No Rovers availible")

        self.rovers: List[Rover] = rovers

        self.cmds: dict[Rover, str] = {}

    def replaceLetters(self, string: str) -> str:
        return "".join(char if char in "RLM" else "" for char in string)

    def getInput(self) -> None:
        # TODO: Figure out how to test this
        data: dict[Rover, str] = {}

        idx: int
        for idx in range(len(self.rovers)):
            rover: Rover = self.rovers[idx]

            roverID: int = rover.roverID
            roverX: int = rover.x
            roverY: int = rover.plateau.rows - rover.y - 1
            roverOrientation: str = rover.orientation.get()

            cmd: str = (
                input(
                    f"Rover {roverID} (column: {roverX}, row: {roverY}, orientation: {roverOrientation}): "  # noqa: E501
                )
                .strip()
                .upper()  # noqa: E501
            )

            data[rover] = self.replaceLetters(string=cmd)

        self.cmds = data

    def sendCommands(self) -> None:
        rover: Rover
        cmd: str | None
        for rover, cmd in self.cmds.items():
            if cmd == "":
                continue
            else:
                rover.update(cmd=cmd)
