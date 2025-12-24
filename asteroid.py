import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
       pygame.draw.circle(screen, "red", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_degree = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(random_degree)
            velocity2 = self.velocity.rotate(-random_degree)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            print("SPLIT:", "old radius =", self.radius, "new radius =", new_radius)
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = velocity1 * 1.2
            asteroid2.velocity = velocity2 * 1.2




            
       
