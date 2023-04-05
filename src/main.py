import pygame.event

from CIFRA_Code25 import CIFRACode25State, print_state
from MonteCarloTreeSearch import MCTS
from view.BoardView import BoardView
import time

def play_game(state,mcts,board_view,screen):
    running = True
    cell_size = 100
    while not state.is_terminal() and running is not False:
        print_state(state)
        board_view.show_board(state, screen, cell_size)
        move = mcts.search(initial_state=state)
        print('Best move:')
        print(move)
        state = state.make_move(move)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



    board_view.show_board(state, screen, cell_size)
    print_state(state)
    print("this is the pieces array")
    print(state.pieces)
    print(state.get_winner())


# def new_menu_option(option):

def draw_title(screen, blue, title_font, screen_width):
    title_text = title_font.render("Cifra Code 25", True, blue)
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 100))
    pygame.display.flip()

def draw_menu_option(screen, screen_width, black, blue, menu_font, menu_options, selected_option):
    # Draw the menu options
    for i in range(len(menu_options)):
        if i == selected_option:
            option_text = menu_font.render(menu_options[i], True, black)
        else:
            option_text = menu_font.render(menu_options[i], True, blue)
        screen.blit(option_text, (screen_width // 2 - option_text.get_width() // 2, 250 + 50 * i))
    pygame.display.flip()

def menu():
    # initialize game window
    pygame.display.init()
    # initialize font for text
    pygame.font.init()

    screen_width = 500
    screen_height = 500

    # create game window
    screen = pygame.display.set_mode([screen_width, screen_height])

    # title of window
    window_title = "Cifra"
    # set window caption
    pygame.display.set_caption(window_title)

    white = (200, 200, 200)
    blue = (14, 19, 117)
    black = (0, 0, 0)

    # update display
    pygame.display.flip()
    # Set the fonts
    title_font = pygame.font.SysFont(None, 60)
    menu_font = pygame.font.SysFont(None, 40)

    # Set the menu options
    menu_options = ["Dash", "Sum", "King", "Quit"]

    # Set the initial selected option
    selected_option = 0

    # Fill the screen with white color
    screen.fill(white)

    # Draw the title
    draw_title(screen, blue, title_font, screen_width)
    draw_menu_option(screen, screen_width, black, blue, menu_font, menu_options, selected_option)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get the current pressed keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            # Move the selection up
            selected_option = selected_option - 1
            if selected_option < 0 or selected_option > 4:
                selected_option = 3
            draw_menu_option(screen, screen_width, black, blue, menu_font, menu_options,
                             selected_option)
            time.sleep(0.3)
        elif keys[pygame.K_DOWN]:
            # Move the selection down
            selected_option = selected_option + 1
            if selected_option > 3:
                selected_option = 0
            draw_menu_option(screen, screen_width, black, blue, menu_font, menu_options,
                             selected_option)
            time.sleep(0.3)
        elif keys[pygame.K_RETURN]:
            # Check if "Play" option is selected
            if selected_option == 3:
                running = False
            else:
                mcts = MCTS('seconds', 0.3)
                if selected_option == 0:
                    state = CIFRACode25State('Dash')
                elif selected_option == 1:
                    state = CIFRACode25State('Sum')
                elif selected_option == 2:
                    state = CIFRACode25State('King')

                board_view = BoardView()
                play_game(state, mcts, board_view, screen)
                # Fill the screen with white color
                screen.fill(white)

                # Draw the title
                draw_title(screen, blue, title_font, screen_width)
                draw_menu_option(screen, screen_width, black, blue, menu_font, menu_options, selected_option)


if __name__ == "__main__":
    menu()