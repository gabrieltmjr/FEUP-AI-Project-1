import pygame
import random
import numpy as np
class Screen:
    def __init__(self):
        # screen dimensions
        
        self.board_color = np.random.randint(0, 2, size=(5, 5))
        
        self.screen_width = 500
        self.screen_height = 500
        self.blueTile = pygame.image.load('./img/0.png')
        self.whiteTile = pygame.image.load('img/1.png')
     
        # flag to know if game menu has been showed
        self.menu_showed = False
        # flag to set game loop
        self.running = True
        # base folder for program resources
        self.resources = "res"
 
        # initialize game window
        pygame.display.init()
        # initialize font for text
        pygame.font.init()

        # create game window
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])

        # title of window
        window_title = "Cifra"
        # set window caption
        pygame.display.set_caption(window_title)

        # update display
        pygame.display.flip()
        
        
    def show_board(self,board):
        
        
        for line in range(0,len(board)):
            row = line%4
            print(row)
# paint screen one time
        pygame.display.flip()        