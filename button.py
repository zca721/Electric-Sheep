import pygame
from settings import *

class Button:
    def __init__(self, x, y, width, height, text, color, highlighted_color, action=None):
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.highlighted_color = highlighted_color
        self.action = action
        self.snip = self.font.render('', True, 'white')
        self.questionOne = "What is your relationship with Burgermeister?"

    def draw(self, button_x, button_y, button_width, button_height, screen):

        # # Get mouse position
        # position = pygame.mouse.get_pos()

        # if self.rect.collidepoint(position):
        #     if pygame
        #         print("CLICKED")
        # pygame.draw.rect(screen, 'white', [BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT])
        # self.snip = self.font.render(self.questionOne, True, 'black')
        # screen.blit(self.snip, (BUTTON_X+10, BUTTON_Y+10))
        # pygame.draw.rect(screen, self.color, self.rect)

        
        text_surface = self.font.render(self.text, True, 'white')
        # text_rect = text_surface.get_rect(center=self.rect.center)
        text_rect = pygame.draw.rect(screen, 'black', [button_x, button_y, button_width, button_height])
        screen.blit(text_surface, text_rect)
        

    def highlight(self, button_x, button_y, button_width, button_height, screen):
        
        text_surface = self.font.render(self.text, True, 'grey')
        # text_rect = text_surface.get_rect(center=self.rect.center)
        text_rect = pygame.draw.rect(screen, 'black', [button_x, button_y, button_width, button_height,])
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print("Clicked")
            if self.rect.collidepoint(event.pos):
                print("Clicked")
                return True
            #     if self.action:
            #         self.action()
                    

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)