from typing import List


class Orientation:
    def __init__(self) -> None:
        self.orientations: List[str] = ["N", "E", "S", "W"]
        self.pointer: int = 0

    def next(self) -> None:
        self.pointer += 1

        if self.pointer > 3:
            self.pointer = 0

    def prev(self) -> None:
        self.pointer -= 1

        if self.pointer < 0:
            self.pointer = 3

    def get(self) -> str:
        return self.orientations[self.pointer]
