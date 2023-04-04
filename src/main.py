from CIFRA_Code25 import CIFRACode25State, print_state
from MonteCarloTreeSearch import MCTS
from view.View import Screen
if __name__=="__main__":
    #state = CIFRACode25State('Sum')
    #state = CIFRACode25State('Dash')
    state = CIFRACode25State('King')
    mcts = MCTS('seconds', 0.1)
    #mcts = MCTS('milliseconds', 1000)
    #mcts = MCTS('simulations', 500)
    screen = Screen()
   
    while not state.is_terminal():
        print_state(state)
        print()
        
        move = mcts.search(initial_state=state)
        print('Best move:')
        print(move)
        print()
        state = state.make_move(move) # e aqui está o proximo state
        screen.show_board(state.board)
    print_state(state)
    print(state.pieces)
    print(state.get_winner())
    
    state.pieces # peças tipo [ [23, 20, 4, 11, 10], [1, 2, 0, 15, -1] ], -1 significa que a peça tá capturada
    state.board # lista de cada tile no tabuleiro de 0 a 24, -1 é WHITE, 0 é a peça NEUTRAL do centro, 1 é BLUE