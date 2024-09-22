from src.main import checkNumberOfRovers


def test_main_checkNumberOfRovers() -> None:
    assert checkNumberOfRovers(roverCount=0, plateauX=1, plateauY=1) is False
    assert checkNumberOfRovers(roverCount=1, plateauX=1, plateauY=1) is True
    assert checkNumberOfRovers(roverCount=1, plateauX=2, plateauY=1) is True
    assert checkNumberOfRovers(roverCount=2, plateauX=1, plateauY=1) is False
