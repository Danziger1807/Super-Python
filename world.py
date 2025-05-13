import pygame

class World:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = 5
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
