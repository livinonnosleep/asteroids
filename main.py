import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import *
from asteroid import Asteroid 
from asteroidfield import AsteroidField
from shot import Shot


def main():
    dt = 0
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        log_state()
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
            for asteroid in asteroids:
                if player.collides_with(asteroid):
                    log_event("player_hit")
                    print ("Game over!")
                    sys.exit()
            for asteroid in asteroids:
                for shot in shots:
                    if shot.collides_with(asteroid):
                        log_event("asteroid_shot")
                        asteroid.split()
                        shot.kill()



        pygame.display.flip()
        

if __name__ == "__main__":

    main()
