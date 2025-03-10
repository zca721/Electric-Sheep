import pygame, sys, time
from settings import *
from level import Level
from textManager import TextManager
from buttonManager import Button
from chat import AIChat

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Electric Sheep')

        # Full screen mode
        # self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        # self.level = Level()
        self.textManager = TextManager()
        self.aiChat = AIChat()

        # Questions for google gemini response for nonscripted NPC
        self.questionOne = "What is your relationship with Burgermeister?"
        self.questionTwo = "What happened when you found Burgermeister missing?"
        self.questionThree = "When was the last time you saw Burgermeister?"
        self.questionFour = "Did you know that Burgermeister’s real daughter is still alive?"

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
        self.questionOneString = 1
        self.questionTwoString = 2
        self.questionThreeString = 4
        self.buildString = 0
        self.secretString = 7

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

                if self.buildString == self.secretString:
                    self.questionFourButton.handle_event(event)
                    if self.questionFourButton.handle_event(event):
                        # self.textManager.updateCounter()
                        self.question = 4
                        self.displayText = True
                        self.buildString = 0

                # Depending on what question is clicked a answer will be given
                if self.questionOneButton.handle_event(event):
                    self.question = 1
                    self.displayText = True
                    self.buildString = self.buildString | self.questionOneString

                elif self.questionTwoButton.handle_event(event):
                    self.question = 2
                    self.displayText = True
                    self.buildString = self.buildString | self.questionTwoString

                elif self.questionThreeButton.handle_event(event):
                    self.question = 3
                    self.displayText = True
                    self.buildString = self.buildString | self.questionThreeString

            delta_time = self.clock.tick() / 1000
            # self.level.run(delta_time)

            # Display questions as buttons
            self.questionOneButton.draw(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT, self.screen)
            self.questionTwoButton.draw(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT, self.screen)
            self.questionThreeButton.draw(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT, self.screen)

            if self.buildString == self.secretString:
                self.questionFourButton.draw(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT, self.screen)
            else:
                self.hideQuestionFour.draw(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT, self.screen)
                
            # Depending on even above a answer will be returned
            if self.displayText == True:
                # Scripted NPC response
                # self.textManager.scriptedResponse(self.screen, self.question)
                # self.displayText = False

                # Nonscripte NPC response
                if self.question == 1:
                    self.aiChat.nonscriptedResponse(self.screen, self.questionOne)
                    self.displayText = False
                elif self.question == 2:
                    self.aiChat.nonscriptedResponse(self.screen, self.questionTwo)
                    self.displayText = False
                elif self.question == 3:
                    self.aiChat.nonscriptedResponse(self.screen, self.questionThree)
                    self.displayText = False
                elif self.question == 4:
                    self.aiChat.nonscriptedResponse(self.screen, self.questionFour)
                    self.displayText = False
                
            pygame.display.flip()
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()