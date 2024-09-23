from typing import Tuple

from src.classes.orientation import Orientation
from src.classes.plateau import Plateau


class Rover:
    def __init__(
        self,
        x: int,
        y: int,
        plateau: Plateau,
        roverID: str,
    ) -> None:
        if (x < 0) or (x >= plateau.columns):
            self.x = 0
        else:
            self.x = x

        if (y < 0) or (y >= plateau.rows):
            self.y = 0
        else:
            self.y = y

        self.plateau: Plateau = plateau
        self.roverID = roverID

        self.orientation: Orientation = Orientation()

        # Place rover
        self.plateau.updateGrid(column=x, row=y, roverID=self.roverID)

    def update(self, cmd: str) -> None:
        char: str
        for char in cmd:
            match char:
                case "R":
                    self.orientation.next()
                case "L":
                    self.orientation.prev()
                case "M":
                    if self.move() is False:
                        break

    def move(self) -> bool:
        currentOrientation: str = self.orientation.get()

        movement: Tuple[int, int]
        match currentOrientation:
            case "N":
                movement = (0, -1)
            case "E":
                movement = (1, 0)
            case "S":
                movement = (0, 1)
            case "W":
                movement = (-1, 0)

        newX: int = self.x + movement[0]
        newY: int = self.y + movement[1]

        if self.plateau.updateGrid(
            column=newX,
            row=newY,
            roverID=self.roverID,
        ):
            self.plateau.clearCell(column=self.x, row=self.y)
            self.x = newX
            self.y = newY

            return True

        else:
            return False
