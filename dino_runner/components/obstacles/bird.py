import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self, image):
        self.position =[280,300, 330]
        self.type = random.randint(0, 1)
        self.type_position = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = self.position[self.type_position]

        