import pygame
from settings import *
from answers import *

class TextManager:
    def __init__(self):
        pygame.init()
        # Font style and size
        self.smallFont = pygame.font.Font('freesansbold.ttf', SMALL_FONT)
        self.mediumFont = pygame.font.Font('freesansbold.ttf', MEDIUM_FONT)
        self.largeFont = pygame.font.Font('freesansbold.ttf', LARGE_FONT)
        self.extraLargeFont = pygame.font.Font('freesansbold.ttf', EXTRA_LARGE_FONT)

        self.snip = self.smallFont.render('', True, 'white')
        # self.counter = 0
        # self.counterOne = 0
        # self.counterTwo = 0
        # self.counterThree = 0
        # self.counterFour = 0
        # self.speed = 3
        # self.done = False
        # self.run = True

    def scriptedResponse(self, screen, question, npc, guilty):
        # keys = pygame.key.get_pressed()
        pygame.draw.rect(screen, 'black', [ANSWER_X, ANSWER_Y, ANSWER_WIDTH, ANSWER_HEIGHT])
        
        if guilty == "Silvia 2.0":
            if npc == "Silvia 2.0":
                if question == 1:
                    self.displayAnswer(screen, answerOneSilviaAIGuilty)
                elif question == 2:
                    self.displayAnswer(screen, answerTwoSilviaAIGuilty)
                elif question == 3:
                    self.displayAnswer(screen, answerThreeSilviaAIGuilty)
                elif question == 4:
                    self.displayAnswer(screen, answerFourSilviaAIGuilty)
                elif question == 5:
                    self.displayAnswer(screen, answerFiveSilviaAIGuilty)
                elif question == 6:
                    self.displayAnswer(screen, answerSixSilviaAIGuilty)
                elif question == 7:
                    self.displayAnswer(screen, answerSevenSilviaAIGuilty)
                elif question == 8:
                    self.displayAnswer(screen, answerEightSilviaAIGuilty)
                elif question == 9:
                    self.displayAnswer(screen, answerNineSilviaAIGuilty)
                elif question == 10:
                    self.displayAnswer(screen, answerTenSilviaAIGuilty)
                elif question == 11:
                    self.displayAnswer(screen, answerElevenSilviaAIGuilty)
                elif question == 12:
                    self.displayAnswer(screen, answerTwelveSilviaAIGuilty)
                elif question == 13:
                    self.displayAnswer(screen, answerThirteenSilviaAIGuilty)
                elif question == 14:
                    self.displayAnswer(screen, answerFourteenSilviaAIGuilty)
                elif question == 15:
                    self.displayAnswer(screen, answerFifteenSilviaAIGuilty)
                elif question == 16:
                    self.displayAnswer(screen, answerSixteenSilviaAIGuilty)
                elif question == 17:
                    self.displayAnswer(screen, answerSeventeenSilviaAIGuilty)
                elif question == 18:
                    self.displayAnswer(screen, answerEighteenSilviaAIGuilty)
                elif question == 19:
                    self.displayAnswer(screen, answerNineteenSilviaAIGuilty)
                elif question == 20:
                    self.displayAnswer(screen, answerTwentySilviaAIGuilty)
                elif question == 21:
                    self.displayAnswer(screen, answerTwentyOneSilviaAIGuilty)
                elif question == 22:
                    self.displayAnswer(screen, answerTwentyTwoSilviaAIGuilty)
                elif question == 23:
                    self.displayAnswer(screen, answerTwentyThreeSilviaAIGuilty)
                elif question == 24:
                    self.displayAnswer(screen, answerTwentyFourSilviaAIGuilty)
                elif question == 25:
                    self.displayAnswer(screen, answerTwentyFiveSilviaAIGuilty)
                elif question == 26:
                    self.displayAnswer(screen, answerTwentySixSilviaAIGuilty)
                elif question == 27:
                    self.displayAnswer(screen, answerTwentySevenSilviaAIGuilty)
                elif question == 28:
                    self.displayAnswer(screen, answerTwentyEightSilviaAIGuilty)
                elif question == 29:
                    self.displayAnswer(screen, answerTwentyNineSilviaAIGuilty)
                elif question == 30:
                    self.displayAnswer(screen, answerThirtySilviaAIGuilty)
                elif question == 31:
                    self.displayAnswer(screen, answerThirtyOneSilviaAIGuilty)
                elif question == 32:
                    self.displayAnswer(screen, answerThirtyTwoSilviaAIGuilty)
                elif question == 33:
                    self.displayAnswer(screen, answerThirtyThreeSilviaAIGuilty)
                elif question == 34:
                    self.displayAnswer(screen, answerThirtyFourSilviaAIGuilty)
                elif question == 35:
                    self.displayAnswer(screen, answerThirtyFiveSilviaAIGuilty)
                elif question == 36:
                    self.displayAnswer(screen, answerThirtySixSilviaAIGuilty)
                elif question == 37:
                    self.displayAnswer(screen, answerThirtySevenSilviaAIGuilty)
                elif question == 38:
                    self.displayAnswer(screen, answerThirtyEightSilviaAIGuilty)
                elif question == 39:
                    self.displayAnswer(screen, answerThirtyNineSilviaAIGuilty)
                elif question == 40:
                    self.displayAnswer(screen, answerFourtySilviaAIGuilty)

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
                elif question == 17:
                    self.displayAnswer(screen, answerSeventeenSilviaHuman)
                elif question == 18:
                    self.displayAnswer(screen, answerEighteenSilviaHuman)
                elif question == 19:
                    self.displayAnswer(screen, answerNineteenSilviaHuman)
                elif question == 20:
                    self.displayAnswer(screen, answerTwentySilviaHuman)
                elif question == 21:
                    self.displayAnswer(screen, answerTwentyOneSilviaHuman)
                elif question == 22:
                    self.displayAnswer(screen, answerTwentyTwoSilviaHuman)
                elif question == 23:
                    self.displayAnswer(screen, answerTwentyThreeSilviaHuman)
                elif question == 24:
                    self.displayAnswer(screen, answerTwentyFourSilviaHuman)
                elif question == 25:
                    self.displayAnswer(screen, answerTwentyFiveSilviaHuman)
                elif question == 26:
                    self.displayAnswer(screen, answerTwentySixSilviaHuman)
                elif question == 27:
                    self.displayAnswer(screen, answerTwentySevenSilviaHuman)
                elif question == 28:
                    self.displayAnswer(screen, answerTwentyEightSilviaHuman)
                elif question == 29:
                    self.displayAnswer(screen, answerTwentyNineSilviaHuman)
                elif question == 30:
                    self.displayAnswer(screen, answerThirtySilviaHuman)
                elif question == 31:
                    self.displayAnswer(screen, answerThirtyOneSilviaHuman)
                elif question == 32:
                    self.displayAnswer(screen, answerThirtyTwoSilviaHuman)
                elif question == 33:
                    self.displayAnswer(screen, answerThirtyThreeSilviaHuman)
                elif question == 34:
                    self.displayAnswer(screen, answerThirtyFourSilviaHuman)
                elif question == 35:
                    self.displayAnswer(screen, answerThirtyFiveSilviaHuman)
                elif question == 36:
                    self.displayAnswer(screen, answerThirtySixSilviaHuman)
                elif question == 37:
                    self.displayAnswer(screen, answerThirtySevenSilviaHuman)
                elif question == 38:
                    self.displayAnswer(screen, answerThirtyEightSilviaHuman)
                elif question == 39:
                    self.displayAnswer(screen, answerThirtyNineSilviaHuman)
                elif question == 40:
                    self.displayAnswer(screen, answerFourtySilviaHuman)


        elif guilty == "Silvia Jade":
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
                elif question == 17:
                    self.displayAnswer(screen, answerSeventeenSilviaAI)
                elif question == 18:
                    self.displayAnswer(screen, answerEighteenSilviaAI)
                elif question == 19:
                    self.displayAnswer(screen, answerNineteenSilviaAI)
                elif question == 20:
                    self.displayAnswer(screen, answerTwentySilviaAI)
                elif question == 21:
                    self.displayAnswer(screen, answerTwentyOneSilviaAI)
                elif question == 22:
                    self.displayAnswer(screen, answerTwentyTwoSilviaAI)
                elif question == 23:
                    self.displayAnswer(screen, answerTwentyThreeSilviaAI)
                elif question == 24:
                    self.displayAnswer(screen, answerTwentyFourSilviaAI)
                elif question == 25:
                    self.displayAnswer(screen, answerTwentyFiveSilviaAI)
                elif question == 26:
                    self.displayAnswer(screen, answerTwentySixSilviaAI)
                elif question == 27:
                    self.displayAnswer(screen, answerTwentySevenSilviaAI)
                elif question == 28:
                    self.displayAnswer(screen, answerTwentyEightSilviaAI)
                elif question == 29:
                    self.displayAnswer(screen, answerTwentyNineSilviaAI)
                elif question == 30:
                    self.displayAnswer(screen, answerThirtySilviaAI)
                elif question == 31:
                    self.displayAnswer(screen, answerThirtyOneSilviaAI)
                elif question == 32:
                    self.displayAnswer(screen, answerThirtyTwoSilviaAI)
                elif question == 33:
                    self.displayAnswer(screen, answerThirtyThreeSilviaAI)
                elif question == 34:
                    self.displayAnswer(screen, answerThirtyFourSilviaAI)
                elif question == 35:
                    self.displayAnswer(screen, answerThirtyFiveSilviaAI)
                elif question == 36:
                    self.displayAnswer(screen, answerThirtySixSilviaAI)
                elif question == 37:
                    self.displayAnswer(screen, answerThirtySevenSilviaAI)
                elif question == 38:
                    self.displayAnswer(screen, answerThirtyEightSilviaAI)
                elif question == 39:
                    self.displayAnswer(screen, answerThirtyNineSilviaAI)
                elif question == 40:
                    self.displayAnswer(screen, answerFourtySilviaAI)

            elif npc == "Silvia Jade":
                if question == 1:
                    self.displayAnswer(screen, answerOneSilviaHumanGuilty)
                elif question == 2:
                    self.displayAnswer(screen, answerTwoSilviaHumanGuilty)
                elif question == 3:
                    self.displayAnswer(screen, answerThreeSilviaHumanGuilty)
                elif question == 4:
                    self.displayAnswer(screen, answerFourSilviaHumanGuilty)
                elif question == 5:
                    self.displayAnswer(screen, answerFiveSilviaHumanGuilty)
                elif question == 6:
                    self.displayAnswer(screen, answerSixSilviaHumanGuilty)
                elif question == 7:
                    self.displayAnswer(screen, answerSevenSilviaHumanGuilty)
                elif question == 8:
                    self.displayAnswer(screen, answerEightSilviaHumanGuilty)
                elif question == 9:
                    self.displayAnswer(screen, answerNineSilviaHumanGuilty)
                elif question == 10:
                    self.displayAnswer(screen, answerTenSilviaHumanGuilty)
                elif question == 11:
                    self.displayAnswer(screen, answerElevenSilviaHumanGuilty)
                elif question == 12:
                    self.displayAnswer(screen, answerTwelveSilviaHumanGuilty)
                elif question == 13:
                    self.displayAnswer(screen, answerThirteenSilviaHumanGuilty)
                elif question == 14:
                    self.displayAnswer(screen, answerFourteenSilviaHumanGuilty)
                elif question == 15:
                    self.displayAnswer(screen, answerFifteenSilviaHumanGuilty)
                elif question == 16:
                    self.displayAnswer(screen, answerSixteenSilviaHumanGuilty)
                elif question == 17:
                    self.displayAnswer(screen, answerSeventeenSilviaHumanGuilty)
                elif question == 18:
                    self.displayAnswer(screen, answerEighteenSilviaHumanGuilty)
                elif question == 19:
                    self.displayAnswer(screen, answerNineteenSilviaHumanGuilty)
                elif question == 20:
                    self.displayAnswer(screen, answerTwentySilviaHumanGuilty)
                elif question == 21:
                    self.displayAnswer(screen, answerTwentyOneSilviaHumanGuilty)
                elif question == 22:
                    self.displayAnswer(screen, answerTwentyTwoSilviaHumanGuilty)
                elif question == 23:
                    self.displayAnswer(screen, answerTwentyThreeSilviaHumanGuilty)
                elif question == 24:
                    self.displayAnswer(screen, answerTwentyFourSilviaHumanGuilty)
                elif question == 25:
                    self.displayAnswer(screen, answerTwentyFiveSilviaHumanGuilty)
                elif question == 26:
                    self.displayAnswer(screen, answerTwentySixSilviaHumanGuilty)
                elif question == 27:
                    self.displayAnswer(screen, answerTwentySevenSilviaHumanGuilty)
                elif question == 28:
                    self.displayAnswer(screen, answerTwentyEightSilviaHumanGuilty)
                elif question == 29:
                    self.displayAnswer(screen, answerTwentyNineSilviaHumanGuilty)
                elif question == 30:
                    self.displayAnswer(screen, answerThirtySilviaHumanGuilty)
                elif question == 31:
                    self.displayAnswer(screen, answerThirtyOneSilviaHumanGuilty)
                elif question == 32:
                    self.displayAnswer(screen, answerThirtyTwoSilviaHumanGuilty)
                elif question == 33:
                    self.displayAnswer(screen, answerThirtyThreeSilviaHumanGuilty)
                elif question == 34:
                    self.displayAnswer(screen, answerThirtyFourSilviaHumanGuilty)
                elif question == 35:
                    self.displayAnswer(screen, answerThirtyFiveSilviaHumanGuilty)
                elif question == 36:
                    self.displayAnswer(screen, answerThirtySixSilviaHumanGuilty)
                elif question == 37:
                    self.displayAnswer(screen, answerThirtySevenSilviaHumanGuilty)
                elif question == 38:
                    self.displayAnswer(screen, answerThirtyEightSilviaHumanGuilty)
                elif question == 39:
                    self.displayAnswer(screen, answerThirtyNineSilviaHumanGuilty)
                elif question == 40:
                    self.displayAnswer(screen, answerFourtySilviaHumanGuilty)

    def displayAnswer(self, screen, message):
        pygame.draw.rect(screen, 'black', [ANSWER_X, ANSWER_Y, ANSWER_WIDTH, ANSWER_HEIGHT])

        # Display text one character at a time
        # if self.counter < self.speed * len(message):
        #     self.counter += 1
        # elif self.counter >= self.speed * len(message):
        #     self.done = True
        # self.snip = self.font.render(message[0:self.counter//self.speed], True, 'white')

        # Display text all at once
        self.snip = self.smallFont.render(message, True, 'white')
        screen.blit(self.snip, (ANSWER_X + DISPLAY_FONT, ANSWER_Y + DISPLAY_FONT))
            
    def displayRedText(self, screen, message, x, y, width, height, size):
        pygame.draw.rect(screen, 'black', [x, y, width, height])

        # Display text all at once
        if size == "small":
            self.snip = self.smallFont.render(message, True, 'red')
        elif size == "medium":
            self.snip = self.mediumFont.render(message, True, 'red')
        elif size == "large":
            self.snip = self.largeFont.render(message, True, 'red')
        elif size == "extra large":
            self.snip = self.extraLargeFont.render(message, True, 'red')

        screen.blit(self.snip, (x + DISPLAY_FONT, y + DISPLAY_FONT))
