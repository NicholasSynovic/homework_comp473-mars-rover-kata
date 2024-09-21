from src.classes.rover import Rover


def test_convertCommand() -> None:
    rover = Rover(0, 0)

    # test looping backwards on a list
    turn_left = rover._convertCommand("L")
    assert rover.position == "W"
    assert turn_left == [0, 0, "W"]

    # test looping forward on a list
    turn_right = rover._convertCommand("R")
    assert rover.position == "N"
    assert turn_right == [0, 0, "N"]


def test_move() -> None:
    rover = Rover(5, 6)

    # rover starting position upon initialization is N
    rover.move("M")
    assert rover.y == 7

    rover.position = "E"
    rover.move("M")
    assert rover.x == 6

    rover.position = "S"
    rover.move("M")
    assert rover.y == 6

    rover.position = "W"
    rover.move("M")
    assert rover.x == 5
