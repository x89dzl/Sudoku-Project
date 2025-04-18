import pygame

pygame.init()
screen = pygame.display.set_mode((630, 710))
pygame.display.set_caption("Sudoku")
# Store sketched values (None if empty)
sketched_grid = [[None for i in range(9)] for i in range(9)]
# Store confirmed (submitted) numbers
confirmed_grid = [[None for i in range(9)] for i in range(9)]
# Mark which cells are locked from editing
#!!! Need to add this value to all numbers that were put by the program
locked_cells = [[False for i in range(9)] for i in range(9)]
# Define buttons rects globally for use outside the function
easy_button = pygame.Rect(70, 405, 130, 50)
medium_button = pygame.Rect(250, 405, 130, 50)
hard_button = pygame.Rect(430, 405, 130, 50)
# start screen
def start_screen():
    #Insert the image
    sudoku_image = pygame.image.load('sudoku_image.jpg')
    screen.blit(sudoku_image,(0,0))
    #Write the text
    font = pygame.font.SysFont(None, 80)
    text = font.render("Welcome to Sudoku", True, 'orange')
    text_rect = text.get_rect(center=(315, 170))
    screen.blit(text, text_rect)
    font = pygame.font.SysFont(None, 70)
    text = font.render("Select Game Mode:", True, 'orange')
    text_rect = text.get_rect(center=(315, 270))
    screen.blit(text, text_rect)
    #Draw the buttons
    pygame.draw.rect(screen, "dark orange", (55, 395, 160, 70))
    pygame.draw.rect(screen, "white", (60,400,150,60))
    pygame.draw.rect(screen, "orange", easy_button)
    font = pygame.font.SysFont(None, 35)
    text = font.render("EASY", True, 'black')
    text_rect = text.get_rect(center=(135, 431))
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, "dark orange", (235, 395, 160, 70))
    pygame.draw.rect(screen, "white", (240,400,150,60))
    pygame.draw.rect(screen, "orange", medium_button)
    font = pygame.font.SysFont(None, 35)
    text = font.render("MEDIUM", True, 'black')
    text_rect = text.get_rect(center=(315, 431))
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, "dark orange", (415, 395, 160, 70))
    pygame.draw.rect(screen, "white", (420,400,150,60))
    pygame.draw.rect(screen, "orange", hard_button)
    font = pygame.font.SysFont(None, 35)
    text = font.render("HARD", True, 'black')
    text_rect = text.get_rect(center=(495, 431))
    screen.blit(text, text_rect)
    pygame.display.flip()

# Define buttons rects globally for use outside the function
reset_button = pygame.Rect(70, 650, 130, 40)
restart_from_the_game_screen_button = pygame.Rect(250, 650, 130, 40)
exit_from_the_game_screen_button = pygame.Rect(430, 650, 130, 40)

selected_cell_row = None
selected_cell_col = None
# Game screen
def game_screen(selected_cell_row = None, selected_cell_col = None):
    screen.fill('white')
#draw horizontal lines
    for i in range(1, 9):
        pygame.draw.line(screen,
        'black',
        (0, i * 70),
        (630, i * 70),
        2
        )
#draw BOLD horizontal lines
    for i in range(3, 10, 3):
        pygame.draw.line(screen,
        'black',
        (0, i * 70),
        (630, i * 70),
        5
        )
#draw vertical lines
    for i in range(1, 9):
        pygame.draw.line(
        screen,
        'black',
        (i * 70, 0),
        (i * 70, 630),
        2
        )
# draw BOLD vertical lines
    for i in range(3, 9, 3):
        pygame.draw.line(
        screen,
        'black',
        (i * 70, 0),
        (i * 70, 630),
        5
        )
# Showing the selected square
    if selected_cell_row is not None and selected_cell_col is not None:
        # find the coordinates of the square to be highlighted
        cell_x = selected_cell_col * 70
        cell_y = selected_cell_row * 70
        # Draw a highlighted border around the selected cell
        pygame.draw.rect(screen, "orange", (cell_x, cell_y, 70, 70), 4)

#drawing the skratch number in the square
    font = pygame.font.SysFont(None, 110)
    for row in range(9):
        for col in range(9):
            if sketched_grid[row][col] is not None:
                x = col * 70 + 14
                y = row * 70 + 2
                text = font.render(str(sketched_grid[row][col]), True, 'gray')
                screen.blit(text, (x, y))
#drawing confirmed numbers
    font_bold = pygame.font.SysFont(None, 110)
    for row in range(9):
        for col in range(9):
            if confirmed_grid[row][col] is not None:
                x = col * 70 + 14
                y = row * 70 + 2
                text = font_bold.render(str(confirmed_grid[row][col]), True, 'black')
                screen.blit(text, (x, y))
