import pygame
from settings import *

class TextManager:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 16)

        self.answerOneMessage = "I am Burgermeister's daughter and care taker. I maintain all of his communications and schedule his appointments."
        self.answerTwoMessage = "The morning of I could not find Burgermeister any where in the Tower and this was very strange becasue he never leaves the Tower, so I call the authorities."
        self.answerThreeMessage = "I last saw Burgermeister the night before. I gave him his night time tea before bed and read him a story till he fell asleep."
        self.answerFourMessage = "I actually overheard Burgermeiseter talking with his real daughter the night before and had plans to meet her outside of the tower."
        self.snip = self.font.render('', True, 'white')
        self.counter = 0
        self.counterOne = 0
        self.counterTwo = 0
        self.counterThree = 0
        self.counterFour = 0
        self.speed = 3
        self.done = False
        self.run = True

    def scriptedResponse(self, screen, question):
        keys = pygame.key.get_pressed()
        pygame.draw.rect(screen, 'black', [ANSWER_X, ANSWER_Y, ANSWER_WIDTH, ANSWER_HEIGHT])
        
        if question == 1:
            self.displayText(screen, self.answerOneMessage)

        elif question == 2:
            self.displayText(screen, self.answerTwoMessage)

        elif question == 3:
            self.displayText(screen, self.answerThreeMessage)
        
        elif question == 4:
            self.displayText(screen, self.answerFourMessage)

    def displayText(self, screen, message):
        pygame.draw.rect(screen, 'black', [ANSWER_X, ANSWER_Y, ANSWER_WIDTH, ANSWER_HEIGHT])

        # Display text one character at a time
        # if self.counter < self.speed * len(message):
        #     self.counter += 1
        # elif self.counter >= self.speed * len(message):
        #     self.done = True
        # self.snip = self.font.render(message[0:self.counter//self.speed], True, 'white')

        # Display text all at once
        self.snip = self.font.render(message, True, 'white')
        screen.blit(self.snip, (ANSWER_X+10, ANSWER_Y+10))
            
