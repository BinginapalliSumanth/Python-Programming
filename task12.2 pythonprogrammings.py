import pygame
import sys

# Initialize pygame
pygame.init()

# Set screen size and title
screen_size = (640, 640)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Chess Board (Text Pieces)')

# Define colors
white = (255, 255, 255)
brown = (153, 76, 0)
black = (0, 0, 0)

# Define font for piece letters
font = pygame.font.SysFont('arial', 48, bold=True)

# Define function to draw the board
def draw_board():
    for row in range(8):
        for col in range(8):
            color = white if (row + col) % 2 == 0 else brown
            square_rect = pygame.Rect(col * 80, row * 80, 80, 80)
            pygame.draw.rect(screen, color, square_rect)

# Mapping pieces to letters and colors
piece_labels = {
    'r': ('R', black), 'n': ('N', black), 'b': ('B', black),
    'q': ('Q', black), 'k': ('K', black), 'p': ('P', black),
    'R': ('R', white), 'N': ('N', white), 'B': ('B', white),
    'Q': ('Q', white), 'K': ('K', white), 'P': ('P', white)
}

# Function to draw pieces as text
def draw_pieces(board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != '.':
                label, color = piece_labels[piece]
                text_surface = font.render(label, True, color)
                text_rect = text_surface.get_rect(center=(col * 80 + 40, row * 80 + 40))
                screen.blit(text_surface, text_rect)

# Initial board state
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

# Main loop
running = True
while running:
    draw_board()
    draw_pieces(board)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
sys.exit()
