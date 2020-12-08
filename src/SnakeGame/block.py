import pygame

class block(object):
    rows = 8
    w = 500

    def __init__(self, position, directionX=1, directionY=0, color=(255, 255, 255)):
        self.pos = position
        self.directionX = 1
        self.directionY = 0
        self.color = color

    def move(self, directionX, directionY):
        self.directionX = directionX
        self.directionY = directionY
        self.pos = (self.pos[0] + self.directionX, self.pos[1] + self.directionY)

    def draw(self, surface):
        size = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        left = i * size + 1
        top = j * size + 1
        width = size - 3
        height = size - 3

        pygame.draw.rect(surface, self.color, (left, top, width, height))
