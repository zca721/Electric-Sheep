import pygame
from settings import *

class TextManager:
    def __init__(self):
        # Font style and size
        self.font = pygame.font.Font('freesansbold.ttf', SMALL_FONT)
        self.mediumFont = pygame.font.Font('freesansbold.ttf', MEDIUM_FONT)
        self.titleFont = pygame.font.Font('freesansbold.ttf', ELECTRIC_SHEEP_FONT)

        # Silvia 2.0 scripted response
        self.answerOneMessageSilviaAI = "I am made in the image of Burgermeisters deceased daughter and I maintain all of his communications and life tasks."
        self.answerTwoMessageSilviaAI = "The morning of I could not find Burgermeister any where in the Tower and this was very strange becasue he never leaves the Tower, so I called the authorities."
        self.answerThreeMessageSilviaAI = "I last saw Burgermeister the night before. He was just finishing his work for the day in his War Room."
        self.answerFourMessageSilviaAI = "I read in Burgermeister's communications that he planned to meet with his daughter in secret outside of the Fortress, but did not specify why."

        # Silvia Jade scripted response
        self.answerOneMessageSilviaJade = "That monster is no father of mine! DONT EVER REFER TO HIM AS MY FATHER AGAIN!"
        self.answerTwoMessageSilviaJade = "I needed to free myself of his grasp, I may have been his daughter, but I was more like a prisoner. I despise all that he stands for!"
        self.answerThreeMessageSilviaJade = "Why would I EVER do that?! I broke free from that WICKED man all those years ago and NEVER looked back!"
        self.answerFourMessageSilviaJade = "Hell no! Why would you think I would ever contemplate that?! I'd rather go blind then ever see that villian again!"

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
                self.displayText(screen, self.answerOneMessageSilviaAI)
            elif question == 2:
                self.displayText(screen, self.answerTwoMessageSilviaAI)
            elif question == 3:
                self.displayText(screen, self.answerThreeMessageSilviaAI)
            elif question == 4:
                self.displayText(screen, self.answerFourMessageSilviaAI)
        elif npc == "Silvia Jade":
            if question == 1:
                self.displayText(screen, self.answerOneMessageSilviaJade)
            elif question == 2:
                self.displayText(screen, self.answerTwoMessageSilviaJade)
            elif question == 3:
                self.displayText(screen, self.answerThreeMessageSilviaJade)
            elif question == 4:
                self.displayText(screen, self.answerFourMessageSilviaJade)

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
        screen.blit(self.snip, (ANSWER_X + DISPLAY_FONT, ANSWER_Y + DISPLAY_FONT))
            
    def mediumDisplayText(self, screen, message, x, y, width, height):
        pygame.draw.rect(screen, 'black', [x, y, width, height])

        # Display text all at once
        self.snip = self.font.render(message, True, 'red')
        screen.blit(self.snip, (x + DISPLAY_FONT, y + DISPLAY_FONT))

    def titleDisplayText(self, screen, message, x, y, width, height):
        pygame.draw.rect(screen, 'black', [x, y, width, height])

        # Display text all at once
        self.snip = self.titleFont.render(message, True, 'red')
        screen.blit(self.snip, (x + DISPLAY_FONT, y + DISPLAY_FONT))