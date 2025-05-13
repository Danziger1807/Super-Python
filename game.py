import pygame
from player import Player
from world import World
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(100, 100, 50, 50, (255, 0, 0))  # x, y, width, height, color
        self.ground = World(0, 550, 800, 50,(0, 255, 0)) # x, y, width, height, color

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)
        self.player.update()

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.ground.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)  # 60 FPS
