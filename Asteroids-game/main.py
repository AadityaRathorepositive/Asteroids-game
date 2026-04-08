import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    dt=0
    x= SCREEN_WIDTH/2
    y= SCREEN_HEIGHT/2
    player=Player(x,y)
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        delta_time=pygame.time.Clock()
        find_delta_time=delta_time.tick(60)
        dt=find_delta_time/1000
        #print(dt)

        
    



if __name__ == "__main__":
    main()
