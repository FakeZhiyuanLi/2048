import pygame
import os
pygame.init()

# Variables
clock = pygame.time.Clock()
window = pygame.display.set_mode([1000, 1000])
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

WHITE = (255, 255, 255)

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
    
    
    pygame.display.update()

def main():
    running = True

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        DRAW_WINDOW()


if  __name__ == '__main__':
    main()