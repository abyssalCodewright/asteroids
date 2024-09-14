import pygame # type: ignore
from constants import *
from player import Player
from asteroids import *
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroids.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (shot_group, drawable_group, updatable_group)

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for member in updatable_group:
            member.update(dt)
        screen.fill('black')
        for member in drawable_group:
            member.draw(screen)
        for member in asteroids_group:
            if member.collision(player):
                print("Game over!")
                return
            for shot in shot_group:
                if member.collision(shot):
                    member.split()
                    shot.kill()
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()