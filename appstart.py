'''
Created on Feb 4, 2020

@author: user
'''
from Repository import Board
from ServiceAI import AI_random, AI
from Service import Game
from UI import UI

board = Board()
ai = AI()

game = Game(board, ai)

ui = UI(game)
ui.start()