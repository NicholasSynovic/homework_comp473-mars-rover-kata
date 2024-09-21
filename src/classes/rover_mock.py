class Rover:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

        self.directions: list = ["N", "E", "S", "W"]
        self.position: str = self.directions[0]

    def _convertCommand(self, cmd) -> tuple[int, int, str]:
        current = self.directions[self.position]

        # insane that python let's you loop backwards on a list
        if cmd == "L":
            self.position = self.directions.index[current - 1]
        if cmd == "R":
            self.position = self.directions.index[(current + 1) % 4]

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
