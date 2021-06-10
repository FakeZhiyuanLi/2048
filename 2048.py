import pygame
import random
import os


pygame.init()

# Main Variables
WIDTH = 1000
HEIGHT = 1000
tile_gotten = False

layers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Tile Variables
clock = pygame.time.Clock()
window = pygame.display.set_mode([WIDTH, HEIGHT])
TWO = pygame.transform.scale(pygame.image.load(os.path.join('2048', 'Assets', '2.png')), (150, 150))
FOUR = pygame.transform.scale(pygame.image.load(os.path.join('2048', 'Assets', '4.png')), (150, 150))
EIGHT = pygame.transform.scale(pygame.image.load(os.path.join('2048', 'Assets', '8.png')), (150, 150))
SIXTEEN = pygame.transform.scale(pygame.image.load(os.path.join('2048', 'Assets', '16.png')), (150, 150))
THIRTYTWO = pygame.transform.scale(pygame.image.load(os.path.join('2048', 'Assets', '32.png')), (150, 150))
SIXTYFOUR = pygame.transform.scale(pygame.image.load(os.path.join('2048', 'Assets', '64.png')), (150, 150))
ONEHUNDREDTWENTYEIGHT = pygame.transform.scale(pygame.image.load(os.path.join('2048', 'Assets', '128.png')), (150, 150))
TWOHUNDREDFIFTYSIX = pygame.transform.scale(pygame.image.load(os.path.join('2048', 'Assets', '256.png')), (150, 150))
FIVEHUNDREDTWELVE = pygame.transform.scale(pygame.image.load(os.path.join('2048', 'Assets', '512.png')), (150, 150))
ONETHOUSANDTWENTYFOUR = pygame.transform.scale(pygame.image.load(os.path.join('2048', 'Assets', '1024.png')), (150, 150))
TWOTHOUSANDFOURTYEIGHT = pygame.transform.scale(pygame.image.load(os.path.join('2048', 'Assets', '2048.png')), (150, 150))


# Outline variables
OUTLINE = pygame.Rect(WIDTH / 2 - 300, HEIGHT / 2 - 300, 600, 600)

WHITE = (255, 255, 255)
OUTLINE_COLOR = (107, 107, 107)

def DRAW_WINDOW():

    # Testing images

    window.fill(WHITE)
    window.blit(TWO, (200, 200))
    window.blit(FOUR, (100, 0))
    window.blit(EIGHT, (200, 0))
    window.blit(SIXTEEN, (300, 0))
    window.blit(THIRTYTWO, (400, 0))
    window.blit(SIXTYFOUR, (500, 0))
    window.blit(ONEHUNDREDTWENTYEIGHT, (600, 0))
    window.blit(TWOHUNDREDFIFTYSIX, (700, 0))
    window.blit(FIVEHUNDREDTWELVE, (800, 0))
    window.blit(ONETHOUSANDTWENTYFOUR, (900, 0))
    window.blit(TWOTHOUSANDFOURTYEIGHT, (0, 100))
    
    # Outline
    pygame.draw.rect(window, OUTLINE_COLOR, OUTLINE, width=8)

    # Vertical
    pygame.draw.line(window, OUTLINE_COLOR, (350, 200), (350, 800), width=8)
    pygame.draw.line(window, OUTLINE_COLOR, (500, 200), (500, 800), width=8)
    pygame.draw.line(window, OUTLINE_COLOR, (650, 200), (650, 800), width=8)

    # Horizontal
    pygame.draw.line(window, OUTLINE_COLOR, (200, 350), (800, 350), width=8)
    pygame.draw.line(window, OUTLINE_COLOR, (200, 500), (800, 500), width=8)
    pygame.draw.line(window, OUTLINE_COLOR, (200, 650), (800, 650), width=8)

    pygame.display.update()


def tile_generation():
    tile_gotten = False
    if 0 in layers[0] or 0 in layers[1] or 0 in layers[2] or 0 in layers[3]:
        while not tile_gotten:
            layer_position = random.randint(0, 3)
            tile_position = random.randint(0, 3)
            if layers[layer_position][tile_position] == 0:
                generate_number = random.randint(1, 4)
                if generate_number <= 3:
                    layers[layer_position][tile_position] = 2
                else:
                    layers[layer_position][tile_position] = 4
                tile_gotten = True
    else:
        print("The board is full")
        # Do something
def UP():
    for i in range(1, 0, -1):
        for j in range(0, 4):
            if layers[i-1][j] == 0:
                layers[i-1][j] = layers[i][j]
                layers[i][j] = 0
    for i in range(2, 0, -1):
        for j in range(0, 4):
            if layers[i-1][j] == 0:
                layers[i-1][j] = layers[i][j]
                layers[i][j] = 0
    for i in range(3, 0, -1):
        for j in range(0, 4):
            if layers[i-1][j] == 0:
                layers[i-1][j] = layers[i][j]
                layers[i][j] = 0
    tile_generation()
    print()
    for layer in layers:
        print(layer)

def LEFT():
    for i in range(1, 0, -1):
        for j in range(0, 4):
            if layers[j][i-1] == 0:
                layers[j][i-1] = layers[j][i]
                layers[j][i] = 0
    for i in range(2, 0, -1):
        for j in range(0, 4):
            if layers[j][i-1] == 0:
                layers[j][i-1] = layers[j][i]
                layers[j][i] = 0
    for i in range(3, 0, -1):
        for j in range(0, 4):
            if layers[j][i-1] == 0:
                layers[j][i-1] = layers[j][i]
                layers[j][i] = 0
    tile_generation()
    print()
    for layer in layers:
        print(layer)

def RIGHT():
    for i in range(0, 4):
        if layers[i][3] == 0:
            layers[i][3] = layers[i][2]
            layers[i][2] = 0
    for j in range(1, 3):
        for i in range(0, 4):
            if layers[i][j+1] == 0:
                layers[i][j+1] = layers[i][j]
                layers[i][j+1] = 0
    for j in range(0, 3):
        for i in range(0, 4):
            if layers[i][j+1] == 0:
                layers[i][j+1] = layers[i][j]
                layers[i][j+1] = 0
    tile_generation()
    print()
    for layer in layers:
        print(layer)
def main():
    running = True

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    UP()
                if event.key == pygame.K_a:
                    LEFT()
                if event.key == pygame.K_s:
                    DOWN()
                if event.key == pygame.K_d:
                    RIGHT()

        DRAW_WINDOW()


if  __name__ == '__main__':
    main()
    