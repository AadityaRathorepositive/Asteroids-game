import pygame
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteriodfield import AsteroidField
import sys
from circleshape import CircleShape
from shoot import Shot

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
    shots=pygame.sprite.Group()
    Shot.containers=(shots,updatable,drawable)

    while True:

        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        #player.draw(screen)
        #player.update(dt)
        updatable.update(dt)
        for object in asteroids:
            for each_shoot in shots:
                if object.collides_with(each_shoot):
                    log_event("asteroid_shot")
                    object.split()
                    each_shoot.kill()
            if object.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt=delta_time.tick(60)/1000
        #print(dt)
        

        
    



if __name__ == "__main__":
    main()
