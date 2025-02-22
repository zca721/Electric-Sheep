import pygame
from settings import *

class SceneManager:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        # self.messages = ["How can I be of assistance?",
        #                  "Is there some questions you would like to ask me?",
        #                  "If so go ahead and start asking."]
        self.answerOneMessage = "I am Burgermeister's daughter and care taker. I maintain all of his communications and schedule his appointments."
        self.answerTwoMessage = "I entered Burgermeister's room in the morning to wake him and noticed right away that he was not in his room, which was weird. Then I checked the building for him and he was no where to be found, then I contacted the authorities."
        self.snip = self.font.render('', True, 'white')
        self.counter = 0
        self.speed = 30
        self.active_message = 0
        # self.message = self.messages[self.active_message]
        self.done = False
        self.run = True

    def displayAnswerText(self, screen, question):
        keys = pygame.key.get_pressed()
        pygame.draw.rect(screen, 'black', [ANSWER_X, ANSWER_Y, ANSWER_WIDTH, ANSWER_HEIGHT])
        
        if question == 1:
            if self.counter < self.speed * len(self.answerOneMessage):
                self.counter += 1

            elif self.counter >= self.speed * len(self.answerOneMessage):
                self.done = True
        elif question == 2:
            if self.counter < self.speed * len(self.answerTwoMessage):
                self.counter += 1

            elif self.counter >= self.speed * len(self.answerTwoMessage):
                self.done = True

        # for event in self.message:
        #     if self.done and self.active_message < len(self.messages) and keys[pygame.K_RETURN]:
        #         self.active_message += 1
        #         self.done = False
        #         self.message = self.messages[self.active_message]
        #         self.counter = 0

        # print("Counter: ", self.counter)
        # // division to the floor
        if question == 1:
            self.snip = self.font.render(self.answerOneMessage[0:self.counter//self.speed], True, 'white')
        elif question == 2:
            self.snip = self.font.render(self.answerTwoMessage[0:self.counter//self.speed], True, 'white')

        screen.blit(self.snip, (ANSWER_X+10, ANSWER_Y+10))

    def update(self):
        self.displayAnswerText()
        
