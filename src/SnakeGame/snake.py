import pygame

from block import block
from hamilton import hamilton
from human import human
from longest_path import longest_path
from shortest_path import shortest_path


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = block(pos)
        self.body.append(self.head)
        self.directionX = 0
        self.directionY = 1
        self.human = human()
        self.shortest = shortest_path()
        self.longest = longest_path()
        self.hamilton = hamilton()

    def move(self, gameMode):
        if gameMode == "human":
            self.human.move(self)
        elif gameMode == "breadth-first-search":
            self.shortest.move(self)
        elif gameMode == "depth-first-search":
            self.longest.move(self)
        elif gameMode == "hamilton":
            self.longest.move(self)
        else:
            pass

    def reset(self, pos):
        self.head = block(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.directionX = 0
        self.directionY = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.directionX, tail.directionY

        if dx == 1 and dy == 0:
            self.body.append(block((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(block((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(block((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(block((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].directionX = dx
        self.body[-1].directionY = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            c.draw(surface)