'''
Created on Feb 4, 2020

@author: user
'''

class Game():
    
    def __init__(self, board, ai):
        self.board = board
        self.ai = ai
        self.symbols = {'x':1, 'o':-1}
        
    def get_board(self):
        return self.board.get_board()
    
    def computer_move(self):
        
        board_status = self.board.get_board()
        line, column, symbol = self.ai.computer(board_status) # ai based on state of board
        print(line,column,symbol)
        self.board.move(line, column, symbol)
    
    def human_move(self, move):
        self.validate_move(move)
        line, column = int(move[0])-1 , int(move[1])-1
        symbol = self.symbols[move[2]]
        self.board.move(line, column, symbol)
        
        
        
    def check_game_over(self):
        '''
        Function that checks if the game is over and returns the result
        Input: self (the current state of the game)
        Output: False - if the game is not finished
                True, 2 - if the board is full (game won by chaos)
                True, 1 - if there was a winning move(5 consecutives) (game won by order)
        
        '''
        
        if self.board.check_full_board():
            return True, 2 # you won
        if self.board.check_winning():
            return True, 1 # you lost
        return False, None #if nobody won
    
    def validate_move(self, move):
        line = move[0]
        column = move[1]
        symbol = move[2]
        try:
            line = int(line)
            if line <1 or line>6:
                raise Exception('Line/Column outside the board')
            column = int(column)
            if column <1 or column >6:
                raise Exception('Line/Column outside the board')
        except ValueError:
            raise Exception('Line and column must be integers')
        if symbol not in ['x','o']:
            raise Exception('Incorrect symbol')