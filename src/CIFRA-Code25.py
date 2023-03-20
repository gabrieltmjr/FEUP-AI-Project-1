import math
import random
import time
import numpy as np
from copy import deepcopy
from enum import IntEnum

WHITE_PIECE = '⬜'
BLUE_PIECE = '🟦'
CENTRE_PIECE = '⬛'

NUM_TILES_PER_COLOR = 12

class Color(IntEnum):
    WHITE = 0
    BLUE = 1

BLUE_HOME_ROW = 5 - 1

class GameMode(IntEnum):
    DASH = 1
    SUM = 2
    KING = 3

class CIFRACode25:
    def __init__(self, game_mode=GameMode.SUM):
        self.game_mode = game_mode

        tile_set = np.array(['⬜', '🟦'] * NUM_TILES_PER_COLOR)
        np.random.shuffle(tile_set)
        self.tiles = np.insert(tile_set, NUM_TILES_PER_COLOR, '⬛').reshape((5, 5))
        
        self.pieces = np.zeros((5, 5), dtype=np.int8)
        for c in Color:
            piece_set = np.array(range(5)) + [1, -5][c]
            np.random.shuffle(piece_set)
            self.pieces[c * BLUE_HOME_ROW] = piece_set

        self.player = Color.WHITE

    def print_state(self):
        print('Next player:', ['⚪', '🔵'][self.player])
        print('Tiles:')
        print(self.tiles)
        print('Pieces:')
        print(self.pieces)
    

game = CIFRACode25()
game.print_state()
