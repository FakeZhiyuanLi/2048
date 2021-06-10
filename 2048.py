import pygame
import random
import os

pygame.init()

# Main Variables
WIDTH = 1000
HEIGHT = 1000
tile_gotten = False

layers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
layer1 = []
layer2 = []
layer3 = []
layer4 = []

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

TWO_LIST = []
FOUR_LIST = []
EIGHT_LIST = []
SIXTEEN_LIST = []
THIRTYTWO_LIST = []
SIXTYFOUR_LIST = []
ONEHUNDREDTWENTYEIGHT_LIST = []
TWOHUNDREDFIFTYSIX_LIST = []
FIVEHUNDREDTWELVE_LIST = []
ONETHOUSANDTWENTYFOUR_LIST = []
TWOTHOUSANDFOURTYEIGHT_LIST = []

# Outline variables
OUTLINE = pygame.Rect(WIDTH / 2 - 300, HEIGHT / 2 - 300, 600, 600)

WHITE = (255, 255, 255)
OUTLINE_COLOR = (107, 107, 107)

def DRAW_WINDOW():
    window.fill(WHITE)

    for two in TWO_LIST:
        window.blit(TWO, (two.x, two.y))
    for four in FOUR_LIST:
        window.blit(FOUR, (four.x, four.y))
    for eight in EIGHT_LIST:
        window.blit(EIGHT, (eight.x, eight.y))
    for sixteen in SIXTEEN_LIST:
        window.blit(SIXTEEN, (sixteen.x, sixteen.y))
    for thirtytwo in THIRTYTWO_LIST:
        window.blit(THIRTYTWO, (thirtytwo.x, thirtytwo.y))
    for sixtyfour in SIXTYFOUR_LIST:
        window.blit(SIXTYFOUR, (sixtyfour.x, sixtyfour.y))
    for onehundredtwentyeight in ONEHUNDREDTWENTYEIGHT_LIST:
        window.blit(ONEHUNDREDTWENTYEIGHT, (onehundredtwentyeight.x, onehundredtwentyeight.y))
    for twohundredfiftysix in TWOHUNDREDFIFTYSIX_LIST:
        window.blit(TWOHUNDREDFIFTYSIX, (twohundredfiftysix.x, twohundredfiftysix.y))

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

def merge_up(i, j):
    layers[i-1][j] *= 2
    layers[i][j] = 0
def merge_left(i, j):
    layers[j][i-1] *= 2
    layers[j][i] = 0
def merge_right(i, j):
    layers[i][j+1] *= 2
    layers[i][j] = 0
def merge_down(i, j):
    layers[j+1][i] *= 2
    layers[j][i] = 0
def UP():
    for i in range(1, 0, -1):
        for j in range(0, 4):
            if layers[i-1][j] == layers[i][j]:
                merge_up(i, j)
            else:
                if layers[i-1][j] == 0:
                    layers[i-1][j] = layers[i][j]
                    layers[i][j] = 0
    for i in range(2, 0, -1):
        for j in range(0, 4):
            if layers[i-1][j] == layers[i][j]:
                merge_up(i, j)
            else:
                if layers[i-1][j] == 0:
                    layers[i-1][j] = layers[i][j]
                    layers[i][j] = 0
    for i in range(3, 0, -1):
        for j in range(0, 4):
            if layers[i-1][j] == layers[i][j]:
                merge_up(i, j)
            else:
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
            if layers[j][i-1] == layers[j][i]:
                merge_left(i, j)
            else:
                if layers[j][i-1] == 0:
                    layers[j][i-1] = layers[j][i]
                    layers[j][i] = 0
    for i in range(2, 0, -1):
        for j in range(0, 4):
            if layers[j][i-1] == layers[j][i]:
                merge_left(i, j)
            else:
                if layers[j][i-1] == 0:
                    layers[j][i-1] = layers[j][i]
                    layers[j][i] = 0
    for i in range(3, 0, -1):
        for j in range(0, 4):
            if layers[j][i-1] == layers[j][i]:
                merge_left(i, j)
            else:
                if layers[j][i-1] == 0:
                    layers[j][i-1] = layers[j][i]
                    layers[j][i] = 0
    tile_generation()
    print()
    for layer in layers:
        print(layer)

def RIGHT():
    for i in range(0, 4):
        if layers[i][3] == layers[i][2]:
            layers[i][3] *= 2
            layers[i][2] = 0
        else:
            if layers[i][3] == 0:
                layers[i][3] = layers[i][2]
                layers[i][2] = 0
    for j in range(1, 3):
        for i in range(0, 4):
            if layers[i][j+1] == layers[i][j]:
                merge_right(i, j)
            else:
                if layers[i][j+1] == 0:
                    layers[i][j+1] = layers[i][j]
                    layers[i][j] = 0
    for j in range(0, 3):
        for i in range(0, 4):
            if layers[i][j+1] == layers[i][j]:
                merge_right(i, j)
            else:
                if layers[i][j+1] == 0:
                    layers[i][j+1] = layers[i][j]
                    layers[i][j] = 0
    tile_generation()
    print()
    for layer in layers:
        print(layer)

def DOWN():
    for i in range(0, 4):
        if layers[3][i] == layers[2][i]:
            layers[3][i] *= 2
            layers[2][i] = 0
        else:
            if layers[3][i] == 0:
                layers[3][i] = layers[2][i]
                layers[2][i] = 0
    for j in range(1, 3):
        for i in range(0, 4):
            if layers[j+1][i] == layers[j][i]:
                merge_down(i, j)
            else:
                if layers[j+1][i] == 0:
                    layers[j+1][i] = layers[j][i]
                    layers[j][i] = 0
    for j in range(0, 3):
        for i in range(0, 4):
            if layers[j+1][i] == layers[j][i]:
                merge_down(i, j)
            else:
                if layers[j+1][i] == 0:
                    layers[j+1][i] = layers[j][i]
                    layers[j][i] = 0
    tile_generation()
    print()
    for layer in layers:
        print(layer)

def HANDLE_TILES():

    # I is the x axix, and J is the y axis
    x, y = 200, 200
    for i in range(0, 4):
        for j in range(0, 4):
            if layers[i][j] == 2:
                TWO_LIST.append(pygame.Rect(x, y, 150, 150))
            if layers[i][j] == 4:
                FOUR_LIST.append(pygame.Rect(x, y, 150, 150))
            # This line goes last
            x += 150
        y += 150    
        x = 200

def main():
    running = True

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    UP()
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    LEFT()
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    DOWN()
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    RIGHT()

        HANDLE_TILES()
        DRAW_WINDOW()

    pygame.quit()

if  __name__ == '__main__':
    main()
    