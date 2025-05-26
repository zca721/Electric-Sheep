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
        self.scene = "settings"
        # self.scene = "main_menu"
        # self.scene = "guilty_suspect"

        # Used for calculating the width of the characters based off font size to determine next line in input text
        self.mediumFont = pygame.font.Font('freesansbold.ttf', MEDIUM_FONT)

        # Full screen mode
        # self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.time = 0
        self.lastClickTime = 0
        self.pauseClick = 6

        # Sound effects
        pygame.mixer.init()
        # self.buttonClickError = pygame.mixer.Sound("./sounds/buttonClickError.mp3")
        # self.interrogationMusic = pygame.mixer.Sound("./sounds/interrogationMusic.mp3")
        # self.interrogationMusic.set_volume(0.1)
        pygame.mixer.music.load("./sounds/interrogationMusic.mp3")
        pygame.mixer.music.play(-1)  # Loop the music indefinitely
        

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
        # self.responseType = "nonscripted"
        # self.responseType = "scripted"
        self.responseType = " "
        self.displayAnswer = False
        self.silviaAIBoolean = True
        self.silviaJadeBoolean = True
        self.questionOneBoolean = True
        self.questionTwoBoolean = True
        self.questionThreeBoolean = True
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

        # Text input variables
        self.inputText = [""]
        self.buildText = ""
        self.index = 0
        self.allowInput = True
        # self.keyStroke = False

        # Display text in main menu
        self.electricSheepTitle = "ELECTRIC SHEEP"

        # Display text in settings menu
        self.settings = "SETTINGS"
        self.selected = "X"

        # Display text in game decription
        self.gameDescription = "DETECTIVE LOG"
        self.gameDescriptionOne = "Burgermeister is missing—no body, no signs of struggle, and the Fortress remains locked"
        self.gameDescriptionTwo = "from the inside. I’ve been brought in to question the only two who might know what" 
        self.gameDescriptionThree = "happened. Silvia 2.0—his AI assistant, calm, precise, and built in the image of his"
        self.gameDescriptionFour = "daughter. And Silvia Jade—his real daughter, believed dead for years, now suddenly"
        self.gameDescriptionFive = "back with a complicated past. I can ask each of them up to three questions, with a"
        self.gameDescriptionSix = "possible fourth if I push just right. There's a short pause—six seconds—between each"
        self.gameDescriptionSeven = "question, just long enough to keep the pressure steady. One of them knows what"
        self.gameDescriptionEight = "happened to Burgermeister. I need to find out who."

        # Display text in iterrogation
        self.selectSuspect = "SELECT SUSPECT"
        self.selectQuestion = "SELECT INTERROGATION QUESTION"
        self.stageDisplay = "STAGE "
        self.timeDisplay = " SECONDS"
        self.coolDown = "QUESTION BUTTON: COOL DOWN"
        self.ready = "QUESTION BUTTON: READY"

        # Display text in guilty_suspect
        self.inputReason = "PLEASE TYPE IN WHY YOU CHOSE WHO WAS GUILTY"
        self.whosGuilty = "SELECT WHO IS GUILTY"
        self.correct = "CORRECT"
        self.wrong = "WRONG"

        # NPC based variables
        self.npc = " "
        self.npcSelect = " "
        self.npcBoolean = " "
        self.npcGuilty = " "
        # self.npcGuilty = "Silvia Jade"
        # self.npcGuilty = "Silvia 2.0"

    # Helper functions
    # Builds secret string for each stage
    def stages(self, questionSlot, npc):
        if questionSlot == 1:
            self.buildString = self.buildString | self.questionOneString
            self.questionOneBoolean = False
        elif questionSlot == 2:
            self.buildString = self.buildString | self.questionTwoString
            self.questionTwoBoolean = False
        elif questionSlot == 3:
            self.buildString = self.buildString | self.questionThreeString
            self.questionThreeBoolean = False
        elif questionSlot == 4:
            self.buildString = 0
            self.questionOneBoolean = True
            self.questionTwoBoolean = True
            self.questionThreeBoolean = True
            if npc == "Silvia 2.0":
                self.npcSelect = "Silvia Jade" # Allows for NPC to be selected after secret question is asked
                self.silviaAIBoolean = True
            elif npc == "Silvia Jade":
                self.npcSelect = "Silvia 2.0" # Allows for NPC to be selected after secret question is asked
                self.silviaJadeBoolean = True
        
        self.displayAnswer = True
        self.lastClickTime = self.time

    def run(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Scenemanager for event
                if self.scene == "main_menu":
                    self.screen.fill('black')
                    if startGame.handle_event(event):

                        text = open("SystemInstructionOutput.txt", "a")
                        text.write("----------------------------------------------------------------------------------------------------------------------------------------" + "\n")
                        text.write("NEW GAME SESSION: " + self.responseType + "\n")
                        text.close()
                        
                        # self.scene = "interrogation"
                        self.scene = "game_description"

                    # Disabled for usability tests
                    # if settingsGame.handle_event(event):
                    #     self.scene = "settings"

                elif self.scene == "settings":
                    self.screen.fill('black')
                    if mainMenu.handle_event(event):
                        self.scene = "main_menu"

                    if scriptedResponse.handle_event(event):
                        self.responseType = "scripted"

                    elif nonscriptedResponse.handle_event(event):
                        self.responseType = "nonscripted"

                    if silviaAIGuilty.handle_event(event):
                        self.npcGuilty = "Silvia 2.0"

                    elif silviaHumanGuilty.handle_event(event):
                        self.npcGuilty = "Silvia Jade"

                elif self.scene == "game_description":
                    self.screen.fill('black')
                    if continueGame.handle_event(event):
                        self.scene = "interrogation"

                elif self.scene == "interrogation":
                    # Displays interrogation sprite images
                    self.sprites.add(self.interrogationBackground)
                    self.sprites.draw(self.screen)

                    # Plays background music when m is pressed
                    # if event.type == pygame.KEYDOWN:
                    #     if event.key == pygame.K_m:
                    #         pygame.mixer.music.load("./sounds/interrogationMusic.mp3")
                    #         pygame.mixer.music.play(-1)  # Loop the music indefinitely

                    # Guess guilty suspect clicked changes scene
                    if guessGuiltySuspect.handle_event(event) and self.stage == 20:
                        self.scene = "guilty_suspect"
                        print(self.scene)

                    # Depending on what NPC is clicked display associated questions
                    if aiSilvia.handle_event(event) and self.silviaAIBoolean == True:
                        self.npc = "Silvia 2.0"
                        self.displayAnswer = False
                        self.silviaAIBoolean = False
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

                    elif humanSilvia.handle_event(event) and self.silviaJadeBoolean == True:
                        self.npc = "Silvia Jade"
                        self.displayAnswer = False
                        self.silviaJadeBoolean = False
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
                                    if questionOneButtonSilviaAI.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 1
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTwoButtonSilviaAI.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 2
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThreeButtonSilviaAI.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionFiveButtonSilviaAI.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 5
                                        self.stages(self.slotOne, self.npc)

                                    elif questionSixButtonSilviaAI.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 6
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionSevenButtonSilviaAI.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionNineButtonSilviaAI.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 9
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTenButtonSilviaAI.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 10
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionElevenButtonSilviaAI.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionThirteenButtonSilviaAI.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 13
                                        self.stages(self.slotOne, self.npc)

                                    elif questionFourteenButtonSilviaAI.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 14
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionFifteenButtonSilviaAI.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionSeventeenButtonSilviaAI.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 17
                                        self.stages(self.slotOne, self.npc)

                                    elif questionEighteenButtonSilviaAI.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 18
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionNineteenButtonSilviaAI.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionTwentyOneButtonSilviaAI.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 21
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTwentyTwoButtonSilviaAI.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 22
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionTwentyThreeButtonSilviaAI.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionTwentyFiveButtonSilviaAI.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 25
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTwentySixButtonSilviaAI.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 26
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionTwentySevenButtonSilviaAI.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionTwentyNineButtonSilviaAI.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 29
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyButtonSilviaAI.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 30
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyOneButtonSilviaAI.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionThirtyThreeButtonSilviaAI.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 33
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyFourButtonSilviaAI.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 34
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyFiveButtonSilviaAI.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionThirtySevenButtonSilviaAI.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 37
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyEightButtonSilviaAI.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 38
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyNineButtonSilviaAI.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionOneButtonSilviaHumanGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 1
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTwoButtonSilviaHumanGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 2
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThreeButtonSilviaHumanGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 3
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionFourButtonSilviaHumanGuilty.handle_event(event):
                                            self.question = 4
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 2
                                # Stage 3
                                elif self.stage == 3:
                                    # Depending on what question is clicked a answer will be given
                                    if questionFiveButtonSilviaHumanGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 5
                                        self.stages(self.slotOne, self.npc)

                                    elif questionSixButtonSilviaHumanGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 6
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionSevenButtonSilviaHumanGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 7
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionEightButtonSilviaHumanGuilty.handle_event(event):
                                            self.question = 8
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 4
                                # Stage 5
                                elif self.stage == 5:
                                    # Depending on what question is clicked a answer will be given
                                    if questionNineButtonSilviaHumanGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 9
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTenButtonSilviaHumanGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 10
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionElevenButtonSilviaHumanGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 11
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionTwelveButtonSilviaHumanGuilty.handle_event(event):
                                            self.question = 12
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 6
                                # Stage 7
                                elif self.stage == 7:
                                    # Depending on what question is clicked a answer will be given
                                    if questionThirteenButtonSilviaHumanGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 13
                                        self.stages(self.slotOne, self.npc)

                                    elif questionFourteenButtonSilviaHumanGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 14
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionFifteenButtonSilviaHumanGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 15
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionSixteenButtonSilviaHumanGuilty.handle_event(event):
                                            self.question = 16
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 8
                                # Stage 9
                                elif self.stage == 9:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionSeventeenButtonSilviaHumanGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 17
                                        self.stages(self.slotOne, self.npc)

                                    elif questionEighteenButtonSilviaHumanGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 18
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionNineteenButtonSilviaHumanGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 19
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionTwentyButtonSilviaHumanGuilty.handle_event(event):
                                            self.question = 20
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 10
                                # Stage 11
                                elif self.stage == 11:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionTwentyOneButtonSilviaHumanGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 21
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTwentyTwoButtonSilviaHumanGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 22
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionTwentyThreeButtonSilviaHumanGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 23
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionTwentyFourButtonSilviaHumanGuilty.handle_event(event):
                                            self.question = 24
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 12
                                # Stage 13
                                elif self.stage == 13:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionTwentyFiveButtonSilviaHumanGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 25
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTwentySixButtonSilviaHumanGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 26
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionTwentySevenButtonSilviaHumanGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 27
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionTwentyEightButtonSilviaHumanGuilty.handle_event(event):
                                            self.question = 28
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 14
                                # Stage 15
                                elif self.stage == 15:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionTwentyNineButtonSilviaHumanGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 29
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyButtonSilviaHumanGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 30
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyOneButtonSilviaHumanGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 31
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionThirtyTwoButtonSilviaHumanGuilty.handle_event(event):
                                            self.question = 32
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 16
                                # Stage 17
                                elif self.stage == 17:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionThirtyThreeButtonSilviaHumanGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 33
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyFourButtonSilviaHumanGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 34
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyFiveButtonSilviaHumanGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 35
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionThirtySixButtonSilviaHumanGuilty.handle_event(event):
                                            self.question = 36
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 18
                                # Stage 19
                                elif self.stage == 19:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionThirtySevenButtonSilviaHumanGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 37
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyEightButtonSilviaHumanGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 38
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyNineButtonSilviaHumanGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 39
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionFourtyButtonSilviaHumanGuilty.handle_event(event):
                                            self.question = 40
                                            self.stages(self.slotFour, self.npc)
                                            # Stage ends here for now
                                            self.stage = 20
                    elif self.npcGuilty == "Silvia 2.0":
                        # Handles events for Silvia 2.0
                        if self.npc == "Silvia 2.0":
                            if self.time - self.lastClickTime >= self.pauseClick or self.lastClickTime == 0:
                                # Stage 0
                                if self.stage == 0:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionOneButtonSilviaAIGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 1
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTwoButtonSilviaAIGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 2
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThreeButtonSilviaAIGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 3
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionFourButtonSilviaAIGuilty.handle_event(event):
                                            self.question = 4
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 1
                                # Stage 2
                                elif self.stage == 2:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionFiveButtonSilviaAIGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 5
                                        self.stages(self.slotOne, self.npc)

                                    elif questionSixButtonSilviaAIGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 6
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionSevenButtonSilviaAIGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 7
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionEightButtonSilviaAIGuilty.handle_event(event):
                                            self.question = 8
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 3
                                # Stage 4
                                elif self.stage == 4:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionNineButtonSilviaAIGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 9
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTenButtonSilviaAIGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 10
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionElevenButtonSilviaAIGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 11
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionTwelveButtonSilviaAIGuilty.handle_event(event):
                                            self.question = 12
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 5
                                # Stage 6
                                elif self.stage == 6:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionThirteenButtonSilviaAIGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 13
                                        self.stages(self.slotOne, self.npc)

                                    elif questionFourteenButtonSilviaAIGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 14
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionFifteenButtonSilviaAIGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 15
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionSixteenButtonSilviaAIGuilty.handle_event(event):
                                            self.question = 16
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 7
                                # Stage 8
                                elif self.stage == 8:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionSeventeenButtonSilviaAIGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 17
                                        self.stages(self.slotOne, self.npc)

                                    elif questionEighteenButtonSilviaAIGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 18
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionNineteenButtonSilviaAIGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 19
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionTwentyButtonSilviaAIGuilty.handle_event(event):
                                            self.question = 20
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 9
                                # Stage 10
                                elif self.stage == 10:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionTwentyOneButtonSilviaAIGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 21
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTwentyTwoButtonSilviaAIGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 22
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionTwentyThreeButtonSilviaAIGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 23
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionTwentyFourButtonSilviaAIGuilty.handle_event(event):
                                            self.question = 24
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 11
                                # Stage 12
                                elif self.stage == 12:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionTwentyFiveButtonSilviaAIGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 25
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTwentySixButtonSilviaAIGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 26
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionTwentySevenButtonSilviaAIGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 27
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionTwentyEightButtonSilviaAIGuilty.handle_event(event):
                                            self.question = 28
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 13
                                # Stage 14
                                elif self.stage == 14:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionTwentyNineButtonSilviaAIGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 29
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyButtonSilviaAIGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 30
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyOneButtonSilviaAIGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 31
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionThirtyTwoButtonSilviaAIGuilty.handle_event(event):
                                            self.question = 32
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 15
                                # Stage 16
                                elif self.stage == 16:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionThirtyThreeButtonSilviaAIGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 33
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyFourButtonSilviaAIGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 34
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyFiveButtonSilviaAIGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 35
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionThirtySixButtonSilviaAIGuilty.handle_event(event):
                                            self.question = 36
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 17
                                # Stage 18
                                elif self.stage == 18:
                                    # Depending on what question is clicked a answer will be given with Silvia 2.0
                                    if questionThirtySevenButtonSilviaAIGuilty.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 37
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyEightButtonSilviaAIGuilty.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 38
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyNineButtonSilviaAIGuilty.handle_event(event) and self.questionThreeBoolean == True:
                                        self.question = 39
                                        self.stages(self.slotThree, self.npc)

                                    if self.buildString == self.secretString:
                                        if questionFourtyButtonSilviaAIGuilty.handle_event(event):
                                            self.question = 40
                                            self.stages(self.slotFour, self.npc)
                                            self.stage = 19

                        # Handles events for Silvia Jade
                        if self.npc == "Silvia Jade":
                            if self.time - self.lastClickTime >= self.pauseClick:
                                # Stage 1
                                if self.stage == 1:
                                    # Depending on what question is clicked a answer will be given
                                    if questionOneButtonSilviaHuman.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 1
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTwoButtonSilviaHuman.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 2
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThreeButtonSilviaHuman.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionFiveButtonSilviaHuman.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 5
                                        self.stages(self.slotOne, self.npc)

                                    elif questionSixButtonSilviaHuman.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 6
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionSevenButtonSilviaHuman.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionNineButtonSilviaHuman.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 9
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTenButtonSilviaHuman.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 10
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionElevenButtonSilviaHuman.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionThirteenButtonSilviaHuman.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 13
                                        self.stages(self.slotOne, self.npc)

                                    elif questionFourteenButtonSilviaHuman.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 14
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionFifteenButtonSilviaHuman.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionSeventeenButtonSilviaHuman.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 17
                                        self.stages(self.slotOne, self.npc)

                                    elif questionEighteenButtonSilviaHuman.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 18
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionNineteenButtonSilviaHuman.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionTwentyOneButtonSilviaHuman.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 21
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTwentyTwoButtonSilviaHuman.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 22
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionTwentyThreeButtonSilviaHuman.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionTwentyFiveButtonSilviaHuman.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 25
                                        self.stages(self.slotOne, self.npc)

                                    elif questionTwentySixButtonSilviaHuman.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 26
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionTwentySevenButtonSilviaHuman.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionTwentyNineButtonSilviaHuman.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 29
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyButtonSilviaHuman.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 30
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyOneButtonSilviaHuman.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionThirtyThreeButtonSilviaHuman.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 33
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyFourButtonSilviaHuman.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 34
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyFiveButtonSilviaHuman.handle_event(event) and self.questionThreeBoolean == True:
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
                                    if questionThirtySevenButtonSilviaHuman.handle_event(event) and self.questionOneBoolean == True:
                                        self.question = 37
                                        self.stages(self.slotOne, self.npc)

                                    elif questionThirtyEightButtonSilviaHuman.handle_event(event) and self.questionTwoBoolean == True:
                                        self.question = 38
                                        self.stages(self.slotTwo, self.npc)

                                    elif questionThirtyNineButtonSilviaHuman.handle_event(event) and self.questionThreeBoolean == True:
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
                    else:
                        if submit.handle_event(event) and self.allowInput == True:
                            for string in self.inputText:
                                self.buildText += string
                            self.allowInput = False
                            text = open("GuiltyVerdict.txt", "a")
                            text.write("Total Time: " + str(round(self.time/60, 2)) + "\n" + "Response Type: " + self.responseType + "\n" + "Guilty Suspect: " + self.npcGuilty + "\n" + "Suspect User Selected: " + self.npc + "\n")
                            text.write(self.buildText + "\n")
                            text.write("----------------------------------------------------------------------------------------------------------------------------------------" + "\n")
                            text.close()
                            print(self.buildText)

                        # Handles input text from user and disallows continuous key pressed
                        # if event.type == pygame.TEXTINPUT and self.keyStroke == False:
                        #     self.inputText[-1] += event.text
                        #     self.keyStroke = True

                        # Allows continuous key pressed but stops at text box width max
                        if event.type == pygame.TEXTINPUT and self.mediumFont.size(self.inputText[self.index])[0] <= INPUT_WIDTH - GAP_FONT and len(self.inputText) <= MAX_CHARACTERS:
                            self.inputText[-1] += event.text

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE:
                                # String splicing to remove last character from string
                                self.inputText[-1] = self.inputText[-1][:-1]
                                if len(self.inputText[-1]) == 0:
                                    if len(self.inputText) > 1:
                                        self.inputText = self.inputText[:-1]
                                        self.index -= 1
                            # Allows for nextline from hitting enter or amount of characters
                            # elif event.key == pygame.K_RETURN or len(self.inputText[self.index]) >= MAX_CHARACTERS:

                            # Allows for nextline when text length is greater or equal to the display text bow
                            elif self.mediumFont.size(self.inputText[self.index])[0] >= INPUT_WIDTH - GAP_FONT:
                                self.inputText.append("")
                                self.index += 1

                        # Part of disallowing continuous key pressed
                        # elif event.type == pygame.KEYUP and self.keyStroke == True:
                        #     self.keyStroke = False
                        

            # Used for timing of game
            delta_time = self.clock.tick() / 1000
            # self.level.run(delta_time)
            self.time = self.time + delta_time
            # print(self.time)

            # Scenemanager for while loop
            if self.scene == "main_menu":
                startGame.drawMediumButton(self.screen)

                # Disabled for usability tests
                # settingsGame.drawMediumButton(self.screen)

                self.textManager.displayRedText(self.screen, self.electricSheepTitle,
                                                  ELECTRIC_SHEEP_X, ELECTRIC_SHEEP_Y, ELECTRIC_SHEEP_WIDTH, ELECTRIC_SHEEP_HEIGHT,
                                                  "extra large")
                
            elif self.scene == "settings":
                mainMenu.drawMediumButton(self.screen)
                scriptedResponse.drawMediumButton(self.screen)
                nonscriptedResponse.drawMediumButton(self.screen)
                silviaAIGuilty.drawMediumButton(self.screen)
                silviaHumanGuilty.drawMediumButton(self.screen)

                self.textManager.displayRedText(self.screen, self.settings,
                                                  SETTINGS_TITLE_X, SETTINGS_TITLE_Y, SETTINGS_TITLE_WIDTH, SETTINGS_TITLE_HEIGHT,
                                                  "extra large")
                
                if self.npcGuilty == "Silvia 2.0":
                    self.textManager.displayRedText(self.screen, self.selected,
                                                  AI_GUILTY_X - SETTINGS_GAP_X, AI_GUILTY_Y - SETTINGS_GAP_Y, SETTINGS_GAP_X, SETTINGS_GAP_X,
                                                  "large")
                    
                elif self.npcGuilty == "Silvia Jade":
                    self.textManager.displayRedText(self.screen, self.selected,
                                                  HUMAN_GUILTY_X - SETTINGS_GAP_X, HUMAN_GUILTY_Y - SETTINGS_GAP_Y, SETTINGS_GAP_X, SETTINGS_GAP_X,
                                                  "large")
                    
                if self.responseType == "scripted":
                    self.textManager.displayRedText(self.screen, self.selected,
                                                  SCRIPTED_X - SETTINGS_GAP_X, SCRIPTED_Y - SETTINGS_GAP_Y, SETTINGS_GAP_X, SETTINGS_GAP_X,
                                                  "large")
                    
                elif self.responseType == "nonscripted":
                    self.textManager.displayRedText(self.screen, self.selected,
                                                  NONSCRIPTED_X - SETTINGS_GAP_X, NONSCRIPTED_Y - SETTINGS_GAP_Y, SETTINGS_GAP_X, SETTINGS_GAP_X,
                                                  "large")
                
            elif self.scene == "game_description":
                continueGame.drawMediumButton(self.screen)

                self.textManager.displayRedText(self.screen, self.gameDescription,
                                                  DESCRIPTION_TITLE_X, DESCRIPTION_TITLE_Y, DESCRIPTION_TITLE_WIDTH, DESCRIPTION_TITLE_HEIGHT,
                                                  "extra large")
                self.textManager.displayRedText(self.screen, self.gameDescriptionOne,
                                                  DESCRIPTION_X, DESCRIPTION_Y, DESCRIPTION_WIDTH, DESCRIPTION_HEIGHT,
                                                  "medium")
                self.textManager.displayRedText(self.screen, self.gameDescriptionTwo,
                                                  DESCRIPTION_X, DESCRIPTION_Y + DESCRIPTION_GAP, DESCRIPTION_WIDTH, DESCRIPTION_HEIGHT,
                                                  "medium")
                self.textManager.displayRedText(self.screen, self.gameDescriptionThree,
                                                  DESCRIPTION_X, DESCRIPTION_Y + (DESCRIPTION_GAP * 2), DESCRIPTION_WIDTH, DESCRIPTION_HEIGHT,
                                                  "medium")
                self.textManager.displayRedText(self.screen, self.gameDescriptionFour,
                                                  DESCRIPTION_X, DESCRIPTION_Y + (DESCRIPTION_GAP * 3), DESCRIPTION_WIDTH, DESCRIPTION_HEIGHT,
                                                  "medium")
                self.textManager.displayRedText(self.screen, self.gameDescriptionFive,
                                                  DESCRIPTION_X, DESCRIPTION_Y + (DESCRIPTION_GAP * 4), DESCRIPTION_WIDTH, DESCRIPTION_HEIGHT,
                                                  "medium")
                self.textManager.displayRedText(self.screen, self.gameDescriptionSix,
                                                  DESCRIPTION_X, DESCRIPTION_Y + (DESCRIPTION_GAP * 5), DESCRIPTION_WIDTH, DESCRIPTION_HEIGHT,
                                                  "medium")
                self.textManager.displayRedText(self.screen, self.gameDescriptionSeven,
                                                  DESCRIPTION_X, DESCRIPTION_Y + (DESCRIPTION_GAP * 6), DESCRIPTION_WIDTH, DESCRIPTION_HEIGHT,
                                                  "medium")
                self.textManager.displayRedText(self.screen, self.gameDescriptionEight,
                                                  DESCRIPTION_X, DESCRIPTION_Y + (DESCRIPTION_GAP * 7), DESCRIPTION_WIDTH, DESCRIPTION_HEIGHT,
                                                  "medium")
                

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
                # self.textManager.displayRedText(self.screen, str(int(self.time)) + self.timeDisplay,
                #                                     TIME_X, TIME_Y, TIME_WIDTH, TIME_HEIGHT,
                #                                     "medium")
                
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
                            questionOneButtonSilviaHumanGuilty.draw(self.screen)
                            questionTwoButtonSilviaHumanGuilty.draw(self.screen)
                            questionThreeButtonSilviaHumanGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionFourButtonSilviaHumanGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaHuman.draw(self.screen)
                        # Stage 3
                        elif self.stage == 3:
                            questionFiveButtonSilviaHumanGuilty.draw(self.screen)
                            questionSixButtonSilviaHumanGuilty.draw(self.screen)
                            questionSevenButtonSilviaHumanGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionEightButtonSilviaHumanGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaHuman.draw(self.screen)
                        # Stage 5
                        elif self.stage == 5:
                            questionNineButtonSilviaHumanGuilty.draw(self.screen)
                            questionTenButtonSilviaHumanGuilty.draw(self.screen)
                            questionElevenButtonSilviaHumanGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionTwelveButtonSilviaHumanGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaHuman.draw(self.screen)
                        # Stage 7
                        elif self.stage == 7:
                            questionThirteenButtonSilviaHumanGuilty.draw(self.screen)
                            questionFourteenButtonSilviaHumanGuilty.draw(self.screen)
                            questionFifteenButtonSilviaHumanGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionSixteenButtonSilviaHumanGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaHuman.draw(self.screen)
                        # Stage 9
                        elif self.stage == 9:
                            questionSeventeenButtonSilviaHumanGuilty.draw(self.screen)
                            questionEighteenButtonSilviaHumanGuilty.draw(self.screen)
                            questionNineteenButtonSilviaHumanGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionTwentyButtonSilviaHumanGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaHuman.draw(self.screen)
                        # Stage 11
                        elif self.stage == 11:
                            questionTwentyOneButtonSilviaHumanGuilty.draw(self.screen)
                            questionTwentyTwoButtonSilviaHumanGuilty.draw(self.screen)
                            questionTwentyThreeButtonSilviaHumanGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionTwentyFourButtonSilviaHumanGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaHuman.draw(self.screen)
                        # Stage 13
                        elif self.stage == 13:
                            questionTwentyFiveButtonSilviaHumanGuilty.draw(self.screen)
                            questionTwentySixButtonSilviaHumanGuilty.draw(self.screen)
                            questionTwentySevenButtonSilviaHumanGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionTwentyEightButtonSilviaHumanGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaHuman.draw(self.screen)
                        # Stage 15
                        elif self.stage == 15:
                            questionTwentyNineButtonSilviaHumanGuilty.draw(self.screen)
                            questionThirtyButtonSilviaHumanGuilty.draw(self.screen)
                            questionThirtyOneButtonSilviaHumanGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionThirtyTwoButtonSilviaHumanGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaHuman.draw(self.screen)
                        # Stage 17
                        elif self.stage == 17:
                            questionThirtyThreeButtonSilviaHumanGuilty.draw(self.screen)
                            questionThirtyFourButtonSilviaHumanGuilty.draw(self.screen)
                            questionThirtyFiveButtonSilviaHumanGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionThirtySixButtonSilviaHumanGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaHuman.draw(self.screen)
                        # Stage 19
                        elif self.stage == 19:
                            questionThirtySevenButtonSilviaHumanGuilty.draw(self.screen)
                            questionThirtyEightButtonSilviaHumanGuilty.draw(self.screen)
                            questionThirtyNineButtonSilviaHumanGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionFourtyButtonSilviaHumanGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaHuman.draw(self.screen)

                elif self.npcGuilty == "Silvia 2.0":
                    # Display questions as buttons
                    if self.npc == "Silvia 2.0":
                        # Stage 0
                        if self.stage == 0:
                            questionOneButtonSilviaAIGuilty.draw(self.screen)
                            questionTwoButtonSilviaAIGuilty.draw(self.screen)
                            questionThreeButtonSilviaAIGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionFourButtonSilviaAIGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaAI.draw(self.screen)
                        # Stage 2
                        elif self.stage == 2:
                            questionFiveButtonSilviaAIGuilty.draw(self.screen)
                            questionSixButtonSilviaAIGuilty.draw(self.screen)
                            questionSevenButtonSilviaAIGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionEightButtonSilviaAIGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaAI.draw(self.screen)
                        # Stage 4
                        elif self.stage == 4:
                            questionNineButtonSilviaAIGuilty.draw(self.screen)
                            questionTenButtonSilviaAIGuilty.draw(self.screen)
                            questionElevenButtonSilviaAIGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionTwelveButtonSilviaAIGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaAI.draw(self.screen)
                        # Stage 6
                        elif self.stage == 6:
                            questionThirteenButtonSilviaAIGuilty.draw(self.screen)
                            questionFourteenButtonSilviaAIGuilty.draw(self.screen)
                            questionFifteenButtonSilviaAIGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionSixteenButtonSilviaAIGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaAI.draw(self.screen)
                        # Stage 8
                        elif self.stage == 8:
                            questionSeventeenButtonSilviaAIGuilty.draw(self.screen)
                            questionEighteenButtonSilviaAIGuilty.draw(self.screen)
                            questionNineteenButtonSilviaAIGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionTwentyButtonSilviaAIGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaAI.draw(self.screen)
                        # Stage 10
                        elif self.stage == 10:
                            questionTwentyOneButtonSilviaAIGuilty.draw(self.screen)
                            questionTwentyTwoButtonSilviaAIGuilty.draw(self.screen)
                            questionTwentyThreeButtonSilviaAIGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionTwentyFourButtonSilviaAIGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaAI.draw(self.screen)
                        # Stage 12
                        elif self.stage == 12:
                            questionTwentyFiveButtonSilviaAIGuilty.draw(self.screen)
                            questionTwentySixButtonSilviaAIGuilty.draw(self.screen)
                            questionTwentySevenButtonSilviaAIGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionTwentyEightButtonSilviaAIGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaAI.draw(self.screen)
                        # Stage 14
                        elif self.stage == 14:
                            questionTwentyNineButtonSilviaAIGuilty.draw(self.screen)
                            questionThirtyButtonSilviaAIGuilty.draw(self.screen)
                            questionThirtyOneButtonSilviaAIGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionThirtyTwoButtonSilviaAIGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaAI.draw(self.screen)
                        # Stage 16
                        elif self.stage == 16:
                            questionThirtyThreeButtonSilviaAIGuilty.draw(self.screen)
                            questionThirtyFourButtonSilviaAIGuilty.draw(self.screen)
                            questionThirtyFiveButtonSilviaAIGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionThirtySixButtonSilviaAIGuilty.draw(self.screen)
                            else:
                                hideSecretQuestionSilviaAI.draw(self.screen)
                        # Stage 18
                        elif self.stage == 18:
                            questionThirtySevenButtonSilviaAIGuilty.draw(self.screen)
                            questionThirtyEightButtonSilviaAIGuilty.draw(self.screen)
                            questionThirtyNineButtonSilviaAIGuilty.draw(self.screen)

                            if self.buildString == self.secretString:
                                questionFourtyButtonSilviaAIGuilty.draw(self.screen)
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
                        if self.responseType == "scripted":
                            # Scripted NPC response
                            self.textManager.scriptedResponse(self.screen, self.question, self.npc, self.npcGuilty)
                            self.displayAnswer = False

                    
                        elif self.responseType == "nonscripted":
                            # Nonscripted NPC response
                            if self.npc == "Silvia 2.0":
                                if self.question == 1:
                                    self.aiChat.nonscriptedResponse(self.screen, questionOneSilviaAI, self.npc, self.npcGuilty)                            
                                elif self.question == 2:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwoSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 3:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThreeSilviaAI, self.npc, self.npcGuilty)                            
                                elif self.question == 4:
                                    self.aiChat.nonscriptedResponse(self.screen, questionFourSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 5:
                                    self.aiChat.nonscriptedResponse(self.screen, questionFiveSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 6:
                                    self.aiChat.nonscriptedResponse(self.screen, questionSixSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 7:
                                    self.aiChat.nonscriptedResponse(self.screen, questionSevenSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 8:
                                    self.aiChat.nonscriptedResponse(self.screen, questionEightSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 9:
                                    self.aiChat.nonscriptedResponse(self.screen, questionNineSilviaAI, self.npc, self.npcGuilty)                            
                                elif self.question == 10:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTenSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 11:
                                    self.aiChat.nonscriptedResponse(self.screen, questionElevenSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 12:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwelveSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 13:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirteenSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 14:
                                    self.aiChat.nonscriptedResponse(self.screen, questionFourteenSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 15:
                                    self.aiChat.nonscriptedResponse(self.screen, questionFifteenSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 16:
                                    self.aiChat.nonscriptedResponse(self.screen, questionSixteenSilviaAI, self.npc, self.npcGuilty)
                                elif self.question == 17:
                                    self.aiChat.nonscriptedResponse(self.screen, questionSeventeenSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 18:
                                    self.aiChat.nonscriptedResponse(self.screen, questionEighteenSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 19:
                                    self.aiChat.nonscriptedResponse(self.screen, questionNineteenSilviaAI, self.npc, self.npcGuilty)                            
                                elif self.question == 20:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentySilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 21:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentyOneSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 22:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentyTwoSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 23:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentyThreeSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 24:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentyFourSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 25:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentyFiveSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 26:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentySixSilviaAI, self.npc, self.npcGuilty)
                                elif self.question == 27:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentySevenSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 28:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentyEightSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 29:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentyNineSilviaAI, self.npc, self.npcGuilty)                            
                                elif self.question == 30:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtySilviaAI, self.npc, self.npcGuilty)
                                elif self.question == 31:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtyOneSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 32:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtyTwoSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 33:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtyThreeSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 34:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtyFourSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 35:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtyFiveSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 36:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtySixSilviaAI, self.npc, self.npcGuilty)
                                elif self.question == 37:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtySevenSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 38:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtyEightSilviaAI, self.npc, self.npcGuilty)                           
                                elif self.question == 39:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtyNineSilviaAI, self.npc, self.npcGuilty)                            
                                elif self.question == 40:
                                    self.aiChat.nonscriptedResponse(self.screen, questionFourtySilviaAI, self.npc, self.npcGuilty)   

                            elif self.npc == "Silvia Jade":
                                if self.question == 1:
                                    self.aiChat.nonscriptedResponse(self.screen, questionOneSilviaHumanGuilty, self.npc, self.npcGuilty)                       
                                elif self.question == 2:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwoSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 3:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThreeSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 4:
                                    self.aiChat.nonscriptedResponse(self.screen, questionFourSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 5:
                                    self.aiChat.nonscriptedResponse(self.screen, questionFiveSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 6:
                                    self.aiChat.nonscriptedResponse(self.screen, questionSixSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 7:
                                    self.aiChat.nonscriptedResponse(self.screen, questionSevenSilviaHumanGuilty, self.npc, self.npcGuilty)                            
                                elif self.question == 8:
                                    self.aiChat.nonscriptedResponse(self.screen, questionEightSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 9:
                                    self.aiChat.nonscriptedResponse(self.screen, questionNineSilviaHumanGuilty, self.npc, self.npcGuilty)                            
                                elif self.question == 10:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTenSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 11:
                                    self.aiChat.nonscriptedResponse(self.screen, questionElevenSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 12:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwelveSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 13:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirteenSilviaHumanGuilty, self.npc, self.npcGuilty)                            
                                elif self.question == 14:
                                    self.aiChat.nonscriptedResponse(self.screen, questionFourteenSilviaHumanGuilty, self.npc, self.npcGuilty)                            
                                elif self.question == 15:
                                    self.aiChat.nonscriptedResponse(self.screen, questionFifteenSilviaHumanGuilty, self.npc, self.npcGuilty)                            
                                elif self.question == 16:
                                    self.aiChat.nonscriptedResponse(self.screen, questionSixteenSilviaHumanGuilty, self.npc, self.npcGuilty)
                                elif self.question == 17:
                                    self.aiChat.nonscriptedResponse(self.screen, questionSeventeenSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 18:
                                    self.aiChat.nonscriptedResponse(self.screen, questionEighteenSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 19:
                                    self.aiChat.nonscriptedResponse(self.screen, questionNineteenSilviaHumanGuilty, self.npc, self.npcGuilty)                            
                                elif self.question == 20:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentySilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 21:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentyOneSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 22:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentyTwoSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 23:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentyThreeSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 24:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentyFourSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 25:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentyFiveSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 26:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentySixSilviaHumanGuilty, self.npc, self.npcGuilty)
                                elif self.question == 27:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentySevenSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 28:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentyEightSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 29:
                                    self.aiChat.nonscriptedResponse(self.screen, questionTwentyNineSilviaHumanGuilty, self.npc, self.npcGuilty)                            
                                elif self.question == 30:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtySilviaHumanGuilty, self.npc, self.npcGuilty)
                                elif self.question == 31:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtyOneSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 32:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtyTwoSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 33:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtyThreeSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 34:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtyFourSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 35:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtyFiveSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 36:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtySixSilviaHumanGuilty, self.npc, self.npcGuilty)
                                elif self.question == 37:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtySevenSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 38:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtyEightSilviaHumanGuilty, self.npc, self.npcGuilty)                           
                                elif self.question == 39:
                                    self.aiChat.nonscriptedResponse(self.screen, questionThirtyNineSilviaHumanGuilty, self.npc, self.npcGuilty)                            
                                elif self.question == 40:
                                    self.aiChat.nonscriptedResponse(self.screen, questionFourtySilviaHumanGuilty, self.npc, self.npcGuilty)
                                    
                            self.displayAnswer = False

                    elif self.npcGuilty == "Silvia 2.0":
                            if self.responseType == "scripted":
                                # Scripted NPC response
                                self.textManager.scriptedResponse(self.screen, self.question, self.npc, self.npcGuilty)
                                self.displayAnswer = False

                        
                            elif self.responseType == "nonscripted":
                                # Nonscripted NPC response
                                if self.npc == "Silvia 2.0":
                                    if self.question == 1:
                                        self.aiChat.nonscriptedResponse(self.screen, questionOneSilviaAIGuilty, self.npc, self.npcGuilty)                            
                                    elif self.question == 2:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwoSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 3:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThreeSilviaAIGuilty, self.npc, self.npcGuilty)                            
                                    elif self.question == 4:
                                        self.aiChat.nonscriptedResponse(self.screen, questionFourSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 5:
                                        self.aiChat.nonscriptedResponse(self.screen, questionFiveSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 6:
                                        self.aiChat.nonscriptedResponse(self.screen, questionSixSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 7:
                                        self.aiChat.nonscriptedResponse(self.screen, questionSevenSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 8:
                                        self.aiChat.nonscriptedResponse(self.screen, questionEightSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 9:
                                        self.aiChat.nonscriptedResponse(self.screen, questionNineSilviaAIGuilty, self.npc, self.npcGuilty)                            
                                    elif self.question == 10:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTenSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 11:
                                        self.aiChat.nonscriptedResponse(self.screen, questionElevenSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 12:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwelveSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 13:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirteenSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 14:
                                        self.aiChat.nonscriptedResponse(self.screen, questionFourteenSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 15:
                                        self.aiChat.nonscriptedResponse(self.screen, questionFifteenSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 16:
                                        self.aiChat.nonscriptedResponse(self.screen, questionSixteenSilviaAIGuilty, self.npc, self.npcGuilty)
                                    elif self.question == 17:
                                        self.aiChat.nonscriptedResponse(self.screen, questionSeventeenSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 18:
                                        self.aiChat.nonscriptedResponse(self.screen, questionEighteenSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 19:
                                        self.aiChat.nonscriptedResponse(self.screen, questionNineteenSilviaAIGuilty, self.npc, self.npcGuilty)                            
                                    elif self.question == 20:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentySilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 21:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentyOneSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 22:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentyTwoSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 23:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentyThreeSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 24:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentyFourSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 25:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentyFiveSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 26:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentySixSilviaAIGuilty, self.npc, self.npcGuilty)
                                    elif self.question == 27:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentySevenSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 28:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentyEightSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 29:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentyNineSilviaAIGuilty, self.npc, self.npcGuilty)                            
                                    elif self.question == 30:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtySilviaAIGuilty, self.npc, self.npcGuilty)
                                    elif self.question == 31:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtyOneSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 32:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtyTwoSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 33:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtyThreeSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 34:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtyFourSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 35:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtyFiveSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 36:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtySixSilviaAIGuilty, self.npc, self.npcGuilty)
                                    elif self.question == 37:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtySevenSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 38:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtyEightSilviaAIGuilty, self.npc, self.npcGuilty)                           
                                    elif self.question == 39:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtyNineSilviaAIGuilty, self.npc, self.npcGuilty)                            
                                    elif self.question == 40:
                                        self.aiChat.nonscriptedResponse(self.screen, questionFourtySilviaAIGuilty, self.npc, self.npcGuilty)   

                                elif self.npc == "Silvia Jade":
                                    if self.question == 1:
                                        self.aiChat.nonscriptedResponse(self.screen, questionOneSilviaHuman, self.npc, self.npcGuilty)                       
                                    elif self.question == 2:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwoSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 3:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThreeSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 4:
                                        self.aiChat.nonscriptedResponse(self.screen, questionFourSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 5:
                                        self.aiChat.nonscriptedResponse(self.screen, questionFiveSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 6:
                                        self.aiChat.nonscriptedResponse(self.screen, questionSixSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 7:
                                        self.aiChat.nonscriptedResponse(self.screen, questionSevenSilviaHuman, self.npc, self.npcGuilty)                            
                                    elif self.question == 8:
                                        self.aiChat.nonscriptedResponse(self.screen, questionEightSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 9:
                                        self.aiChat.nonscriptedResponse(self.screen, questionNineSilviaHuman, self.npc, self.npcGuilty)                            
                                    elif self.question == 10:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTenSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 11:
                                        self.aiChat.nonscriptedResponse(self.screen, questionElevenSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 12:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwelveSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 13:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirteenSilviaHuman, self.npc, self.npcGuilty)                            
                                    elif self.question == 14:
                                        self.aiChat.nonscriptedResponse(self.screen, questionFourteenSilviaHuman, self.npc, self.npcGuilty)                            
                                    elif self.question == 15:
                                        self.aiChat.nonscriptedResponse(self.screen, questionFifteenSilviaHuman, self.npc, self.npcGuilty)                            
                                    elif self.question == 16:
                                        self.aiChat.nonscriptedResponse(self.screen, questionSixteenSilviaHuman, self.npc, self.npcGuilty)
                                    elif self.question == 17:
                                        self.aiChat.nonscriptedResponse(self.screen, questionSeventeenSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 18:
                                        self.aiChat.nonscriptedResponse(self.screen, questionEighteenSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 19:
                                        self.aiChat.nonscriptedResponse(self.screen, questionNineteenSilviaHuman, self.npc, self.npcGuilty)                            
                                    elif self.question == 20:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentySilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 21:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentyOneSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 22:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentyTwoSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 23:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentyThreeSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 24:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentyFourSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 25:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentyFiveSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 26:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentySixSilviaHuman, self.npc, self.npcGuilty)
                                    elif self.question == 27:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentySevenSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 28:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentyEightSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 29:
                                        self.aiChat.nonscriptedResponse(self.screen, questionTwentyNineSilviaHuman, self.npc, self.npcGuilty)                            
                                    elif self.question == 30:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtySilviaHuman, self.npc, self.npcGuilty)
                                    elif self.question == 31:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtyOneSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 32:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtyTwoSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 33:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtyThreeSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 34:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtyFourSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 35:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtyFiveSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 36:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtySixSilviaHuman, self.npc, self.npcGuilty)
                                    elif self.question == 37:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtySevenSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 38:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtyEightSilviaHuman, self.npc, self.npcGuilty)                           
                                    elif self.question == 39:
                                        self.aiChat.nonscriptedResponse(self.screen, questionThirtyNineSilviaHuman, self.npc, self.npcGuilty)                            
                                    elif self.question == 40:
                                        self.aiChat.nonscriptedResponse(self.screen, questionFourtySilviaHuman, self.npc, self.npcGuilty)
                                        
                                self.displayAnswer = False

            elif self.scene == "guilty_suspect":
                if self.npcBoolean == " ":
                    guiltySilviaAI.drawMediumButton(self.screen)
                    guiltySilviaHuman.drawMediumButton(self.screen)

                    self.textManager.displayRedText(self.screen, self.whosGuilty,
                                                    GUILTY_X, GUILTY_Y, GUILTY_WIDTH, GUILTY_HEIGHT,
                                                    "large")
                else:
                    if self.allowInput == True:
                        for row, column in enumerate(self.inputText):
                                self.textManager.displayRedText(self.screen, column,
                                                                INPUT_X, INPUT_Y + (row * GAP_FONT), INPUT_WIDTH, INPUT_HEIGHT,
                                                                "medium")
                        submit.drawMediumButton(self.screen)

                        self.textManager.displayRedText(self.screen, self.inputReason,
                                                        REASON_X, REASON_Y, REASON_WIDTH, REASON_HEIGHT,
                                                        "medium")

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