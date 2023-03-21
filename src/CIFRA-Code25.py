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

GOAL_ROW = [5 - 1, 0]
HOME_ROW = [0, 5 - 1]
BLUE_START_INDEX = 20

class GameMode(IntEnum):
    DASH = 1
    SUM = 2
    KING = 3

MOVE_DIRECTION = [(i - 1, j - 1) for i in range(3) for j in range(3) if i != 1 or j != 1]

class CIFRACode25:
    def __init__(self, game_mode=GameMode.SUM):
        self.game_mode = game_mode

        tile_set = np.array(['⬜', '🟦'] * NUM_TILES_PER_COLOR)
        np.random.shuffle(tile_set)
        self.tiles = np.insert(tile_set, NUM_TILES_PER_COLOR, '⬛').reshape((5, 5))
        
        self.pieces = np.zeros((2, 5, 2), dtype=np.int8)
        for c in Color:
            piece_set = np.array(range(5))
            np.random.shuffle(piece_set)
            for p in range(5):
                self.pieces[c, p] = [BLUE_START_INDEX * c, piece_set[p]]

        self.player = Color.WHITE

    def get_initial_state(self):
        pieces = np.zeros((2, 5), dtype=np.uint8)
        for c in Color:
            piece_set = np.array(range(5))
            np.random.shuffle(piece_set)
            pieces[c] = piece_set + BLUE_START_INDEX * c

        player = Color.WHITE
        return (pieces, player)

    def get_board(self, pieces):
        board = np.zeros((25), dtype=np.int8)
        for i in range(5):
            if pieces[i] == 25:
                continue
            board[pieces[i]] = i + 1
        return board.reshape((5, 5))

    def print_state(self, pieces, color):
        print('Next player:', ['⚪', '🔵'][color])
        print('Tiles:')
        print(self.tiles)
        print('Pieces (blue = negative):')
        white = self.get_board(pieces[color])
        blue = self.get_board(pieces[1 - color])
        print(white - blue)

    def get_moves(self, pieces, color):
        movelist = []
        for i in range(5):
            p = pieces[color][i]
            initial_row = p // 5
            initial_col = p  % 5
            if initial_row == GOAL_ROW[color]:
                continue
            for dir in MOVE_DIRECTION:
                row = dir[0] + initial_row
                col = dir[1] + initial_col
                idx = row * 5 + col
                if row < 0 or row > 4 or col < 0 or col > 4 or idx in pieces[color]:
                    continue
                new_pieces = np.copy(pieces)
                new_pieces[color][i] = idx
                new_pieces[1 - color][new_pieces[1 - color] == idx] = 25
                movelist.append(new_pieces)
        return movelist
    

game = CIFRACode25()
pieces, color = game.get_initial_state()
game.print_state(pieces, color)
moves = game.get_moves(pieces, color)

i = 0
for move in moves:
    print('', i, ':')
    i += 1
    print(game.get_board(move[color]))
