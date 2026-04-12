from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self,screen):
        color="white"
        
        pygame.draw.circle(screen,color,self.position,self.radius,LINE_WIDTH)
    def update(self,dt):
        self.position += self.velocity*dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angel=random.uniform(20,50)
            
            new_radius=self.radius-ASTEROID_MIN_RADIUS
            new_asteriod1=Asteroid(self.position.x,self.position.y,new_radius)
            new_asteriod2=Asteroid(self.position.x,self.position.y,new_radius)
            vector1=self.velocity.rotate(random_angel)
            vector2=self.velocity.rotate(-random_angel)
            new_asteriod1.velocity=vector1*1.2
            new_asteriod2.velocity=vector2*1.2

