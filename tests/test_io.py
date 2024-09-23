from typing import List

from src.classes.io import IO
from src.classes.plateau import Plateau
from src.classes.rover import Rover


def test_io_rovers() -> None:
    rovers: List[Rover] = [Rover(x=0, y=0, plateau=Plateau(), roverID=1)]

    io: IO = IO(rovers=rovers)
    assert io.rovers == rovers


def test_io_cmds() -> None:
    rovers: List[Rover] = [Rover(x=0, y=0, plateau=Plateau(), roverID=1)]

    io: IO = IO(rovers=rovers)
    assert io.cmds == {}


def test_io_replaceLetters() -> None:
    rovers: List[Rover] = [Rover(x=0, y=0, plateau=Plateau(), roverID=1)]

    io: IO = IO(rovers=rovers)

    assert io.replaceLetters(string="Hello World".upper()) == "LLRL"
    assert io.replaceLetters(string="Meats and Cheeses".upper()) == "M"
    assert io.replaceLetters(string="The cat and the hat".upper()) == ""
