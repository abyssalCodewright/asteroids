import pygame # type: ignore
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for member in updatable_group:
            member.update(dt)
        screen.fill('black')
        for member in drawable_group:
            member.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()