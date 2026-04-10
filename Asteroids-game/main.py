import pygame
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteriodfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    delta_time=pygame.time.Clock()

    pygame.time.Clock()
    dt=0
    x= SCREEN_WIDTH/2
    y= SCREEN_HEIGHT/2
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    Player.containers=(updatable,drawable)
    player=Player(x,y)
    asteroids=pygame.sprite.Group()
    Asteroid.containers=(asteroids,updatable,drawable)
    AsteroidField.containers=(updatable,)
    AsteroidField1=AsteroidField()

    while True:

        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        #player.draw(screen)
        #player.update(dt)
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt=delta_time.tick(60)/1000
        #print(dt)
        

        
    



if __name__ == "__main__":
    main()
