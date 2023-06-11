import pygame
import math
import numpy

from object_3d import *
from camera import *
from projection import *


class SoftwareRender:
    def __init__(self):
        pygame.init()
        self.RES = self.WIDTH, self.HEIGHT = 800, 800
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 30
        self.screen = pygame.display.set_mode(self.RES)
        self.clock = pygame.time.Clock()
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self, [0.5,1,-4])
        self.projection = Projection(self)
        self.object = Object3D(self)
        self.object.translate([0.2, 0.4, 0.2])
        self.object.rotate_y(math.pi / 6)

    def draw(self):
        self.screen.fill(pygame.Color('black'))
        self.object.draw()

    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
            pygame.display.set_caption(str(self.clock.get_fps()))
            pygame.display.flip()
            self.clock.tick(self.FPS)


app = SoftwareRender()
app.run()