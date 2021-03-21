'''
Created on Feb 4, 2020

@author: user
'''
from texttable import Texttable

class UI:
    
    def __init__(self, game):
        self.game = game
        self.messages = {1:'Order won', 2:'Chaos won'}
    
    def print_board(self):
        t = Texttable()
        b = self.game.get_board()
        for line in b:
            printed_line = []
            for element in line:
                if element == 0:
                    printed_line.append(' ')
                elif element == 1:
                    printed_line.append('x')
                else:
                    printed_line.append('o')
            t.add_row(printed_line)
        print(t.draw())
    
    def start(self):
        self.print_board()
        game_over = False
        
        while True:
            try:
                while not game_over:    
                    human_move = self.read_human_move()
                    self.game.human_move(human_move)
                    self.print_board()
                    game_over, result = self.game.check_game_over()
                    if game_over:
                        print(self.messages[result])
                        return
                    if not game_over:
                        self.game.computer_move()
                        self.print_board()
                        game_over, result = self.game.check_game_over()
                        if game_over:
                            print(self.messages[result])
                            return
            except Exception as text:
                print(' ! Error' + str(text))
        #print(self.messages[result])
        
        
    def read_human_move(self):
        line = input('Line: ')
        column = input('Column: ')
        symbol = input('Symbol: ')
        return [line,column,symbol]