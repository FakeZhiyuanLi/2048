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
TWO = pygame.image.load(os.path.join('2048', 'Assets', '2.png'))
FOUR = pygame.image.load(os.path.join('2048', 'Assets', '4.png'))
EIGHT = pygame.image.load(os.path.join('2048', 'Assets', '8.png'))
SIXTEEN = pygame.image.load(os.path.join('2048', 'Assets', '16.png'))
THIRTYTWO = pygame.image.load(os.path.join('2048', 'Assets', '32.png'))
SIXTYFOUR = pygame.image.load(os.path.join('2048', 'Assets', '64.png'))
ONEHUNDREDTWENTYEIGHT = pygame.image.load(os.path.join('2048', 'Assets', '128.png'))
TWOHUNDREDFIFTYSIX = pygame.image.load(os.path.join('2048', 'Assets', '256.png'))
FIVEHUNDREDTWELVE = pygame.image.load(os.path.join('2048', 'Assets', '512.png'))
ONETHOUSANDTWENTYFOUR = pygame.image.load(os.path.join('2048', 'Assets', '1024.png'))
TWOTHOUSANDFOURTYEIGHT = pygame.image.load(os.path.join('2048', 'Assets', '2048.png'))


# Outline variables
# OUTLINE = pygame.Rect(WIDTH / 2, HEIGHT / 2, 400, 400)

WHITE = (255, 255, 255)
# OUTLINE_COLOR = (107, 107, 107)

def DRAW_WINDOW():
    window.fill(WHITE)
    window.blit(TWO, (0, 0))
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
    
    # pygame.draw.rect(window, OUTLINE_COLOR, OUTLINE)
    
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
def UP():
    tile_generation()
    print(layers)


def main():
    running = True

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.QUIT()
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