from src.classes.rover_mock import Rover


class IO:
    def __init__(self, roverSquadSize: int = 2) -> None:
        for idx in range(roverSquadSize):
            Rover()
