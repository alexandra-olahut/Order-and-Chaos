'''
Created on Feb 4, 2020

@author: user
'''

class Board():
    
    def __init__(self):
        self.data = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        self.moves = 0
        
    def get_board(self):
        return self.data
    
    def getter(self, line, column):
        return self.data[line][column]
    
    
    def move(self, line, column, symbol):
        if self.data[line][column] != 0:
            raise Exception(' ! The spot is not empty')
        self.data[line][column] = symbol
        self.moves +=1
        
    def check_full_board(self):
        if self.moves == 36:
            return True 
        return False
    
    
    def check_winning(self):
        '''
        Function that checks if 'order' won (if there are 5 consecutive symbols of same type)
              - we create 'windows' of 5 consecutive elements from the board and check if it is a win
        Input: -self: the currrent state of the board
        Output: True - if game was won by 'order'
                False - if game is still on
        '''
        #VERTICALLY
        for c in range(6):
            for l_start in range(2):
                window = []
                for i in range(5):
                    window.append(self.data[l_start+i][c])
                if window.count(1) == 5 or window.count(-1) == 5:
                    return True    
                
        #HORIZONTALLY
        for l in range(6):
            for c_start in range(2):
                window = []
                for i in range(5):
                    window.append(self.data[l][c_start+i])
                if window.count(1) == 5 or window.count(-1) == 5:
                    return True    
                
        #DIAGONALLY - positive
        for l in range(5,3,-1):
            for c in range(2):
                window = []
                for i in range(5):
                    window.append(self.data[l-i][c+i])
                if window.count(1) == 5 or window.count(-1) == 5:
                    return True    
        
        #DIAGONALLY - negative
        for l in range(2):
            for c in range(2):
                window = []
                for i in range(5):
                    window.append(self.data[l+i][c+i])
                if window.count(1) == 5 or window.count(-1) == 5:
                    return True    
                
                
    
    
    
    
    
    
    
    
    
    
    
    '''
    
    def check_winning_move(self):
        pass
    
    
    def most_frequent_symbol(self):
        frequence1, frequence_1 = 0
        for l in range(6):
            for c in range(6):
                if self.data[l][c] == 1:
                    frequence1 +=1
                elif self.data[l][c] == -1:
                    frequence_1 +=1
        return max(frequence1, frequence_1)
    
    
    
    def most_neighbours(self, symbol):
        neighbour = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        
        for l in range(1,5): #without borders
            for c in range(1,5):
                # if i find the symbol i note it as a neighbour for its neighbours
                if self.data[l][c] == symbol: #than it is a neighbour of:
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
                if self.data[l][c] == 0:
                    if neighbour[l][c]>max_nrof_neighbours:
                        max_nrof_neighbours = neighbour[l][c] 
                        line = l 
                        column = c
        
        return line, column
        '''