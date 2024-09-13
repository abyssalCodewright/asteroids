from circleshape import CircleShape
import pygame # type: ignore

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, 'orange', self.position, self.radius, width=2)


    def update(self, dt):
        self.position += (self.velocity * dt)