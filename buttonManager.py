import pygame
from settings import *
from textManager import TextManager

class Button:
    def __init__(self, x, y, width, height, text, color, highlighted_color, action=None):
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.highlighted_color = highlighted_color
        self.action = action
        self.snip = self.font.render('', True, 'white')

    def draw(self, button_x, button_y, button_width, button_height, screen):
        text_surface = self.font.render(self.text, True, 'white')
        text_rect = pygame.draw.rect(screen, 'black', [button_x, button_y, button_width, button_height])
        screen.blit(text_surface, text_rect)
        

    def highlight(self, button_x, button_y, button_width, button_height, screen):
        text_surface = self.font.render(self.text, True, 'grey')
        text_rect = pygame.draw.rect(screen, 'black', [button_x, button_y, button_width, button_height,])
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
                    

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)