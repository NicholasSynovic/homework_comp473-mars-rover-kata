from src.classes.orientation import Orientation


def test_orientation_next() -> None:
    orientation: Orientation = Orientation()

    orientation.next()
    assert orientation.pointer == 1

    orientation.pointer = 3
    orientation.next()
    assert orientation.pointer == 0

    orientation.pointer = 1000
    orientation.next()
    assert orientation.pointer == 0


def test_orientation_prev() -> None:
    orientation: Orientation = Orientation()

    orientation.prev()
    assert orientation.pointer == 3

    orientation.pointer = 3
    orientation.prev()
    assert orientation.pointer == 2

    orientation.pointer = 0
    orientation.prev()
    assert orientation.pointer == 3


def test_orientation_get() -> None:
    orientation: Orientation = Orientation()

    assert orientation.get() == "N"

    orientation.next()
    assert orientation.get() == "E"

    orientation.prev()
    orientation.prev()
    assert orientation.get() == "W"