#Draw the buttons
    pygame.draw.rect(screen, "dark orange", (55, 640, 160, 60))
    pygame.draw.rect(screen, "white", (60,645,150,50))
    pygame.draw.rect(screen, "orange", reset_button)
    font = pygame.font.SysFont(None, 35)
    text = font.render("RESET", True, 'black')
    text_rect = text.get_rect(center=(135, 671))
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, "dark orange", (235, 640, 160, 60))
    pygame.draw.rect(screen, "white", (240,645,150,50))
    pygame.draw.rect(screen, "orange", restart_from_the_game_screen_button)
    font = pygame.font.SysFont(None, 35)
    text = font.render("RESTART", True, 'black')
    text_rect = text.get_rect(center=(315, 671))
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, "dark orange", (415, 640, 160, 60))
    pygame.draw.rect(screen, "white", (420,645,150,50))
    pygame.draw.rect(screen, "orange",exit_from_the_game_screen_button)
    font = pygame.font.SysFont(None, 35)
    text = font.render("EXIT", True, 'black')
    text_rect = text.get_rect(center=(495, 671))
    screen.blit(text, text_rect)
    pygame.display.flip()


#Lost game screen
def game_over_screen():
# Insert the image
    sudoku_image = pygame.image.load('sudoku_image.jpg')
    screen.blit(sudoku_image, (0, 0))
# Write the text
    font = pygame.font.SysFont(None, 100)
    text = font.render("Game Over :(", True, 'orange')
    text_rect = text.get_rect(center=(315, 200))
    screen.blit(text, text_rect)

# Draw the button
    pygame.draw.rect(screen, "dark orange", (235, 295, 210, 90))
    pygame.draw.rect(screen, "white", (240, 300, 200, 80))
    pygame.draw.rect(screen, "orange", (250, 305, 180, 70))
    font = pygame.font.SysFont(None, 35)
    text = font.render("RESTART", True, 'black')
    text_rect = text.get_rect(center=(340, 341))
    screen.blit(text, text_rect)
    pygame.display.flip()

#Won game screen
def game_won_screen():
# Insert the image
    sudoku_image = pygame.image.load('sudoku_image.jpg')
    screen.blit(sudoku_image, (0, 0))
# Write the text
    font = pygame.font.SysFont(None, 100)
    text = font.render("Game Won!", True, 'orange')
    text_rect = text.get_rect(center=(315, 200))
    screen.blit(text, text_rect)
# Draw the button
    pygame.draw.rect(screen, "dark orange", (235, 295, 210, 90))
    pygame.draw.rect(screen, "white", (240, 300, 200, 80))
    pygame.draw.rect(screen, "orange", (250, 305, 180, 70))
    font = pygame.font.SysFont(None, 35)
    text = font.render("EXIT", True, 'black')
    text_rect = text.get_rect(center=(340, 341))
    screen.blit(text, text_rect)
    pygame.display.flip()
# clear all inputs
def reset_board():
    global sketched_grid, confirmed_grid, locked_cells
    global selected_cell_row, selected_cell_col

    sketched_grid = [[None for i in range(9)] for i  in range(9)]
    confirmed_grid = [[None for i in range(9)] for i in range(9)]
    locked_cells = [[False for i in range(9)] for i in range(9)]
    selected_cell_row = None
    selected_cell_col = None


STATE = "start"

running = True
while running:
# Setting three states of the game
    if STATE == "start":
        start_screen()
    elif STATE == "game":
        game_screen(selected_cell_row, selected_cell_col)
    elif STATE == "exit":
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if STATE == "start":
#!!! add functions to create the sudoku according to the difficulty level
                if easy_button.collidepoint(event.pos):
                    STATE = "game"
                elif medium_button.collidepoint(event.pos):
                    STATE = "game"
                elif hard_button.collidepoint(event.pos):
                    STATE = "game"
# actions on the game board
            elif STATE == "game":
                if reset_button.collidepoint(event.pos):
                    reset_board()
                    STATE = "game"
                elif restart_from_the_game_screen_button.collidepoint(event.pos):
                    reset_board()
                    STATE = "start"
                elif exit_from_the_game_screen_button.collidepoint(event.pos):
                    STATE = "exit"
#selecting a square by clicking
                else:
                    if event.pos[0] < 630 and event.pos[1] < 630:
                        selected_cell_col = event.pos[0] // 70
                        selected_cell_row = event.pos[1] // 70
# !!! Edit when the function if the game is over or the user won is added
            elif STATE == "won":
                game_won_screen()
            elif STATE == "lost":
                game_over_screen()
# Actions on the keyboard
        elif event.type == pygame.KEYDOWN:
            if STATE == "game" and selected_cell_row is not None:
#selecting the square by arrow keys
                if event.key == pygame.K_LEFT and selected_cell_col is not None:
                    selected_cell_col -= 1
                elif event.key == pygame.K_RIGHT and selected_cell_col is not None:
                    selected_cell_col += 1
                elif event.key == pygame.K_UP and selected_cell_row is not None:
                    selected_cell_row -= 1
                elif event.key == pygame.K_DOWN and selected_cell_row is not None:
                    selected_cell_row += 1
#typing in the value
                if event.unicode != '' and event.unicode in '123456789':
                    if not locked_cells[selected_cell_row][selected_cell_col]:
                        sketched_grid[selected_cell_row][selected_cell_col] = int(event.unicode)
#submitting the value
                if event.key == pygame.K_RETURN:
                    if sketched_grid[selected_cell_row][selected_cell_col] is not None and not locked_cells[selected_cell_row][selected_cell_col]:
                        confirmed_grid[selected_cell_row][selected_cell_col] = sketched_grid[selected_cell_row][selected_cell_col]
                        locked_cells[selected_cell_row][selected_cell_col] = True
                        sketched_grid[selected_cell_row][selected_cell_col] = None

pygame.quit()
