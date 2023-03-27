# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 11:25:35 2023

@author: Antonio Augusto
"""

import pygame

class Screen:
    def __init__(self):
        # screen dimensions
        screen_width = 500
        screen_height = 500
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
        self.screen = pygame.display.set_mode([screen_width, screen_height])

        # title of window
        window_title = "Cifra"
        # set window caption
        pygame.display.set_caption(window_title)

        # update display
        pygame.display.flip()
        
        
        
    