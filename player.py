import pygame

class Player:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = 5
        self.velocity = pygame.Vector2(0, 0)

    def handle_input(self, keys):
        self.velocity.x = 0
        self.velocity.y = 0
        if keys[pygame.K_w]:
            self.velocity.y = -self.speed
        if keys[pygame.K_s]:
            self.velocity.y = self.speed
        if keys[pygame.K_a]:
            self.velocity.x = -self.speed
        if keys[pygame.K_d]:
            self.velocity.x = self.speed

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
