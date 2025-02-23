import pygame, sys
from settings import *
from level import Level
from textManager import TextManager
from buttonManager import Button

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Electric Sheep')

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        # self.level = Level()
        self.sceneManager = TextManager()

        # Buttons for interrogation questions
        self.questionOneButton = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        "What is your relationship with Burgermeister?",
                                        'white', 'gray', action=None)
        self.questionTwoButton = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        "What happened when you found Burgermeister missing?",
                                        'white', 'gray', action=None)
        self.questionThreeButton = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        "When was the last time you saw Burgermeister?",
                                        'white', 'gray', action=None)
        self.questionFourButton = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        "Did you know that Burgermeister’s real daughter is still alive?",
                                        'white', 'gray', action=None)
        self.hideQuestionFour = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        "",
                                        'white', 'gray', action=None)
        
        self.displayText = False
        self.question = 0
        self.sequence = 0
        self.questionOneString = '100'
        self.questionTwoString = '010'
        self.questionThreeString = '001'
        self.buildString = ''
        self.secretString = '100010001'

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Checks for even when button clicked
                self.questionOneButton.handle_event(event)
                self.questionTwoButton.handle_event(event)
                self.questionThreeButton.handle_event(event)

                if self.buildString == self.secretString and self.sequence == 3:
                    self.questionFourButton.handle_event(event)
                    if self.questionFourButton.handle_event(event):
                        self.sceneManager.updateCounter()
                        self.question = 4
                        self.displayText = True
                        self.buildString = ""

                # Depending on what question is clicked a answer will be given
                if self.questionOneButton.handle_event(event):
                    self.sceneManager.updateCounter()
                    self.question = 1
                    self.displayText = True
                    self.sequence += 1
                    self.buildString = self.buildString + self.questionOneString

                elif self.questionTwoButton.handle_event(event):
                    self.sceneManager.updateCounter()
                    self.question = 2
                    self.displayText = True
                    self.sequence += 1
                    self.buildString = self.buildString + self.questionTwoString

                elif self.questionThreeButton.handle_event(event):
                    self.sceneManager.updateCounter()
                    self.question = 3
                    self.displayText = True
                    self.sequence += 1
                    self.buildString = self.buildString + self.questionThreeString

            delta_time = self.clock.tick() / 1000
            # self.level.run(delta_time)

            # Display questions as buttons
            self.questionOneButton.draw(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT, self.screen)
            self.questionTwoButton.draw(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT, self.screen)
            self.questionThreeButton.draw(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT, self.screen)


            print(self.buildString)
            if self.buildString == self.secretString and self.sequence == 3:
                self.questionFourButton.draw(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT, self.screen)
                if self.questionFourButton.is_hovered(mouse_pos):
                    self.questionFourButton.highlight(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT, self.screen)
                else:
                    self.questionFourButton.draw(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT, self.screen)
                
            elif self.buildString != self.secretString and self.sequence == 3:
                # self.hideQuestionFour.draw(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT, self.screen)
                self.sequence = 0
                self.buildString = ''
            else:
                self.hideQuestionFour.draw(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT, self.screen)


            # Tracks mouse movement and keeps it updated
            mouse_pos = pygame.mouse.get_pos()

            # Checks if hovering over question one
            if self.questionOneButton.is_hovered(mouse_pos):
                self.questionOneButton.highlight(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT, self.screen)
            else:
                self.questionOneButton.draw(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT, self.screen)

            # Checks if hovering over question two
            if self.questionTwoButton.is_hovered(mouse_pos):
                self.questionTwoButton.highlight(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT, self.screen)
            else:
                self.questionTwoButton.draw(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT, self.screen)

            # Checks if hovering over question three
            if self.questionThreeButton.is_hovered(mouse_pos):
                self.questionThreeButton.highlight(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT, self.screen)
            else:
                self.questionThreeButton.draw(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT, self.screen)
                
            # Depending on even above a answer will be returned
            if self.displayText == True:
                self.sceneManager.displayAnswerText(self.screen, self.question)
                
            pygame.display.flip()
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()