import math
import random
import time


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

class MCTS():
    def __init__(self, limit_type, limit, exploration_constant=(1 / math.sqrt(2)), rollout_func=pick_random_move):
        if limit_type == 'seconds':
            self.limit_type = 'time'
            self.time_limit = max(0.001, limit)
        elif limit_type == 'milliseconds':
            self.limit_type = 'time'
            self.time_limit = max(1, limit) / 1000
        elif limit_type == 'simulations':
            self.limit_type = 'sims'
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