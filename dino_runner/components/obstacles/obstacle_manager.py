import random
import pygame
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.cactus_type = [SMALL_CACTUS, LARGE_CACTUS]
        
    def update(self, game):
        self.type = random.randint(0, 1)        
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(self.cactus_type[self.type]))
            
            if len(self.obstacles) > 0 and len(self.obstacles) < 2:
                self.obstacles.append(Bird(BIRD))


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                game.playing = False
                break
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    
        

    
        
