from circleshape import CircleShape
from constants import *
import random
import pygame # type: ignore

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, 'orange', self.position, self.radius, width=2)


    def update(self, dt):
        self.position += (self.velocity * dt)

    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        positive_random = self.velocity.rotate(random_angle)
        negative_random = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_new = Asteroids(self.position.x, self.position.y, new_radius)
        second_new = Asteroids(self.position.x, self.position.y, new_radius)

        first_new.velocity = positive_random * 1.2
        second_new.velocity = negative_random * 1.2