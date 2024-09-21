import pytest
from plateau import Plateau

def test_create_grid():
    plateau = Plateau(5, 5)
    
    assert len(plateau.grid) == 6 
    assert len(plateau.grid[0]) == 6  
    
    for row in plateau.grid:
        for cell in row:
            assert cell is None

def test_check_move_invalid():
    plateau = Plateau(5, 5)
    rover = Rover(6, 6, 'N')  
    
    assert plateau.checkMove(rover) == False

def test_check_move_on_edge():
    plateau = Plateau(5, 5)
    rover = Rover(5, 5, 'N')

    assert plateau.checkMove(rover) == True


