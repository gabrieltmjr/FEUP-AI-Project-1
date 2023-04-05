import random
from copy import deepcopy
import numpy as np

WHITE = -1
BLUE = 1
NEUTRAL = 0
COLORS = [WHITE, BLUE, NEUTRAL]

CAPTURED = -1
temp = [False] * 20 + [True] * 5
IS_GOAL_ROW = [temp, temp[::-1]]

MOVE_DIRECTION = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if x or y]
MOVELIST = np.zeros((25, 8), dtype=int) + CAPTURED
for idx in range(25):
    orig_pos = np.array([idx // 5, idx % 5])
    for dir in range(8):
        pos = orig_pos + np.array(MOVE_DIRECTION[dir])
        if np.any((pos < 0) + (pos > 4)):
            continue
        MOVELIST[idx, dir] = pos[0] * 5 + pos[1]
MOVELIST = MOVELIST.T.tolist()



def get_board_representation(pieces):
    board = np.zeros((25), dtype=np.int8)
    for i in range(5):
        if pieces[i] == CAPTURED:
            continue
        board[pieces[i]] = i + 1
    return board.reshape((5, 5))

def print_state(state):
    print('Tiles:')
    tiles_arr = np.array([['⬛', '🟦', '⬜'][i] for i in state.board])
    print(tiles_arr.reshape(5, 5))
    print('Pieces (white = negative):')
    white = get_board_representation(state.pieces[0])
    blue = get_board_representation(state.pieces[1])
    print(blue - white)
    print('Next player:', [None, '🔵', '⚪'][state.current_player])

class CIFRACode25State():
    def __init__(self, game_mode):
        self.game_mode = game_mode
        CIFRACode25State.board = [WHITE, BLUE] * 12
        random.shuffle(CIFRACode25State.board)
        CIFRACode25State.board.insert(12, NEUTRAL)
        CIFRACode25State.game_mode = game_mode if game_mode in ['Sum', 'King'] else 'Dash'

        self.pieces = [list(range(5)), list(range(20, 25))]
        for i in range(2):
            random.shuffle(self.pieces[i])
        self.current_player = WHITE

    def get_current_player(self):
        return self.current_player

    def show_me_ya_moves(self):
        moves = []
        player_idx = self.current_player == BLUE
        opponent_idx = 1 - player_idx
        friendly, enemy = self.pieces if self.current_player == WHITE else self.pieces[::-1]
        for i in range(5):
            orig_pos = friendly[i]
            if IS_GOAL_ROW[player_idx][orig_pos]:
                continue
            for dir in MOVELIST:
                last_pos = orig_pos
                is_moveable = True
                while is_moveable:
                    next_pos = dir[last_pos]
                    if next_pos == CAPTURED or next_pos in friendly:
                        break
                    is_at_opponent_piece = next_pos in enemy
                    if is_at_opponent_piece and IS_GOAL_ROW[opponent_idx][next_pos]:
                        break
                    moves.append((i, next_pos))
                    is_moveable = self.board[last_pos] == self.current_player and self.board[next_pos] == self.current_player
                    last_pos = next_pos
        if len(moves) == 0:
            print_state(self.board, self.pieces, self.current_player)
            print(self.get_winner())
            print(self.is_terminal())
        return moves

    def make_move(self, move):
        new_state = deepcopy(self)
        piece_idx, board_idx = move
        player_idx = self.current_player == BLUE
        opponent_idx = 1 - player_idx
        new_state.pieces[player_idx][piece_idx] = board_idx
        for i in range(5):
            if new_state.pieces[opponent_idx][i] == board_idx:
                new_state.pieces[opponent_idx][i] = CAPTURED
                break
        new_state.current_player = self.current_player * (-1)
        return new_state

    def is_terminal(self):
        if self.game_mode == 'King':
            for i in range(2):
                king = self.pieces[i][4]
                if king == CAPTURED or IS_GOAL_ROW[i][king]:
                    return True
        else:
            for i in range(2):
                locked = 0
                for p in self.pieces[i]:
                    locked += p == CAPTURED or IS_GOAL_ROW[i][p]
                if locked == 5:
                    return True
        return False

    def get_winner(self):
        if self.game_mode == 'King':
            for i in range(2):
                king = self.pieces[i][4]
                if king == CAPTURED:
                    return COLORS[1 - i]
                if  IS_GOAL_ROW[i][king]:
                    return COLORS[i]
        goal = [0, 0]
        living = [0, 0]
        score = [0, 0]
        for i in range(2):
            for j in range(5):
                p = self.pieces[i][j]
                if p != CAPTURED:
                    goal[i] += IS_GOAL_ROW[i][p]
                    living[i] += 1
                    score[i] += j
        if self.game_mode == 'Sum' and score[0] != score[1]:
            return COLORS[score[1] > score[0]]
        if goal[0] != goal[1]:
            return COLORS[goal[1] > goal[0]]
        return COLORS[living[1] > living[0]]


