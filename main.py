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
        self.time = 0
        self.lastClickTime = 0
        self.pauseClick = 6

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
        self.coolDown = "QUESTION BUTTON: COOL DOWN"
        self.ready = "QUESTION BUTTON: READY"

        # Display text in guilty_suspect
        self.whosGuilty = "SELECT WHO IS GUILTY"
        self.correct = "CORRECT"
        self.wrong = "WRONG"

        # NPC based variables
        self.npc = " "
        self.npcSelect = " "
        self.npcGuilty = "Silvia Jade"
        self.npcBoolean = " "

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
        self.lastClickTime = self.time

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

                    # Guess guilty suspect clicked changes scene
                    if guessGuiltySuspect.handle_event(event) and self.stage == 20:
                        self.scene = "guilty_suspect"
                        print(self.scene)

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

                    if self.npcGuilty == "Silvia Jade":
                        # Handles events for Silvia 2.0
                        if self.npc == "Silvia 2.0":
                            if self.time - self.lastClickTime >= self.pauseClick or self.lastClickTime == 0:
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
                                # Stage 8
                                elif self.stage == 8:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionSeventeenButtonSilviaAI.handle_event(event):
                                        self.question = 17
                                        self.stages(self.slotOne, self.npc)

                                    elif questionEighteenButtonSilviaAI.handle_event(event):
                                        self.question = 18
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionNineteenButtonSilviaAI.handle_event(event):
                                        self.question = 19
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionTwentyButtonSilviaAI.handle_event(event):
                                            self.question = 20
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 9
                                # Stage 10
                                elif self.stage == 10:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionTwentyOneButtonSilviaAI.handle_event(event):
                                        self.question = 21
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTwentyTwoButtonSilviaAI.handle_event(event):
                                        self.question = 22
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionTwentyThreeButtonSilviaAI.handle_event(event):
                                        self.question = 23
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionTwentyFourButtonSilviaAI.handle_event(event):
                                            self.question = 24
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 11
                                # Stage 12
                                elif self.stage == 12:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionTwentyFiveButtonSilviaAI.handle_event(event):
                                        self.question = 25
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTwentySixButtonSilviaAI.handle_event(event):
                                        self.question = 26
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionTwentySevenButtonSilviaAI.handle_event(event):
                                        self.question = 27
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionTwentyEightButtonSilviaAI.handle_event(event):
                                            self.question = 28
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 13
                                # Stage 14
                                elif self.stage == 14:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionTwentyNineButtonSilviaAI.handle_event(event):
                                        self.question = 29
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyButtonSilviaAI.handle_event(event):
                                        self.question = 30
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyOneButtonSilviaAI.handle_event(event):
                                        self.question = 31
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionThirtyTwoButtonSilviaAI.handle_event(event):
                                            self.question = 32
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 15
                                # Stage 16
                                elif self.stage == 16:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionThirtyThreeButtonSilviaAI.handle_event(event):
                                        self.question = 33
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyFourButtonSilviaAI.handle_event(event):
                                        self.question = 34
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyFiveButtonSilviaAI.handle_event(event):
                                        self.question = 35
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionThirtySixButtonSilviaAI.handle_event(event):
                                            self.question = 36
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 17
                                # Stage 18
                                elif self.stage == 18:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionThirtySevenButtonSilviaAI.handle_event(event):
                                        self.question = 37
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyEightButtonSilviaAI.handle_event(event):
                                        self.question = 38
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyNineButtonSilviaAI.handle_event(event):
                                        self.question = 39
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionFourtyButtonSilviaAI.handle_event(event):
                                            self.question = 40
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 19

                        # Handles events for Silvia Jade
                        if self.npc == "Silvia Jade":
                            if self.time - self.lastClickTime >= self.pauseClick:
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
                                # Stage 9
                                elif self.stage == 9:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionSeventeenButtonSilviaHuman.handle_event(event):
                                        self.question = 17
                                        self.stages(self.slotOne, self.npc)

                                    elif questionEighteenButtonSilviaHuman.handle_event(event):
                                        self.question = 18
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionNineteenButtonSilviaHuman.handle_event(event):
                                        self.question = 19
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionTwentyButtonSilviaHuman.handle_event(event):
                                            self.question = 20
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 10
                                # Stage 11
                                elif self.stage == 11:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionTwentyOneButtonSilviaHuman.handle_event(event):
                                        self.question = 21
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTwentyTwoButtonSilviaHuman.handle_event(event):
                                        self.question = 22
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionTwentyThreeButtonSilviaHuman.handle_event(event):
                                        self.question = 23
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionTwentyFourButtonSilviaHuman.handle_event(event):
                                            self.question = 24
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 12
                                # Stage 13
                                elif self.stage == 13:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionTwentyFiveButtonSilviaHuman.handle_event(event):
                                        self.question = 25
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTwentySixButtonSilviaHuman.handle_event(event):
                                        self.question = 26
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionTwentySevenButtonSilviaHuman.handle_event(event):
                                        self.question = 27
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionTwentyEightButtonSilviaHuman.handle_event(event):
                                            self.question = 28
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 14
                                # Stage 15
                                elif self.stage == 15:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionTwentyNineButtonSilviaHuman.handle_event(event):
                                        self.question = 29
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyButtonSilviaHuman.handle_event(event):
                                        self.question = 30
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyOneButtonSilviaHuman.handle_event(event):
                                        self.question = 31
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionThirtyTwoButtonSilviaHuman.handle_event(event):
                                            self.question = 32
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 16
                                # Stage 17
                                elif self.stage == 17:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionThirtyThreeButtonSilviaHuman.handle_event(event):
                                        self.question = 33
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyFourButtonSilviaHuman.handle_event(event):
                                        self.question = 34
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyFiveButtonSilviaHuman.handle_event(event):
                                        self.question = 35
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionThirtySixButtonSilviaHuman.handle_event(event):
                                            self.question = 36
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 18
                                # Stage 19
                                elif self.stage == 19:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionThirtySevenButtonSilviaHuman.handle_event(event):
                                        self.question = 37
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyEightButtonSilviaHuman.handle_event(event):
                                        self.question = 38
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyNineButtonSilviaHuman.handle_event(event):
                                        self.question = 39
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionFourtyButtonSilviaHuman.handle_event(event):
                                            self.question = 40
                                            self.stages(self.slotFour, self.npc)
                                            # Stage ends here for now
                                            self.stage = 20

                elif self.scene == "guilty_suspect":
                    self.screen.fill('black')

                    if self.npcBoolean == " ":
                        if guiltySilviaAI.handle_event(event):
                            self.npc = "Silvia 2.0"
                            if self.npcGuilty == self.npc:
                                self.npcBoolean = True

                            elif self.npcGuilty != self.npc:
                                self.npcBoolean = False

                        if guiltySilviaHuman.handle_event(event):
                            self.npc = "Silvia Jade"
                            if self.npcGuilty == self.npc:
                                self.npcBoolean = True
                                
                            elif self.npcGuilty != self.npc:
                                self.npcBoolean = False

            # Used for timing of game
            delta_time = self.clock.tick() / 1000
            # self.level.run(delta_time)
            self.time = self.time + delta_time
            # print(self.time)

            # Scenemanager for while loop
            if self.scene == "main_menu":
                startGame.drawMediumButton(self.screen)
                self.textManager.displayRedText(self.screen, self.electricSheepTitle,
                                                  ELECTRIC_SHEEP_X, ELECTRIC_SHEEP_Y, ELECTRIC_SHEEP_WIDTH, ELECTRIC_SHEEP_HEIGHT,
                                                  "extra large")

            elif self.scene == "interrogation":
                # Keeps sprite images in sprites group being continuously displayed if in group
                self.sprites.update()

                # Display NPC names to select from based off npc name string
                if self.stage != 20:
                    if self.npcSelect == " " or self.npcSelect == "Silvia 2.0":
                        aiSilvia.draw(self.screen)
                    elif self.npcSelect == "Silvia Jade":
                        humanSilvia.draw(self.screen)
                elif self.stage == 20:
                    guessGuiltySuspect.drawMediumButton(self.screen)
                    # self.scene = "guilty_suspect"

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
                self.textManager.displayRedText(self.screen, str(int(self.time)),
                                                    TIME_X, TIME_Y, TIME_WIDTH, TIME_HEIGHT,
                                                    "medium")
                
                if self.time - self.lastClickTime >= self.pauseClick or self.lastClickTime == 0:
                    self.textManager.displayRedText(self.screen, self.ready,
                                                   COOL_DOWN_X, COOL_DOWN_Y, COOL_DOWN_WIDTH, COOL_DOWN_HEIGHT,
                                                   "small")
                else:
                    self.textManager.displayRedText(self.screen, self.coolDown,
                                                   COOL_DOWN_X, COOL_DOWN_Y, COOL_DOWN_WIDTH, COOL_DOWN_HEIGHT,
                                                   "small")

                if self.npcGuilty == "Silvia Jade":
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
                        # Stage 8
                        elif self.stage == 8:
                            questionSeventeenButtonSilviaAI.draw(self.screen)
                            questionEighteenButtonSilviaAI.draw(self.screen)
                            questionNineteenButtonSilviaAI.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionTwentyButtonSilviaAI.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaAI.draw(self.screen)
                        # Stage 10
                        elif self.stage == 10:
                            questionTwentyOneButtonSilviaAI.draw(self.screen)
                            questionTwentyTwoButtonSilviaAI.draw(self.screen)
                            questionTwentyThreeButtonSilviaAI.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionTwentyFourButtonSilviaAI.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaAI.draw(self.screen)
                        # Stage 12
                        elif self.stage == 12:
                            questionTwentyFiveButtonSilviaAI.draw(self.screen)
                            questionTwentySixButtonSilviaAI.draw(self.screen)
                            questionTwentySevenButtonSilviaAI.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionTwentyEightButtonSilviaAI.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaAI.draw(self.screen)
                        # Stage 14
                        elif self.stage == 14:
                            questionTwentyNineButtonSilviaAI.draw(self.screen)
                            questionThirtyButtonSilviaAI.draw(self.screen)
                            questionThirtyOneButtonSilviaAI.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionThirtyTwoButtonSilviaAI.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaAI.draw(self.screen)
                        # Stage 16
                        elif self.stage == 16:
                            questionThirtyThreeButtonSilviaAI.draw(self.screen)
                            questionThirtyFourButtonSilviaAI.draw(self.screen)
                            questionThirtyFiveButtonSilviaAI.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionThirtySixButtonSilviaAI.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaAI.draw(self.screen)
                        # Stage 18
                        elif self.stage == 18:
                            questionThirtySevenButtonSilviaAI.draw(self.screen)
                            questionThirtyEightButtonSilviaAI.draw(self.screen)
                            questionThirtyNineButtonSilviaAI.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionFourtyButtonSilviaAI.draw(self.screen)
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
                        # Stage 9
                        elif self.stage == 9:
                            questionSeventeenButtonSilviaHuman.draw(self.screen)
                            questionEighteenButtonSilviaHuman.draw(self.screen)
                            questionNineteenButtonSilviaHuman.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionTwentyButtonSilviaHuman.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaHuman.draw(self.screen)
                        # Stage 11
                        elif self.stage == 11:
                            questionTwentyOneButtonSilviaHuman.draw(self.screen)
                            questionTwentyTwoButtonSilviaHuman.draw(self.screen)
                            questionTwentyThreeButtonSilviaHuman.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionTwentyFourButtonSilviaHuman.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaHuman.draw(self.screen)
                        # Stage 13
                        elif self.stage == 13:
                            questionTwentyFiveButtonSilviaHuman.draw(self.screen)
                            questionTwentySixButtonSilviaHuman.draw(self.screen)
                            questionTwentySevenButtonSilviaHuman.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionTwentyEightButtonSilviaHuman.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaHuman.draw(self.screen)
                        # Stage 15
                        elif self.stage == 15:
                            questionTwentyNineButtonSilviaHuman.draw(self.screen)
                            questionThirtyButtonSilviaHuman.draw(self.screen)
                            questionThirtyOneButtonSilviaHuman.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionThirtyTwoButtonSilviaHuman.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaHuman.draw(self.screen)
                        # Stage 17
                        elif self.stage == 17:
                            questionThirtyThreeButtonSilviaHuman.draw(self.screen)
                            questionThirtyFourButtonSilviaHuman.draw(self.screen)
                            questionThirtyFiveButtonSilviaHuman.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionThirtySixButtonSilviaHuman.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaHuman.draw(self.screen)
                        # Stage 19
                        elif self.stage == 19:
                            questionThirtySevenButtonSilviaHuman.draw(self.screen)
                            questionThirtyEightButtonSilviaHuman.draw(self.screen)
                            questionThirtyNineButtonSilviaHuman.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionFourtyButtonSilviaHuman.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaHuman.draw(self.screen)
                        
                # Depending on even above a answer will be returned
                if self.displayAnswer == True:

                    if self.npcGuilty == "Silvia Jade":
                        # Scripted NPC response
                        # self.textManager.scriptedResponse(self.screen, self.question, self.npc)
                        # self.displayAnswer = False

                        # Nonscripted NPC response
                        if self.npc == "Silvia 2.0":
                            if self.question == 1:
                                self.aiChat.nonscriptedResponse(self.screen, questionOneSilviaAI, self.npc)                            
                            elif self.question == 2:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwoSilviaAI, self.npc)                           
                            elif self.question == 3:
                                self.aiChat.nonscriptedResponse(self.screen, questionThreeSilviaAI, self.npc)                            
                            elif self.question == 4:
                                self.aiChat.nonscriptedResponse(self.screen, questionFourSilviaAI, self.npc)                           
                            elif self.question == 5:
                                self.aiChat.nonscriptedResponse(self.screen, questionFiveSilviaAI, self.npc)                           
                            elif self.question == 6:
                                self.aiChat.nonscriptedResponse(self.screen, questionSixSilviaAI, self.npc)                           
                            elif self.question == 7:
                                self.aiChat.nonscriptedResponse(self.screen, questionSevenSilviaAI, self.npc)                           
                            elif self.question == 8:
                                self.aiChat.nonscriptedResponse(self.screen, questionEightSilviaAI, self.npc)                           
                            elif self.question == 9:
                                self.aiChat.nonscriptedResponse(self.screen, questionNineSilviaAI, self.npc)                            
                            elif self.question == 10:
                                self.aiChat.nonscriptedResponse(self.screen, questionTenSilviaAI, self.npc)                           
                            elif self.question == 11:
                                self.aiChat.nonscriptedResponse(self.screen, questionElevenSilviaAI, self.npc)                           
                            elif self.question == 12:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwelveSilviaAI, self.npc)                           
                            elif self.question == 13:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirteenSilviaAI, self.npc)                           
                            elif self.question == 14:
                                self.aiChat.nonscriptedResponse(self.screen, questionFourteenSilviaAI, self.npc)                           
                            elif self.question == 15:
                                self.aiChat.nonscriptedResponse(self.screen, questionFifteenSilviaAI, self.npc)                           
                            elif self.question == 16:
                                self.aiChat.nonscriptedResponse(self.screen, questionSixteenSilviaAI, self.npc)
                            elif self.question == 17:
                                self.aiChat.nonscriptedResponse(self.screen, questionSeventeenSilviaAI, self.npc)                           
                            elif self.question == 18:
                                self.aiChat.nonscriptedResponse(self.screen, questionEighteenSilviaAI, self.npc)                           
                            elif self.question == 19:
                                self.aiChat.nonscriptedResponse(self.screen, questionNineteenSilviaAI, self.npc)                            
                            elif self.question == 20:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentySilviaAI, self.npc)                           
                            elif self.question == 21:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentyOneSilviaAI, self.npc)                           
                            elif self.question == 22:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentyTwoSilviaAI, self.npc)                           
                            elif self.question == 23:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentyThreeSilviaAI, self.npc)                           
                            elif self.question == 24:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentyFourSilviaAI, self.npc)                           
                            elif self.question == 25:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentyFiveSilviaAI, self.npc)                           
                            elif self.question == 26:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentySixSilviaAI, self.npc)
                            elif self.question == 27:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentySevenSilviaAI, self.npc)                           
                            elif self.question == 28:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentyEightSilviaAI, self.npc)                           
                            elif self.question == 29:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentyNineSilviaAI, self.npc)                            
                            elif self.question == 30:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtySilviaAI, self.npc)
                            elif self.question == 31:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtyOneSilviaAI, self.npc)                           
                            elif self.question == 32:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtyTwoSilviaAI, self.npc)                           
                            elif self.question == 33:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtyThreeSilviaAI, self.npc)                           
                            elif self.question == 34:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtyFourSilviaAI, self.npc)                           
                            elif self.question == 35:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtyFiveSilviaAI, self.npc)                           
                            elif self.question == 36:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtySixSilviaAI, self.npc)
                            elif self.question == 37:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtySevenSilviaAI, self.npc)                           
                            elif self.question == 38:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtyEightSilviaAI, self.npc)                           
                            elif self.question == 39:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtyNineSilviaAI, self.npc)                            
                            elif self.question == 40:
                                self.aiChat.nonscriptedResponse(self.screen, questionFourtySilviaAI, self.npc)   

                        elif self.npc == "Silvia Jade":
                            if self.question == 1:
                                self.aiChat.nonscriptedResponse(self.screen, questionOneSilviaHuman, self.npc)                       
                            elif self.question == 2:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwoSilviaHuman, self.npc)                           
                            elif self.question == 3:
                                self.aiChat.nonscriptedResponse(self.screen, questionThreeSilviaHuman, self.npc)                           
                            elif self.question == 4:
                                self.aiChat.nonscriptedResponse(self.screen, questionFourSilviaHuman, self.npc)                           
                            elif self.question == 5:
                                self.aiChat.nonscriptedResponse(self.screen, questionFiveSilviaHuman, self.npc)                           
                            elif self.question == 6:
                                self.aiChat.nonscriptedResponse(self.screen, questionSixSilviaHuman, self.npc)                           
                            elif self.question == 7:
                                self.aiChat.nonscriptedResponse(self.screen, questionSevenSilviaHuman, self.npc)                            
                            elif self.question == 8:
                                self.aiChat.nonscriptedResponse(self.screen, questionEightSilviaHuman, self.npc)                           
                            elif self.question == 9:
                                self.aiChat.nonscriptedResponse(self.screen, questionNineSilviaHuman, self.npc)                            
                            elif self.question == 10:
                                self.aiChat.nonscriptedResponse(self.screen, questionTenSilviaHuman, self.npc)                           
                            elif self.question == 11:
                                self.aiChat.nonscriptedResponse(self.screen, questionElevenSilviaHuman, self.npc)                           
                            elif self.question == 12:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwelveSilviaHuman, self.npc)                           
                            elif self.question == 13:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirteenSilviaHuman, self.npc)                            
                            elif self.question == 14:
                                self.aiChat.nonscriptedResponse(self.screen, questionFourteenSilviaHuman, self.npc)                            
                            elif self.question == 15:
                                self.aiChat.nonscriptedResponse(self.screen, questionFifteenSilviaHuman, self.npc)                            
                            elif self.question == 16:
                                self.aiChat.nonscriptedResponse(self.screen, questionSixteenSilviaHuman, self.npc)
                            elif self.question == 17:
                                self.aiChat.nonscriptedResponse(self.screen, questionSeventeenSilviaHuman, self.npc)                           
                            elif self.question == 18:
                                self.aiChat.nonscriptedResponse(self.screen, questionEighteenSilviaHuman, self.npc)                           
                            elif self.question == 19:
                                self.aiChat.nonscriptedResponse(self.screen, questionNineteenSilviaHuman, self.npc)                            
                            elif self.question == 20:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentySilviaHuman, self.npc)                           
                            elif self.question == 21:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentyOneSilviaHuman, self.npc)                           
                            elif self.question == 22:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentyTwoSilviaHuman, self.npc)                           
                            elif self.question == 23:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentyThreeSilviaHuman, self.npc)                           
                            elif self.question == 24:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentyFourSilviaHuman, self.npc)                           
                            elif self.question == 25:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentyFiveSilviaHuman, self.npc)                           
                            elif self.question == 26:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentySixSilviaHuman, self.npc)
                            elif self.question == 27:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentySevenSilviaHuman, self.npc)                           
                            elif self.question == 28:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentyEightSilviaHuman, self.npc)                           
                            elif self.question == 29:
                                self.aiChat.nonscriptedResponse(self.screen, questionTwentyNineSilviaHuman, self.npc)                            
                            elif self.question == 30:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtySilviaHuman, self.npc)
                            elif self.question == 31:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtyOneSilviaHuman, self.npc)                           
                            elif self.question == 32:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtyTwoSilviaHuman, self.npc)                           
                            elif self.question == 33:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtyThreeSilviaHuman, self.npc)                           
                            elif self.question == 34:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtyFourSilviaHuman, self.npc)                           
                            elif self.question == 35:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtyFiveSilviaHuman, self.npc)                           
                            elif self.question == 36:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtySixSilviaHuman, self.npc)
                            elif self.question == 37:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtySevenSilviaHuman, self.npc)                           
                            elif self.question == 38:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtyEightSilviaHuman, self.npc)                           
                            elif self.question == 39:
                                self.aiChat.nonscriptedResponse(self.screen, questionThirtyNineSilviaHuman, self.npc)                            
                            elif self.question == 40:
                                self.aiChat.nonscriptedResponse(self.screen, questionFourtySilviaHuman, self.npc)
                                
                        self.displayAnswer = False

            elif self.scene == "guilty_suspect":
                if self.npcBoolean == " ":
                    guiltySilviaAI.drawMediumButton(self.screen)
                    guiltySilviaHuman.drawMediumButton(self.screen)

                    self.textManager.displayRedText(self.screen, self.whosGuilty,
                                                    GUILTY_X, GUILTY_Y, GUILTY_WIDTH, GUILTY_HEIGHT,
                                                    "large")
                if self.npcBoolean == True:
                    self.textManager.displayRedText(self.screen, self.correct,
                                                    CORRECT_X, CORRECT_Y, CORRECT_WIDTH, CORRECT_HEIGHT,
                                                    "extra large")
                elif self.npcBoolean == False:
                    self.textManager.displayRedText(self.screen, self.wrong,
                                                    WRONG_X, WRONG_Y, WRONG_WIDTH, WRONG_HEIGHT,
                                                    "extra large")

            pygame.display.flip()
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()