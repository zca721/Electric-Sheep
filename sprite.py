import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        # self.rect.center = (x, y)
        self.rect.x = x
        self.rect.y = y

    def destroy(self):
        print("destroy")
        self.kill()
