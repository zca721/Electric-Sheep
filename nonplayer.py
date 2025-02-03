import pygame
from settings import *
from support import *

class Nonplayer(pygame.sprite.Sprite):
    def __init__(self, position, group, collision_sprites):
        super().__init__(group)

        self.import_assets()
        self.status = 'rachael'
        self.frame_index = 0

        # self.image = pygame.Surface((64,64))
        # self.image.fill('red')
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = position)

        # Collision
        self.collision_sprites = collision_sprites
        self.hitbox = self.rect.copy()  #.inflate((x,y)) will allow for shrinking and growing the hit box

    def import_assets(self):
        self.animations = {'deckard': [], 'rachael': []}

        for animation in self.animations.keys():
            # May need to change the path when uploading to github as a playable link
            full_path = '/Users/zacharyanderson/Unity-workspace/Blabe Walker/images/' + animation
            self.animations[animation] = import_folder(full_path)
