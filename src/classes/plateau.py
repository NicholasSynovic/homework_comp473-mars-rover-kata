import numpy
from numpy import ndarray


class Plateau:
    def __init__(self, columns: int = 10, rows: int = 10):
        self.columns: int
        self.rows: int

        if columns < 1:
            self.columns = 10
        else:
            self.columns = columns

        if rows < 1:
            self.rows = 10
        else:
            self.rows = rows

        self.grid: ndarray = numpy.zeros(shape=(self.rows, self.columns))

    def checkEmptyCell(self, column: int, row: int) -> bool:
        if (column >= self.columns) or (row >= self.rows):
            return False

        if self.grid[column, row] == 0:
            return True
        else:
            return False

    def validateCoordinate(self, column: int, row: int) -> bool:
        if (
            (column >= 0)
            and (column <= self.columns)
            and (row >= 0)
            and (row <= self.rows)
        ):
            return True
        else:
            return False

    def updateGrid(self, column: int, row: int, roverID: int) -> bool:
        if self.checkEmptyCell(column=column, row=row) and self.validateCoordinate(
            column=column,
            row=row,
        ):
            self.grid[column, row] = roverID
            return True
        else:
            return False
