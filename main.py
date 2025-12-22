import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while 1:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("red")
        pygame.display.flip()

    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
