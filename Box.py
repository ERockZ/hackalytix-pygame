import pygame as pgame
class Box:
    def __init__(self, x, y, color=(255, 0, 0)):
        self.width = 10
        self.height = 10
        self.x = x
        self.y = y
        self.color = color

    def draw(self, window):
        pgame.draw.rect(window, self.color,
                        (self.x, self.y, self.width, self.height))
