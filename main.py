import pygame, sys, time
from settings import *
from questions import *
from buttons import *
from level import Level
from textManager import TextManager
from buttonManager import Button
from chat import AIChat
from sprite import Sprite

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Electric Sheep')

        # Scene
        self.scene = "main_menu"

        # Full screen mode
        # self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        # Sprite images
        self.silviaAISprite = pygame.image.load("./images/silviaAI/SilviaAI.png").convert_alpha()
        self.silviaHumanSprite = pygame.image.load("./images/silviaJade/SilviaJade.png").convert_alpha()
        self.interrogationBackgroundSprite = pygame.image.load("./images/objects/InterrogationBackground.png").convert_alpha()
        self.spriteSilviaAI = Sprite(self.silviaAISprite, AI_SILVIA_X, AI_SILVIA_Y)
        self.spriteSilviaHuman = Sprite(self.silviaHumanSprite, HUMAN_SILVIA_X, HUMAN_SILVIA_Y)
        self.interrogationBackground = Sprite(self.interrogationBackgroundSprite, INTERROGATION_BACKGROUND_X, INTERROGATION_BACKGROUND_Y)

        # self.level = Level()
        self.textManager = TextManager()
        self.aiChat = AIChat()
        self.sprites = pygame.sprite.Group()

        # Text based variables
        self.displayAnswer = False
        self.stage = 0
        self.slotOne = 1
        self.slotTwo = 2
        self.slotThree = 3
        self.slotFour = 4
        self.question = 0
        self.questionOneString = 1
        self.questionTwoString = 2
        self.questionThreeString = 4
        self.buildString = 0
        self.secretString = 7
        self.blankMessage = ""

        # Display text in main menu
        self.electricSheepTitle = "ELECTRIC SHEEP"

        # Display text in iterrogation
        self.selectSuspect = "SELECT SUSPECT"
        self.selectQuestion = "SELECT INTERROGATION QUESTION"
        self.stageDisplay = "STAGE "

        # NPC based variables
        self.npc = " "
        self.npcSelect = " "

    # Helper functions
    # Builds secret string for each stage
    def stages(self, questionSlot, npc):
        if questionSlot == 1:
            self.buildString = self.buildString | self.questionOneString
        elif questionSlot == 2:
            self.buildString = self.buildString | self.questionTwoString
        elif questionSlot == 3:
            self.buildString = self.buildString | self.questionThreeString
        elif questionSlot == 4:
            self.buildString = 0
            if npc == "Silvia 2.0":
                self.npcSelect = "Silvia Jade" # Allows for NPC to be selected after secret question is asked
            elif npc == "Silvia Jade":
                self.npcSelect = "Silvia 2.0" # Allows for NPC to be selected after secret question is asked
        
        self.displayAnswer = True

    def run(self):

        text = open("SystemInstructionOutput.txt", "a")
        text.write("----------------------------------------------------------------------------------------------------------------------------------------" + "\n")
        text.write("NEW GAME SESSION: " + "\n")
        text.close()

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Scenemanager for event
                if self.scene == "main_menu":
                    self.screen.fill('black')
                    if startGame.handle_event(event):
                        self.scene = "interrogation"

                elif self.scene == "interrogation":
                    # Displays interrogation sprite images
                    self.sprites.add(self.interrogationBackground)
                    self.sprites.draw(self.screen)

                    # Depending on what NPC is clicked display associated questions
                    if aiSilvia.handle_event(event):
                        self.npc = "Silvia 2.0"
                        self.displayAnswer = False
                        self.question = 0
                        self.buildString = 0
                        self.textManager.displayAnswer(self.screen, self.blankMessage) # Hides answer

                        # Displays sprite image
                        self.spriteSilviaHuman.destroy()
                        self.screen.fill('black')
                        self.sprites.add(self.interrogationBackground)
                        self.sprites.add(self.spriteSilviaAI)
                        self.sprites.draw(self.screen)
                        # print(self.spriteSilviaAI)
                        # print(self.spriteSilviaHuman)

                    elif humanSilvia.handle_event(event):
                        self.npc = "Silvia Jade"
                        self.displayAnswer = False
                        self.question = 0
                        self.buildString = 0
                        self.textManager.displayAnswer(self.screen, self.blankMessage) # Hides answer

                        # Displays sprite image
                        self.spriteSilviaAI.destroy()
                        self.screen.fill('black')
                        self.sprites.add(self.interrogationBackground)
                        self.sprites.add(self.spriteSilviaHuman)
                        self.sprites.draw(self.screen)
                        # print(self.spriteSilviaAI)
                        # print(self.spriteSilviaHuman)

                    # Handles events for Silvia 2.0
                    if self.npc == "Silvia 2.0":
                        # Stage 0
                        if self.stage == 0:
                            # Depending on what question is clicked a answer will be given with Silvia 2.0
                            if questionOneButtonSilviaAI.handle_event(event):
                                self.question = 1
                                self.stages(self.slotOne, self.npc)

                            elif questionTwoButtonSilviaAI.handle_event(event):
                                self.question = 2
                                self.stages(self.slotTwo, self.npc)

                            elif questionThreeButtonSilviaAI.handle_event(event):
                                self.question = 3
                                self.stages(self.slotThree, self.npc)

                            if self.buildString == self.secretString:
                                if questionFourButtonSilviaAI.handle_event(event):
                                    self.question = 4
                                    self.stages(self.slotFour, self.npc)
                                    self.stage = 1
                        # Stage 2
                        elif self.stage == 2:
                            # Depending on what question is clicked a answer will be given with Silvia 2.0
                            if questionFiveButtonSilviaAI.handle_event(event):
                                self.question = 5
                                self.stages(self.slotOne, self.npc)

                            elif questionSixButtonSilviaAI.handle_event(event):
                                self.question = 6
                                self.stages(self.slotTwo, self.npc)

                            elif questionSevenButtonSilviaAI.handle_event(event):
                                self.question = 7
                                self.stages(self.slotThree, self.npc)

                            if self.buildString == self.secretString:
                                if questionEightButtonSilviaAI.handle_event(event):
                                    self.question = 8
                                    self.stages(self.slotFour, self.npc)
                                    self.stage = 3
                        # Stage 4
                        elif self.stage == 4:
                            # Depending on what question is clicked a answer will be given with Silvia 2.0
                            if questionNineButtonSilviaAI.handle_event(event):
                                self.question = 9
                                self.stages(self.slotOne, self.npc)

                            elif questionTenButtonSilviaAI.handle_event(event):
                                self.question = 10
                                self.stages(self.slotTwo, self.npc)

                            elif questionElevenButtonSilviaAI.handle_event(event):
                                self.question = 11
                                self.stages(self.slotThree, self.npc)

                            if self.buildString == self.secretString:
                                if questionTwelveButtonSilviaAI.handle_event(event):
                                    self.question = 12
                                    self.stages(self.slotFour, self.npc)
                                    self.stage = 5
                        # Stage 6
                        elif self.stage == 6:
                            # Depending on what question is clicked a answer will be given with Silvia 2.0
                            if questionThirteenButtonSilviaAI.handle_event(event):
                                self.question = 13
                                self.stages(self.slotOne, self.npc)

                            elif questionFourteenButtonSilviaAI.handle_event(event):
                                self.question = 14
                                self.stages(self.slotTwo, self.npc)

                            elif questionFifteenButtonSilviaAI.handle_event(event):
                                self.question = 15
                                self.stages(self.slotThree, self.npc)

                            if self.buildString == self.secretString:
                                if questionSixteenButtonSilviaAI.handle_event(event):
                                    self.question = 16
                                    self.stages(self.slotFour, self.npc)
                                    self.stage = 7

                    # Handles events for Silvia Jade
                    if self.npc == "Silvia Jade":
                        # Stage 1
                        if self.stage == 1:
                            # Depending on what question is clicked a answer will be given
                            if questionOneButtonSilviaHuman.handle_event(event):
                                self.question = 1
                                self.stages(self.slotOne, self.npc)

                            elif questionTwoButtonSilviaHuman.handle_event(event):
                                self.question = 2
                                self.stages(self.slotTwo, self.npc)

                            elif questionThreeButtonSilviaHuman.handle_event(event):
                                self.question = 3
                                self.stages(self.slotThree, self.npc)

                            if self.buildString == self.secretString:
                                if questionFourButtonSilviaHuman.handle_event(event):
                                    self.question = 4
                                    self.stages(self.slotFour, self.npc)
                                    self.stage = 2
                        # Stage 3
                        elif self.stage == 3:
                            # Depending on what question is clicked a answer will be given
                            if questionFiveButtonSilviaHuman.handle_event(event):
                                self.question = 5
                                self.stages(self.slotOne, self.npc)

                            elif questionSixButtonSilviaHuman.handle_event(event):
                                self.question = 6
                                self.stages(self.slotTwo, self.npc)

                            elif questionSevenButtonSilviaHuman.handle_event(event):
                                self.question = 7
                                self.stages(self.slotThree, self.npc)

                            if self.buildString == self.secretString:
                                if questionEightButtonSilviaHuman.handle_event(event):
                                    self.question = 8
                                    self.stages(self.slotFour, self.npc)
                                    self.stage = 4
                        # Stage 5
                        elif self.stage == 5:
                            # Depending on what question is clicked a answer will be given
                            if questionNineButtonSilviaHuman.handle_event(event):
                                self.question = 9
                                self.stages(self.slotOne, self.npc)

                            elif questionTenButtonSilviaHuman.handle_event(event):
                                self.question = 10
                                self.stages(self.slotTwo, self.npc)

                            elif questionElevenButtonSilviaHuman.handle_event(event):
                                self.question = 11
                                self.stages(self.slotThree, self.npc)

                            if self.buildString == self.secretString:
                                if questionTwelveButtonSilviaHuman.handle_event(event):
                                    self.question = 12
                                    self.stages(self.slotFour, self.npc)
                                    self.stage = 6
                        # Stage 7
                        elif self.stage == 7:
                            # Depending on what question is clicked a answer will be given
                            if questionThirteenButtonSilviaHuman.handle_event(event):
                                self.question = 13
                                self.stages(self.slotOne, self.npc)

                            elif questionFourteenButtonSilviaHuman.handle_event(event):
                                self.question = 14
                                self.stages(self.slotTwo, self.npc)

                            elif questionFifteenButtonSilviaHuman.handle_event(event):
                                self.question = 15
                                self.stages(self.slotThree, self.npc)

                            if self.buildString == self.secretString:
                                if questionSixteenButtonSilviaHuman.handle_event(event):
                                    self.question = 16
                                    self.stages(self.slotFour, self.npc)
                                    self.stage = 8

            # Used for timing of game
            # delta_time = self.clock.tick() / 1000
            # self.level.run(delta_time)

            # Scenemanager for while loop
            if self.scene == "main_menu":
                startGame.drawMainMenu(self.screen)
                self.textManager.displayRedText(self.screen, self.electricSheepTitle,
                                                  ELECTRIC_SHEEP_X, ELECTRIC_SHEEP_Y, ELECTRIC_SHEEP_WIDTH, ELECTRIC_SHEEP_HEIGHT,
                                                  "title")

            elif self.scene == "interrogation":
                # Keeps sprite images in sprites group being continuously displayed if in group
                self.sprites.update()

                # Display NPC names to select from based off npc name string
                if self.npcSelect == " " or self.npcSelect == "Silvia 2.0":
                    aiSilvia.draw(self.screen)
                elif self.npcSelect == "Silvia Jade":
                    humanSilvia.draw(self.screen)

                # Display interrogation big font
                self.textManager.displayRedText(self.screen, self.selectSuspect,
                                                   SUSPECT_X, SUSPECT_Y, SUSPECT_WIDTH, SUSPECT_HEIGHT,
                                                   "small")
                self.textManager.displayRedText(self.screen, self.selectQuestion,
                                                   QUESTION_X, QUESTION_Y, QUESTION_WIDTH, QUESTION_HEIGHT,
                                                   "small")
                self.textManager.displayRedText(self.screen, self.stageDisplay + str(self.stage),
                                                    STAGE_X, STAGE_Y, STAGE_WIDTH, STAGE_HEIGHT,
                                                    "medium")

                # Display questions as buttons
                if self.npc == "Silvia 2.0":
                    # Stage 0
                    if self.stage == 0:
                        questionOneButtonSilviaAI.draw(self.screen)
                        questionTwoButtonSilviaAI.draw(self.screen)
                        questionThreeButtonSilviaAI.draw(self.screen)

                        if self.buildString == self.secretString:
                            questionFourButtonSilviaAI.draw(self.screen)
                        else:
                            hideSecretQuestionSilviaAI.draw(self.screen)
                    # Stage 2
                    elif self.stage == 2:
                        questionFiveButtonSilviaAI.draw(self.screen)
                        questionSixButtonSilviaAI.draw(self.screen)
                        questionSevenButtonSilviaAI.draw(self.screen)

                        if self.buildString == self.secretString:
                            questionEightButtonSilviaAI.draw(self.screen)
                        else:
                            hideSecretQuestionSilviaAI.draw(self.screen)
                    # Stage 4
                    elif self.stage == 4:
                        questionNineButtonSilviaAI.draw(self.screen)
                        questionTenButtonSilviaAI.draw(self.screen)
                        questionElevenButtonSilviaAI.draw(self.screen)

                        if self.buildString == self.secretString:
                            questionTwelveButtonSilviaAI.draw(self.screen)
                        else:
                            hideSecretQuestionSilviaAI.draw(self.screen)
                    # Stage 6
                    elif self.stage == 6:
                        questionThirteenButtonSilviaAI.draw(self.screen)
                        questionFourteenButtonSilviaAI.draw(self.screen)
                        questionFifteenButtonSilviaAI.draw(self.screen)

                        if self.buildString == self.secretString:
                            questionSixteenButtonSilviaAI.draw(self.screen)
                        else:
                            hideSecretQuestionSilviaAI.draw(self.screen)
                
                elif self.npc == "Silvia Jade":
                    # Stage 1
                    if self.stage == 1:
                        questionOneButtonSilviaHuman.draw(self.screen)
                        questionTwoButtonSilviaHuman.draw(self.screen)
                        questionThreeButtonSilviaHuman.draw(self.screen)

                        if self.buildString == self.secretString:
                            questionFourButtonSilviaHuman.draw(self.screen)
                        else:
                            hideSecretQuestionSilviaHuman.draw(self.screen)
                    # Stage 3
                    elif self.stage == 3:
                        questionFiveButtonSilviaHuman.draw(self.screen)
                        questionSixButtonSilviaHuman.draw(self.screen)
                        questionSevenButtonSilviaHuman.draw(self.screen)

                        if self.buildString == self.secretString:
                            questionEightButtonSilviaHuman.draw(self.screen)
                        else:
                            hideSecretQuestionSilviaHuman.draw(self.screen)
                    # Stage 5
                    elif self.stage == 5:
                        questionNineButtonSilviaHuman.draw(self.screen)
                        questionTenButtonSilviaHuman.draw(self.screen)
                        questionElevenButtonSilviaHuman.draw(self.screen)

                        if self.buildString == self.secretString:
                            questionTwelveButtonSilviaHuman.draw(self.screen)
                        else:
                            hideSecretQuestionSilviaHuman.draw(self.screen)
                    # Stage 7
                    elif self.stage == 7:
                        questionThirteenButtonSilviaHuman.draw(self.screen)
                        questionFourteenButtonSilviaHuman.draw(self.screen)
                        questionFifteenButtonSilviaHuman.draw(self.screen)

                        if self.buildString == self.secretString:
                            questionSixteenButtonSilviaHuman.draw(self.screen)
                        else:
                            hideSecretQuestionSilviaHuman.draw(self.screen)
                    
                # Depending on even above a answer will be returned
                if self.displayAnswer == True:
                    # Scripted NPC response
                    self.textManager.scriptedResponse(self.screen, self.question, self.npc)
                    self.displayAnswer = False

                    # Nonscripted NPC response
                    # if self.npc == "Silvia 2.0":
                    #     if self.question == 1:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionOneSilviaAI, self.npc)                            
                    #     elif self.question == 2:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionTwoSilviaAI, self.npc)                           
                    #     elif self.question == 3:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionThreeSilviaAI, self.npc)                            
                    #     elif self.question == 4:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionFourSilviaAI, self.npc)                           
                    #     elif self.question == 5:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionFiveSilviaAI, self.npc)                           
                    #     elif self.question == 6:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionSixSilviaAI, self.npc)                           
                    #     elif self.question == 7:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionSevenSilviaAI, self.npc)                           
                    #     elif self.question == 8:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionEightSilviaAI, self.npc)                           
                    #     elif self.question == 9:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionNineSilviaAI, self.npc)                            
                    #     elif self.question == 10:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionTenSilviaAI, self.npc)                           
                    #     elif self.question == 11:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionElevenSilviaAI, self.npc)                           
                    #     elif self.question == 12:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionTwelveSilviaAI, self.npc)                           
                    #     elif self.question == 13:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionThirteenSilviaAI, self.npc)                           
                    #     elif self.question == 14:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionFourteenSilviaAI, self.npc)                           
                    #     elif self.question == 15:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionFifteenSilviaAI, self.npc)                           
                    #     elif self.question == 16:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionSixteenSilviaAI, self.npc)                           

                    # elif self.npc == "Silvia Jade":
                    #     if self.question == 1:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionOneSilviaHuman, self.npc)                       
                    #     elif self.question == 2:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionTwoSilviaHuman, self.npc)                           
                    #     elif self.question == 3:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionThreeSilviaHuman, self.npc)                           
                    #     elif self.question == 4:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionFourSilviaHuman, self.npc)                           
                    #     elif self.question == 5:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionFiveSilviaHuman, self.npc)                           
                    #     elif self.question == 6:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionSixSilviaHuman, self.npc)                           
                    #     elif self.question == 7:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionSevenSilviaHuman, self.npc)                            
                    #     elif self.question == 8:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionEightSilviaHuman, self.npc)                           
                    #     elif self.question == 9:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionNineSilviaHuman, self.npc)                            
                    #     elif self.question == 10:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionTenSilviaHuman, self.npc)                           
                    #     elif self.question == 11:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionElevenSilviaHuman, self.npc)                           
                    #     elif self.question == 12:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionTwelveSilviaHuman, self.npc)                           
                    #     elif self.question == 13:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionThirteenSilviaHuman, self.npc)                            
                    #     elif self.question == 14:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionFourteenSilviaHuman, self.npc)                            
                    #     elif self.question == 15:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionFifteenSilviaHuman, self.npc)                            
                    #     elif self.question == 16:
                    #         self.aiChat.nonscriptedResponse(self.screen, questionSixteenSilviaHuman, self.npc)
                            
                    self.displayAnswer = False
                    
            pygame.display.flip()
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()