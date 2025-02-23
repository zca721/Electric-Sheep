import pygame
from settings import *

class TextManager:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.numberFont = pygame.font.Font('freesansbold.ttf', 40)
        # self.messages = ["How can I be of assistance?",
        #                  "Is there some questions you would like to ask me?",
        #                  "If so go ahead and start asking."]
        self.answerOneMessage = "I am Burgermeister's daughter and care taker. I maintain all of his communications and schedule his appointments."
        self.answerTwoMessage = "I entered Burgermeister's room in the morning to wake him and noticed he was not in his room."
        self.answerThreeMessage = "I last saw Burgermeister the night before. I gave him his night time tea before bed and read him a story till he fell asleep."
        self.answerFourMessage = "I actually overheard Burgermeiseter talking with his real daughter the night before and had plans to meet her outside of the tower."
        self.snip = self.font.render('', True, 'white')
        self.counterOne = 0
        self.counterTwo = 0
        self.counterThree = 0
        self.counterFour = 0
        self.speed = 3
        self.active_message = 0
        # self.message = self.messages[self.active_message]
        self.done = False
        self.run = True

    def displayAnswerText(self, screen, question):
        keys = pygame.key.get_pressed()
        pygame.draw.rect(screen, 'black', [ANSWER_X, ANSWER_Y, ANSWER_WIDTH, ANSWER_HEIGHT])
        
        if question == 1:
            self.counterTwo = 0
            self.counterThree = 0
            self.counterFour = 0
            if self.counterOne < self.speed * len(self.answerOneMessage):
                self.counterOne += 1
            elif self.counterOne >= self.speed * len(self.answerOneMessage):
                self.done = True

        elif question == 2:
            self.counterOne = 0
            self.counterThree = 0
            self.counterFour = 0
            if self.counterTwo < self.speed * len(self.answerTwoMessage):
                self.counterTwo += 1
            elif self.counterTwo >= self.speed * len(self.answerTwoMessage):
                self.done = True

        elif question == 3:
            self.counterOne = 0
            self.counterTwo = 0
            self.counterFour = 0
            if self.counterThree < self.speed * len(self.answerThreeMessage):
                self.counterThree += 1
            elif self.counterThree >= self.speed * len(self.answerThreeMessage):
                self.done = True
        
        elif question == 4:
            self.counterOne = 0
            self.counterTwo = 0
            self.counterThree = 0
            if self.counterFour < self.speed * len(self.answerFourMessage):
                self.counterFour += 1
            elif self.counterFour >= self.speed * len(self.answerFourMessage):
                self.done = True

        # // division to the floor
        if question == 1:
            self.snip = self.font.render(self.answerOneMessage[0:self.counterOne//self.speed], True, 'white')
        elif question == 2:
            self.snip = self.font.render(self.answerTwoMessage[0:self.counterTwo//self.speed], True, 'white')
        elif question == 3:
            self.snip = self.font.render(self.answerThreeMessage[0:self.counterThree//self.speed], True, 'white')
        elif question == 4:
            self.snip = self.font.render(self.answerFourMessage[0:self.counterFour//self.speed], True, 'red')

        screen.blit(self.snip, (ANSWER_X+10, ANSWER_Y+10))
        
    def questionSequence(self, screen, sequence):
        print(sequence)
        string_sequence = str(sequence)

        pygame.draw.rect(screen, 'black', [SEQUENCE_X, SEQUENCE_Y, SEQUENCE_WIDTH, SCREEN_HEIGHT])
        self.snip = self.numberFont.render(string_sequence, True, 'white')
        screen.blit(self.snip, (SEQUENCE_X+10, SEQUENCE_Y+10))

    def updateCounter(self):
        # self.displayAnswerText()
        self.counterOne = 0
        self.counterTwo = 0
        self.counterThree = 0
        self.counterFour = 0
        
