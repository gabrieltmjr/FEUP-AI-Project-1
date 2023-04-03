from ast import Pass
import time
import math
import random
from copy import deepcopy
from functools import reduce
import operator
import numpy as np


def pick_random_move(state):
    while not state.is_terminal():
        move = random.choice(state.show_me_ya_moves())
        state = state.make_move(move)
    return state.get_winner()


class Node():
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.children = {}
        self.num_visits = 0
        self.total_reward = 0
        self.is_terminal = state.is_terminal()
        self.is_fully_expanded = self.is_terminal

class mcts():
    def __init__(self, limit_type, limit, exploration_constant=(1 / math.sqrt(2)), rollout_func=pick_random_move):
        self.limit_type = limit_type
        if limit_type == 'time':
            self.time_limit = max(1, limit) / 1000
        elif limit_type == 'sims':
            self.num_sims = max(1, int(limit))
        self.exploration_constant = exploration_constant
        self.rollout = rollout_func

    def search(self, initial_state):
        self.root = Node(initial_state, None)

        if self.limit_type == 'time':
            time_limit = time.time() + self.time_limit
            while time.time() < time_limit:
                self.run_round()
        else:
            for i in range(self.num_sims):
                self.run_round()

        best_child = self.get_best_child(self.root, 0)
        move = (move for move, node in self.root.children.items() if node is best_child).__next__()
        return move

    def run_round(self):
        node = self.select(self.root)
        reward = self.rollout(node.state)
        self.backpropagate(node, reward)

    def select(self, node):
        while not node.is_terminal:
            if node.is_fully_expanded:
                node = self.get_best_child(node, self.exploration_constant)
            else:
                return self.expand(node)
        return node

    def expand(self, node):
        moves = node.state.show_me_ya_moves()
        for move in moves:
            if move not in node.children:
                new_node = Node(node.state.make_move(move), node)
                node.children[move] = new_node
                if len(moves) == len(node.children):
                    node.is_fully_expanded = True
                return new_node

    def backpropagate(self, node, reward):
        while node is not None:
            node.num_visits += 1
            node.total_reward += reward
            node = node.parent

    def get_best_child(self, node, exploration_constant):
        best_value = float("-inf")
        best_nodes = []
        for child in node.children.values():
            node_value = node.state.get_current_player() * child.total_reward / child.num_visits + exploration_constant * math.sqrt(
                2 * math.log(node.num_visits) / child.num_visits)
            if node_value > best_value:
                best_value = node_value
                best_nodes = [child]
            elif node_value == best_value:
                best_nodes.append(child)
        return random.choice(best_nodes)

WHITE = -1
BLUE = 1
NEUTRAL = 0
COLORS = [WHITE, BLUE, NEUTRAL]

DASH = 1
SUM = 2
KING = 3

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

def print_state(board, pieces, player):
    print('Tiles:')
    tiles_arr = np.array([['⬛', '🟦', '⬜'][i] for i in board])
    print(tiles_arr.reshape(5, 5))
    print('Pieces (white = negative):')
    white = get_board_representation(pieces[0])
    blue = get_board_representation(pieces[1])
    print(blue - white)
    print('Next player:', [None, '🔵', '⚪'][player])

class CIFRACode25State():
    def __init__(self, game_mode):
        self.board = [WHITE, BLUE] * 12
        random.shuffle(self.board)
        self.board.insert(12, NEUTRAL)
        self.game_mode = game_mode

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
        if self.game_mode == KING:
            for i in range(2):
                king = self.pieces[i][4]
                if king == CAPTURED or IS_GOAL_ROW[i][king]:
                    return True
        else:
            for i in range(2):
                locked = 0
                for j in self.pieces[i]:
                    locked += j == CAPTURED or IS_GOAL_ROW[i][j]
                if locked == 5:
                    return True
        return False

    def get_winner(self):
        if self.game_mode == KING:
            for i in range(2):
                king = self.pieces[i][4]
                if king == CAPTURED:
                    return COLORS[1 - i]
                if  IS_GOAL_ROW[i][king]:
                    return COLORS[i]
        goal = [0, 0]
        alive = [0, 0]
        score = [0, 0]
        for i in range(2):
            for j in range(5):
                p = self.pieces[i][j]
                if p != CAPTURED:
                    goal[i] += IS_GOAL_ROW[i][p]
                    alive[i] += 1
                    score[i] += j
        if self.game_mode == SUM and score[0] != score[1]:
            return COLORS[score[1] > score[0]]
        if goal[0] != goal[1]:
            return COLORS[goal[1] > goal[0]]
        return COLORS[alive[1] > alive[0]]




if __name__=="__main__":
    cifra_initial_state = CIFRACode25State(SUM)
    cifra_searcher = mcts('sims', 1000)
    cifra_move = cifra_searcher.search(initial_state=cifra_initial_state)
    print(cifra_move)
    