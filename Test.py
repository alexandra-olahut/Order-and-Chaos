'''
Created on Feb 4, 2020

@author: user
'''
from Service import Game
from ServiceAI import AI
from Repository import Board

class Test():
    
    def __init__(self):
        pass
        
    def test_win_row(self):
        board = Board()
        for i in range(5):
            board.move(2, i, 1)
        assert board.check_winning() == True
        
    def test_win_column(self):
        board = Board()
        for i in range(5):
            board.move(i,0,-1)
        assert board.check_winning() == True
        
    def test_win_diagonally(self):
        board = Board()
        for i in range(5):
            for j in range(5):
                board.move(i,j,1)
        assert board.check_winning() == True
        
    
    def run_all(self):
        self.test_win_row()
        self.test_win_column()
        self.test_win_diagonally()
        
t = Test()
t.run_all()