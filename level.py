import pygame
from settings import *
from player import Player
from nonplayer import Nonplayer

class Level:
    def __init__(self):
        # Get the display surface
        self.display_surface = pygame.display.get_surface()

        # Sprite group
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        # Call setup method
        self.setup()

    def setup(self):
        # Displays in center of screen
        self.player = Player((640, 360), self.all_sprites, self.collision_sprites)

        self.nonplayer = Nonplayer((1200, 80), self.all_sprites, self.collision_sprites)

    def run(self, delta_time):
        self.display_surface.fill('white')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(delta_time)