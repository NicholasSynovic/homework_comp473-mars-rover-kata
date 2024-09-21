import numpy
from numpy import ndarray

from src.classes.rover import Rover


class Plateau:
    def __init__(self, x: int, y: int):
        self.x: int
        self.y: int

        if x < 1:
            self.x = 10
        else:
            self.x = x

        if y < 1:
            self.y = 10
        else:
            self.y = y

    def createGrid(self) -> None:
        self.grid: ndarray = numpy.zeros(shape=(self.x, self.y))

    def checkEmpty(self, x: int, y: int) -> bool:
        if self.grid[x, y] == 0:
            return True
        else:
            return False

    def validateCoordinate(self, x: int, y: int) -> bool:
        if (x >= 0) and (x <= self.x) and (y >= 0) and (y <= self.y):
            return True
        else:
            return False

    def updateGrid(self, x: int, y: int, rover: Rover) -> bool:
        if self.checkEmpty(x=x, y=y) and self.validateCoordinate(
            x=x,
            y=y,
        ):
            self.grid[x, y] = rover
            return True
        else:
            return False
