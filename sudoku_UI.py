import pygame

pygame.init()
screen = pygame.display.set_mode((630, 710))
pygame.display.set_caption("Sudoku")
# Define buttons rects globally for use outside the function
easy_button = pygame.Rect(70, 405, 130, 50)
medium_button = pygame.Rect(250, 405, 130, 50)
hard_button = pygame.Rect(430, 405, 130, 50)

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

reset_button = pygame.Rect(70, 650, 130, 40)
restart_from_the_game_screen_button = pygame.Rect(250, 650, 130, 40)
exit_from_the_game_screen_button = pygame.Rect(430, 650, 130, 40)
def game_screen():
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



waiting = True
def if_start_screen(waiting):
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    game_screen()

                if medium_button.collidepoint(event.pos):
                    game_screen()

                if hard_button.collidepoint(event.pos):
                    game_screen()


start_screen()
if_start_screen(waiting)
game_screen()

waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reset_button.collidepoint(event.pos):
                waiting = False
            if restart_from_the_game_screen_button.collidepoint(event.pos):
                start_screen()
                if_start_screen(waiting)
                waiting = False
            if exit_from_the_game_screen_button.collidepoint(event.pos):
                waiting = False

game_over_screen()

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()