import math
import random
import time
import numpy as np
from copy import deepcopy

NUM_ROWS = 6
NUM_COLS = 7

class State:
    
    def __init__(self):
        # initialize the board info here and any additional variables
        self.board = np.zeros((NUM_ROWS, NUM_COLS)) # board initial state (all zeros)
        self.column_heights = [NUM_ROWS - 1] * NUM_COLS # useful to keep track of the index in which pieces should be inserted
        self.available_moves = list(range(7)) # list of playable columns (not full)
        self.player = 1
        self.winner = -1 # -1 - no winner (during game); 0 - draw; 1- player 1; 2 - player 2
        
    def move(self, column): 
        # function that performs a move given the column number and returns the new state
        # do not forget to update the available moves list, column heights, pass the turn and check for winners
        state_copy = deepcopy(self)
        
        height = state_copy.column_heights[column]
        state_copy.column_heights[column] = height
        state_copy.board[height][column] = self.player
        
        if height == 0:
            state_copy.available_moves.remove(column)
        else:
            state_copy.column_heights[column] = height - 1
        
        state_copy.update_winner() 
        state_copy.player = 3 - self.player # update player turn
        
        return state_copy
    
    def update_winner(self):
        # function that tests objective and update the winner accordingly
        # sholud return 1, 2 or 0 (draw)
        for i in range(1, 3):
            if self.count_lines(4, i):
                self.winner = i
                return i
        if len(self.available_moves) == 0:
            self.winner = 0
            return 0

    
    def check_line(self, n, player, values):
        num_pieces = sum(list(map(lambda val: val == player, values)))
        if n == 4:
            return num_pieces == 4
        if n == 3:
            num_empty_spaces = sum(list(map(lambda val: val == 0, values)))
            return num_pieces == 3 and num_empty_spaces == 1
    
    # c1) c2)
    def count_lines(self, n, player):
        num_lines = 0
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if col < NUM_COLS - 3 and self.check_line(n, player, [self.board[row][col], self.board[row][col+1], self.board[row][col+2], self.board[row][col+3]]):
                    num_lines += 1
                if row < NUM_ROWS - 3 and self.check_line(n, player, [self.board[row][col], self.board[row+1][col], self.board[row+2][col], self.board[row+3][col]]):
                    num_lines += 1
                if col < NUM_COLS - 3 and row < NUM_ROWS - 3 and self.check_line(n, player, [self.board[row][col], self.board[row+1][col+1], self.board[row+2][col+2], self.board[row+3][col+3]]):
                    num_lines += 1
        return num_lines
    
    # c3)
    def central(self, player):
        columns = [2,3,4]
        points = [1,2,1]
        total = 0
        for i in range(3):
            total += points[i] * np.count_nonzero(self.board[:,columns[i]] == player)
        return total

class ConnectFourGame:
    
    def __init__(self, player_1_ai, player_2_ai):
        self.state = State()
        self.player_1_ai = player_1_ai
        self.player_2_ai = player_2_ai
        
    def start(self, log_moves = False):
        self.state = State()
        while True:
            if self.state.player == 1:
                self.player_1_ai(self)
            else:
                self.player_2_ai(self)
            
            if log_moves:
                print(game.state.board)
            
            if self.state.winner != -1:
                break
        
        if self.state.winner == 0:
            print("End of game! Draw!")
        else:
            print(f"End of game! Player {self.state.winner} wins!")
    
    def run_n_matches(self, n, max_time = 3600, log_moves = False):
        start_time = time.time()
        
        results = [0, 0, 0] # [draws, player 1 victories, player 2 victories]
        
        for i in range(n):
            if time.time() - start_time > 3600:
                break
            self.start(log_moves)
            results[self.state.winner] += 1
     
        print("\n=== Elapsed time: %s seconds ===" % (int(time.time() - start_time)))
        print(f"  Player 1: {results[1]} victories")
        print(f"  Player 2: {results[2]} victories")
        print(f"  Draws: {results[0]} ")
        print("===============================")
               
""" 
    Heuristic functions - e)
"""

def evaluate_f1(state):
    return state.count_lines(4, 1) - state.count_lines(4, 2)

def evaluate_f2(state):
    return (state.count_lines(4, 1) - state.count_lines(4, 2)) * 100 + state.count_lines(3, 1) - state.count_lines(3, 2)

def evaluate_f3(state):
    return 100 * evaluate_f1(state) + state.central(1) - state.central(2)

def evaluate_f4(state):
    return 5 * evaluate_f2(state) + evaluate_f3(state)     

""" 
    Move selection methods
"""
    
def execute_random_move(game):
    move = random.choice(game.state.available_moves)
    game.state = game.state.move(move)
    
def execute_minimax_move(game, evaluate_func, depth):
    maxEval = -math.inf
    maxState = None
    for move in game.state.available_moves:
        state = game.state.move(move)
        currEval = minimax(state, depth, -math.inf, math.inf, True, state.player, evaluate_func)
        if currEval > maxEval:
            maxEval = currEval
            maxState = state
    game.state = maxState

def minimax(state, depth, alpha, beta, maximizing, player, evaluate_func):
    if depth == 0 or state.winner != -1:
        return evaluate_func(state)
    minimaxEval = math.inf * [1, -1][maximizing]
    for move in state.available_moves:
        state = state.move(move)
        evaluation = minimax(state, depth - 1, alpha, beta, not maximizing, state.player, evaluate_func)
        minimaxEval = [min, max][maximizing](minimaxEval, evaluation)
        if maximizing:
            alpha = max(alpha, evaluation)
        else:
            beta = min(beta, evaluation)
        if beta <= alpha:
            break
    return minimaxEval


print("You thought it was CIFRA-Code25... But it was me! Connect 4!!!!!")
print()


print("Random vs random")
game = ConnectFourGame(execute_random_move, execute_random_move)
game.run_n_matches(10, 120, False)

print("Minimax (f1, depth = 2) vs random")
game = ConnectFourGame(lambda x: execute_minimax_move(x, evaluate_f1, 2), execute_random_move)
game.run_n_matches(10, 120)

print("Minimax (f2, depth = 2) vs random")
game = ConnectFourGame(lambda x: execute_minimax_move(x, evaluate_f2, 2), execute_random_move)
game.run_n_matches(10, 120)

print("Minimax (f3, depth = 2) vs random")
game = ConnectFourGame(lambda x: execute_minimax_move(x, evaluate_f3, 2), execute_random_move)
game.run_n_matches(10, 120)

print("Minimax (f4, depth = 2) vs random")
game = ConnectFourGame(lambda x: execute_minimax_move(x, evaluate_f4, 2), execute_random_move)
game.run_n_matches(10, 120)

print("Minimax (f1, depth = 2) vs Minimax (f4, depth = 2)")
game = ConnectFourGame(lambda x: execute_minimax_move(x, evaluate_f1, 2), lambda x: execute_minimax_move(x, evaluate_f4, 2))
game.run_n_matches(5, 120)

print("Minimax (f4, depth = 2) vs Minimax (f4, depth = 4)")
game = ConnectFourGame(lambda x: execute_minimax_move(x, evaluate_f4, 2), lambda x: execute_minimax_move(x, evaluate_f4, 4))
game.run_n_matches(3, 240, True)