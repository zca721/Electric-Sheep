import pygame, sys
from settings import *
from level import Level
from sceneManager import SceneManager
from button import Button

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Electric Sheep')

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        # self.level = Level()
        self.sceneManager = SceneManager()

        self.questionOneButton = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        "What is your relationship with Burgermeister?",
                                        'white', 'gray', action=None)
        self.questionTwoButton = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        "What happened when you found Burgermeister missing?",
                                        'white', 'gray', action=None)
        
        self.displayText = False
        self.question = 0



    # button = Button(100, 100, 200, 50, "Click Me", (200, 200, 200), (255, 255, 255), action=button_action)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                self.questionOneButton.handle_event(event)
                self.questionTwoButton.handle_event(event)
                if self.questionOneButton.handle_event(event):
                    self.question = 1
                    self.displayText = True
                elif self.questionTwoButton.handle_event(event):
                    self.question = 2
                    self.displayText = True

                # else:
                #     self.displayText = False

            delta_time = self.clock.tick() / 1000
            # self.level.run(delta_time)
            self.questionOneButton.draw(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT, self.screen)
            self.questionTwoButton.draw(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT, self.screen)
            mouse_pos = pygame.mouse.get_pos()

            if self.questionOneButton.is_hovered(mouse_pos):
                # print("Hovering")
                self.questionOneButton.highlight(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT, self.screen)
            else:
                # print("Not Hovering")
                self.questionOneButton.draw(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT, self.screen)

            if self.questionTwoButton.is_hovered(mouse_pos):
                # print("Hovering")
                self.questionTwoButton.highlight(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT, self.screen)
            else:
                # print("Not Hovering")
                self.questionTwoButton.draw(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT, self.screen)
                
            if self.displayText == True:
                self.sceneManager.displayAnswerText(self.screen, self.question)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()