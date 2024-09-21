import numpy
from numpy import ndarray


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

    def checkMove(self, x: int, y: int, rover) -> bool:
        if 0 <= x <= self.width and 0 <= y <= self.height:
            coordinate_x = rover.x + x
            coordinate_y = rover.y + y
            if coordinate_x <= self.width and coordinate_y <= self.height:
                return True
        return False
