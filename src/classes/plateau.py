class Plateau:
    def __init__(self, x: int, y: int):
        self.width = x
        self.height = y
        self.grid = self.create_grid()

    def createGrid(self):
        return [
            [None for _ in range(self.x_limit + 1)]
            for _ in range(self.y_limit + 1)  # noqa: E501
        ]

    def checkMove(self, x: int, y: int, rover) -> bool:
        if 0 <= x <= self.width and 0 <= y <= self.height:
            coordinate_x = rover.x + x
            coordinate_y = rover.y + y
            if coordinate_x <= self.width and coordinate_y <= self.height:
                return True
        return False
