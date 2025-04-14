import pygame
from settings import *
from answers import *

class TextManager:
    def __init__(self):
        pygame.init()
        # Font style and size
        self.font = pygame.font.Font('freesansbold.ttf', SMALL_FONT)
        self.mediumFont = pygame.font.Font('freesansbold.ttf', MEDIUM_FONT)
        self.titleFont = pygame.font.Font('freesansbold.ttf', ELECTRIC_SHEEP_FONT)

        self.snip = self.font.render('', True, 'white')
        # self.counter = 0
        # self.counterOne = 0
        # self.counterTwo = 0
        # self.counterThree = 0
        # self.counterFour = 0
        # self.speed = 3
        # self.done = False
        # self.run = True

    def scriptedResponse(self, screen, question, npc):
        # keys = pygame.key.get_pressed()
        pygame.draw.rect(screen, 'black', [ANSWER_X, ANSWER_Y, ANSWER_WIDTH, ANSWER_HEIGHT])
        
        if npc == "Silvia 2.0":
            if question == 1:
                self.displayAnswer(screen, answerOneSilviaAI)
            elif question == 2:
                self.displayAnswer(screen, answerTwoSilviaAI)
            elif question == 3:
                self.displayAnswer(screen, answerThreeSilviaAI)
            elif question == 4:
                self.displayAnswer(screen, answerFourSilviaAI)
            elif question == 5:
                self.displayAnswer(screen, answerFiveSilviaAI)
            elif question == 6:
                self.displayAnswer(screen, answerSixSilviaAI)
            elif question == 7:
                self.displayAnswer(screen, answerSevenSilviaAI)
            elif question == 8:
                self.displayAnswer(screen, answerEightSilviaAI)
            elif question == 9:
                self.displayAnswer(screen, answerNineSilviaAI)
            elif question == 10:
                self.displayAnswer(screen, answerTenSilviaAI)
            elif question == 11:
                self.displayAnswer(screen, answerElevenSilviaAI)
            elif question == 12:
                self.displayAnswer(screen, answerTwelveSilviaAI)
            elif question == 13:
                self.displayAnswer(screen, answerThirteenSilviaAI)
            elif question == 14:
                self.displayAnswer(screen, answerFourteenSilviaAI)
            elif question == 15:
                self.displayAnswer(screen, answerFifteenSilviaAI)
            elif question == 16:
                self.displayAnswer(screen, answerSixteenSilviaAI)

        elif npc == "Silvia Jade":
            if question == 1:
                self.displayAnswer(screen, answerOneSilviaHuman)
            elif question == 2:
                self.displayAnswer(screen, answerTwoSilviaHuman)
            elif question == 3:
                self.displayAnswer(screen, answerThreeSilviaHuman)
            elif question == 4:
                self.displayAnswer(screen, answerFourSilviaHuman)
            elif question == 5:
                self.displayAnswer(screen, answerFiveSilviaHuman)
            elif question == 6:
                self.displayAnswer(screen, answerSixSilviaHuman)
            elif question == 7:
                self.displayAnswer(screen, answerSevenSilviaHuman)
            elif question == 8:
                self.displayAnswer(screen, answerEightSilviaHuman)
            elif question == 9:
                self.displayAnswer(screen, answerNineSilviaHuman)
            elif question == 10:
                self.displayAnswer(screen, answerTenSilviaHuman)
            elif question == 11:
                self.displayAnswer(screen, answerElevenSilviaHuman)
            elif question == 12:
                self.displayAnswer(screen, answerTwelveSilviaHuman)
            elif question == 13:
                self.displayAnswer(screen, answerThirteenSilviaHuman)
            elif question == 14:
                self.displayAnswer(screen, answerFourteenSilviaHuman)
            elif question == 15:
                self.displayAnswer(screen, answerFifteenSilviaHuman)
            elif question == 16:
                self.displayAnswer(screen, answerSixteenSilviaHuman)

    def displayAnswer(self, screen, message):
        pygame.draw.rect(screen, 'black', [ANSWER_X, ANSWER_Y, ANSWER_WIDTH, ANSWER_HEIGHT])

        # Display text one character at a time
        # if self.counter < self.speed * len(message):
        #     self.counter += 1
        # elif self.counter >= self.speed * len(message):
        #     self.done = True
        # self.snip = self.font.render(message[0:self.counter//self.speed], True, 'white')

        # Display text all at once
        self.snip = self.font.render(message, True, 'white')
        screen.blit(self.snip, (ANSWER_X + DISPLAY_FONT, ANSWER_Y + DISPLAY_FONT))
            
    def displayRedText(self, screen, message, x, y, width, height, size):
        pygame.draw.rect(screen, 'black', [x, y, width, height])

        # Display text all at once
        if size == "small":
            self.snip = self.font.render(message, True, 'red')
        elif size == "medium":
            self.snip = self.mediumFont.render(message, True, 'red')
        elif size == "title":
            self.snip = self.titleFont.render(message, True, 'red')

        screen.blit(self.snip, (x + DISPLAY_FONT, y + DISPLAY_FONT))
