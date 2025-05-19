import pygame
from settings import *

class Button:
    def __init__(self, x, y, width, height, text, color, highlighted_color, action=None):
        pygame.init()
        self.font = pygame.font.Font('freesansbold.ttf', SMALL_FONT)
        self.mediumFont = pygame.font.Font('freesansbold.ttf', LARGE_FONT)
        # self.delay_time = 4000  # milliseconds
        # self.last_click_time = 0
        pygame.mixer.init()
        # self.buttonClick = pygame.mixer.Sound("./sounds/buttonClickOne.mp3")
        # self.buttonClick = pygame.mixer.Sound("./sounds/buttonClickTwo.mp3")
        self.buttonClick = pygame.mixer.Sound("./sounds/buttonClickThree.mp3")
        # self.buttonClick = pygame.mixer.Sound("./sounds/buttonClickFour.mp3")

        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.highlighted_color = highlighted_color
        self.action = action
        self.snip = self.font.render('', True, 'white')

    def draw(self, screen):

        mouse_pos = pygame.mouse.get_pos()
        if self.is_hovered(mouse_pos):
            text_surface = self.font.render(self.text, True, self.highlighted_color)
        else:
            text_surface = self.font.render(self.text, True, self.color)

        text_rect = pygame.draw.rect(screen, 'black', [self.x, self.y, self.width, self.height])
        screen.blit(text_surface, text_rect)

    def drawMediumButton(self, screen):

        mouse_pos = pygame.mouse.get_pos()
        if self.is_hovered(mouse_pos):
            text_surface = self.mediumFont.render(self.text, True, self.highlighted_color)
        else:
            text_surface = self.mediumFont.render(self.text, True, self.color)

        text_rect = pygame.draw.rect(screen, 'black', [self.x, self.y, self.width, self.height])
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.buttonClick.play()
                return True
                    
    # def delay_handle_event(self, event):
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         if self.rect.collidepoint(event.pos):
    #             current_time = pygame.time.get_ticks()
    #             if current_time - self.last_click_time >= self.delay_time:
    #                 print("Button Clicked!")
    #                 print("current_time", current_time)
    #                 print("last_click_time", self.last_click_time)
    #                 print("delay_time", self.delay_time)
    #                 self.last_click_time = current_time
    #                 return True
    #             else:
    #                 print("Button is on cooldown.")
    #                 print("current_time", current_time)
    #                 print("last_click_time", self.last_click_time)
    #                 print("delay_time", self.delay_time)

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)