from typing import List, Literal, Tuple

from src.classes.plateau import Plateau


class Rover:
    def __init__(self, x: int, y: int, plateau: Plateau, _id: str) -> None:
        self.plateau: Plateau = plateau
        self.orientation: Literal["N", "S", "E", "W"] = "N"
        self.id = _id

        if self.plateau.updateGrid(x=x, y=y, roverID=self.id):
            self.xPos: int = x
            self.yPos: int = y

        print(self.xPos, self.yPos)

    def _convertCommand(self, cmd) -> Tuple[int, int, str]:
        current = self.directions.index(self.position)

        # insane that python let's you loop backwards on a list
        if cmd == "L":
            self.position = self.directions[current - 1]
        if cmd == "R":
            self.position = self.directions[(current + 1) % 4]

        if cmd == "M":
            self.move(self, cmd)

        return [self.x, self.y, self.position]

    def move(self, str) -> bool:
        if self.position == "N":
            self.y += 1
        elif self.position == "E":
            self.x += 1
        elif self.position == "S":
            self.y -= 1
        elif self.position == "W":
            self.x -= 1
