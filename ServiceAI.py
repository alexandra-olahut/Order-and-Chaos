'''
Created on Feb 4, 2020

@author: user
'''

import random
class AI_random:
    
    def __init__(self):
        pass 
    def computer(self, board):
        line = random.choice([0,1,2,3,4,5])
        column = random.choice([0,1,2,3,4,5])
        symbol = random.choice([1,-1])
        return line,column,symbol

class AI():
    def __init__(self):
        pass 
    
    def computer(self, board):
        # first check if winning move
        winning_move, line, column, symbol = self.check_winning_move(board)
        if winning_move:
            return line, column, symbol
        
        else:
            symbol = self.most_frequent_symbol(board)
            line,column = self.most_neighbours(symbol, board)
            return line, column, symbol
    
    
    def most_frequent_symbol(self, board):
        frequence1 = 0
        frequence_1 = 0
        for l in range(6):
            for c in range(6):
                if board[l][c] == 1:
                    frequence1 +=1
                elif board[l][c] == -1:
                    frequence_1 +=1
        if frequence1 >= frequence_1:
            return 1
        else:
            return -1
    
    
    
    def most_neighbours(self, symbol, board):
        neighbour = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        
        
        # if there is not optimal way, we choose random
        line, column = 0,0
        while board[line][column] !=0:
            line = random.choice([0,1,2,3,4,5])
            column = random.choice([0,1,2,3,4,5])
                
        
        for l in range(6): #without borders
            for c in range(6):
                # if i find the symbol i note it as a neighbour for its neighbours
                if board[l][c] == symbol: #than it is a neighbour of:
                    if l!=0:
                        if c!=0:
                            neighbour[l-1][c-1] +=1
                        neighbour[l-1][c] +=1
                        if c!=5:
                            neighbour[l-1][c+1] +=1
                    
                    if c!=0:
                        neighbour[l][c-1] +=1
                    if c!=5:
                        neighbour[l][c+1] +=1
                    
                    if l!=5:
                        if c!=0:
                            neighbour[l+1][c-1] +=1
                        neighbour[l+1][c] +=1
                        if c!=5:
                            neighbour[l+1][c+1] +=1
        
        max_nrof_neighbours = 0
        for l in range(6):
            for c in range(6):
                #if valid move only
                if board[l][c] == 0:
                    if neighbour[l][c]>max_nrof_neighbours:
                        max_nrof_neighbours = neighbour[l][c] 
                        line = l 
                        column = c
        
        return line, column
    
    
    def check_winning_window(self, window):
    
        if window.count(0) == 1 and window.count(1) == 4:
            return True, window.index(0), 1
    
        if window.count(0) == 1 and window.count(-1) == 4:
            return True, window.index(0), -1
        return False, 0,0
    
    def check_winning_move(self, board):
        
        # i take windows of 5 consecutive spaces on vertical, horizontal, diagonally
        # check for every window if it has 4 same-symbols and an empty space
        
        #VERTICALLY
        for c in range(6):
            for l_start in range(2):
                window = []
                for i in range(5):
                    window.append(board[l_start+i][c])
                is_win,index_in_window,symbol = self.check_winning_window(window)
                line = index_in_window + l_start
                column = c
                if is_win:
                    return True, line, column, symbol    
                
        #HORIZONTALLY
        for l in range(6):
            for c_start in range(2):
                window = []
                for i in range(5):
                    window.append(board[l][c_start+i])
                is_win,index_in_window,symbol = self.check_winning_window(window)
                column = index_in_window + c_start
                line = l
                if is_win:
                    return True, line, column, symbol    
                
        #DIAGONALLY - positive
        for l in range(5,3,-1):
            for c in range(2):
                window = []
                for i in range(5):
                    window.append(board[l-i][c+i])
                is_win,index_in_window,symbol = self.check_winning_window(window)
                column = index_in_window + c
                line = -index_in_window + l
                if is_win:
                    return True, line, column, symbol    
                
        
        
        
        #DIAGONALLY - negative
        for l in range(2):
            for c in range(2):
                window = []
                for i in range(5):
                    window.append(board[l+i][c+i])
                is_win,index_in_window,symbol = self.check_winning_window(window)
                column = index_in_window + c
                line = index_in_window + l
                if is_win:
                    return True, line, column, symbol    
                
        
        return False,0,0,0