import pygame, sys
from pygame.locals import *
import time

# initializing global variables
XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255,255,255)
line_color = (10,10,10)
row = None
col = None

# tic tac toe board
board = [[None]*3, [None]*3, [None]*3]

# initializing pygame window
pygame.init()
fps = 30
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height + 100), 0)  # additional 100 in height for statusbar for viewing result
pygame.display.set_caption('Tic Tac Toe')

# loading the images
opening = pygame.image.load('opening.png')
x_img = pygame.image.load('x.png')
o_img = pygame.image.load('o.png')

# resizing the images
x_img = pygame.transform.scale(x_img, (80, 80))
o_img = pygame.transform.scale(o_img, (80, 80))
opening = pygame.transform.scale(opening, (width, height+100))

def game_opening():
    screen.blit(opening, (0,0))
    pygame.display.update()
    time.sleep(1)
    screen.fill(white)

    # drawing verical lines
    pygame.draw.line(screen, line_color, (width/3, 0), (width/3, height), 7)
    pygame.draw.line(screen, line_color, (width/3*2, 0), (width/3*2, height), 7)
    # drawing horizontal lines
    pygame.draw.line(screen, line_color, (0, height/3), (width, height/3), 7)
    pygame.draw.line(screen, line_color, (0, height/3*2), (width, height/3*2), 7)
    draw_status()

def draw_status():
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " Won!"

    if draw:
        message = "Game Draw!"        

    font = pygame.font.Font(None, 30)        
    text = font.render(message, 1, (255, 255, 255))

    # copy the render message onto the board
    screen.fill((0,0,0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50)) 
    screen.blit(text, text_rect)
    pygame.display.update()

def check_win():
    global board, winner, draw

    # check for winning row
    for row in range(3):
        if ((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            # this row won
            winner = board[row][0]
            # draw winnig line
            pygame.draw.line(screen, (255, 0, 0), (0, (row + 1) * height/3 - height/6),(width, (row + 1)* height/3 - height/6), 4)
            break

    # check for winning column
    for col in range(3):
        if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None):
            # this column won
            winner = board[0][col]
            # draw winning line
            pygame.draw.line(screen, (255, 0, 0), ((col + 1) * width/3 - width/6, 0),((col + 1)* width/3 - width/6, height), 4)
            break

    # check for win in diagonal
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        # this diagonally won left to right
        winner = board[0][0]
        # drawing winnig line
        pygame.draw.line(screen, (255, 70, 70), (50, 50), (350, 350), 4)
    
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        # this diagonal won right to left
        winner = board[0][2]
        # drawing winning line
        pygame.draw.line(screen, (255, 70, 70), (350, 50), (50, 350), 4)

    if (all([all(row) for row in board]) and winner is None):
        draw = True
    draw_status()        

def draw_xo(row, col):
    global board, XO
    if row == 1:
        posx = 30
    if row == 2:
        posx = width/3 + 30
    if row == 3:
        posx = width/3*2 + 30

    if col == 1:
        posy = 30
    if col == 2:
        posy = height/3 + 30
    if col == 3:
        posy = height/3*2 + 30 

    board[row -1][col-1] = XO
    if (XO =='x'):
        screen.blit(x_img, (int(posy), int(posx)))
        XO = 'o'
    else:
        screen.blit(o_img, (int(posy), int(posx)))
        XO = 'x'
    pygame.display.update()
    print(posx, posy)
    print(board)

def user_click():
    # get co-ordinates of mouse click
    x, y = pygame.mouse.get_pos()

    # get column of the mouse click(1-3)
    if (x < width/3):
        col = 1
    elif (x < width/3*2):
        col = 2
    elif (x < width):
        col = 3
    else:
        col = None
    
    # get row of the mouse click(1-3)
    if (y < height/3):
        row = 1
    elif (y < height/3*2):
        row = 2
    elif (y < height):
        row = 3
    else:
        col = None
    # print(row, col)        

    if (row and col and board[row - 1][col - 1] is None):
        global XO
        # draw x or o on the screen
        draw_xo(row, col)
        check_win()

def reset_game():
    global board, winner, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_opening()
    winner = None
    board = [[None]*3, [None]*3, [None]*3]

game_opening()

# running the game in a continuous loop
while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type is MOUSEBUTTONDOWN:
            # user click, place x or o
            user_click()
            if (winner or draw):
                reset_game()
    pygame.display.update()
    clock.tick(fps)




















