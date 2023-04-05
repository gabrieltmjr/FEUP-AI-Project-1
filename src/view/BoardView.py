import pygame
import numpy as np

class BoardView:
    def __init__(self):
        self.blue_tile = pygame.image.load('img/white_tile.png')
        self.white_tile = pygame.image.load('img/blue_tile.png')
        self.center_tile = pygame.image.load('img/center_tile.png')
        self.white_piece = pygame.image.load('img/white_piece.png')
        self.light_blue_piece = pygame.image.load('img/light_blue_piece.png')
        self.white_piece_king = pygame.image.load('img/white_piece_king.png')
        self.white_piece_sum_1 = pygame.image.load('img/white_piece_sum_1.png')
        self.white_piece_sum_2 = pygame.image.load('img/white_piece_sum_2.png')
        self.white_piece_sum_3 = pygame.image.load('img/white_piece_sum_3.png')
        self.white_piece_sum_4 = pygame.image.load('img/white_piece_sum_4.png')
        self.white_piece_sum_5 = pygame.image.load('img/white_piece_sum_5.png')
        self.light_blue_piece_king = pygame.image.load('img/light_blue_piece_king.png')
        self.light_blue_piece_sum_1 = pygame.image.load('img/light_blue_piece_sum_1.png')
        self.light_blue_piece_sum_2 = pygame.image.load('img/light_blue_piece_sum_2.png')
        self.light_blue_piece_sum_3 = pygame.image.load('img/light_blue_piece_sum_3.png')
        self.light_blue_piece_sum_4 = pygame.image.load('img/light_blue_piece_sum_4.png')
        self.light_blue_piece_sum_5 = pygame.image.load('img/light_blue_piece_sum_5.png')

    def calculate_position(self, number):
        row = number // 5
        col = number % 5
        return row, col
    def show_board(self, state, screen,cell_size):
        self.cell_size = cell_size
        self.screen = screen
        double_array_board = [state.board[i:i+5] for i in range(0, len(state.board), 5)]
        for row in range(5):
            for col in range(5):
                number = double_array_board[row][col]
                if number == -1:
                    self.screen.blit(self.blue_tile, (col * self.cell_size, row * self.cell_size))
                elif number == 0:
                    self.screen.blit(self.center_tile, (col * self.cell_size, row * self.cell_size))
                elif number == 1:
                    self.screen.blit(self.white_tile, (col * self.cell_size, row * self.cell_size))

        for row in range(2):
            for col in range(5):
                number = state.pieces[row][col]
                if number == -1:
                    continue
                else:
                    position = self.calculate_position(number)
                    other_row = position[0]
                    other_col = position[1]
                    if state.game_mode == 'Dash':
                        if row == 0:
                            self.screen.blit(self.white_piece, (other_col * self.cell_size, other_row * self.cell_size))
                        elif row == 1:
                            self.screen.blit(self.light_blue_piece,
                                             (other_col * self.cell_size, other_row * self.cell_size))
                    elif state.game_mode == 'King':
                        if col == 4:
                            if row == 0:
                                self.screen.blit(self.white_piece_king,
                                                 (other_col * self.cell_size, other_row * self.cell_size))
                            elif row == 1:
                                self.screen.blit(self.light_blue_piece_king,
                                                 (other_col * self.cell_size, other_row * self.cell_size))
                        else:
                            if row == 0:
                                self.screen.blit(self.white_piece,
                                                 (other_col * self.cell_size, other_row * self.cell_size))
                            elif row == 1:
                                self.screen.blit(self.light_blue_piece,
                                                 (other_col * self.cell_size, other_row * self.cell_size))
                    elif state.game_mode == 'Sum':
                        if col == 0:
                            if row == 0:
                                self.screen.blit(self.white_piece_sum_1,
                                                 (other_col * self.cell_size, other_row * self.cell_size))
                            elif row == 1:
                                self.screen.blit(self.light_blue_piece_sum_1,
                                                 (other_col * self.cell_size, other_row * self.cell_size))
                        elif col == 1:
                            if row == 0:
                                self.screen.blit(self.white_piece_sum_2,
                                                 (other_col * self.cell_size, other_row * self.cell_size))
                            elif row == 1:
                                self.screen.blit(self.light_blue_piece_sum_2,
                                                 (other_col * self.cell_size, other_row * self.cell_size))
                        elif col == 2:
                            if row == 0:
                                self.screen.blit(self.white_piece_sum_3,
                                                 (other_col * self.cell_size, other_row * self.cell_size))
                            elif row == 1:
                                self.screen.blit(self.light_blue_piece_sum_3,
                                                 (other_col * self.cell_size, other_row * self.cell_size))
                        elif col == 3:
                            if row == 0:
                                self.screen.blit(self.white_piece_sum_4,
                                                 (other_col * self.cell_size, other_row * self.cell_size))
                            elif row == 1:
                                self.screen.blit(self.light_blue_piece_sum_4,
                                                 (other_col * self.cell_size, other_row * self.cell_size))
                        if col == 4:
                            if row == 0:
                                self.screen.blit(self.white_piece_sum_5,
                                                 (other_col * self.cell_size, other_row * self.cell_size))
                            elif row == 1:
                                self.screen.blit(self.light_blue_piece_sum_5,
                                                 (other_col * self.cell_size, other_row * self.cell_size))

        pygame.display.flip()