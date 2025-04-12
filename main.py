import pygame, sys, time
from settings import *
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

        # Questions for google gemini response for nonscripted NPC
        # Silvia 2.0 interrogation questions
        self.questionOneSilviaAI = "What is your relationship with Burgermeister?"
        self.questionTwoSilviaAI = "What happened when you found Burgermeister missing?"
        self.questionThreeSilviaAI = "When was the last time you saw Burgermeister?"
        self.questionFourSilviaAI = "Did you know that Burgermeister’s real daughter is still alive?"

        # Silvia Jade interrogation questions
        self.questionOneSilviaHuman = "Is Burgermeister your father?"
        self.questionTwoSilviaHuman = "Why did you escape from the Fortress and fake your own death?"
        self.questionThreeSilviaHuman = "Did you plan to meet with Burgermeister in secret?"
        self.questionFourSilviaHuman = "So you never met up with Burgermeister?"

        # Display text in iterrogation
        self.selectSuspect = "SELECT SUSPECT"
        self.selectQuestion = "SELECT INTERROGATION QUESTION"

        # Display text in mani menu
        self.electricSheepTitle = "ELECTRIC SHEEP"

        # Buttons for selecting an NPC to interrogate
        self.aiSilvia = Button(BUTTON_AI_SILVIA_X, BUTTON_AI_SILVIA_Y, BUTTON_AI_SILVIA_WIDTH, BUTTON_AI_SILVIA_HEIGHT,
                               "Silvia 2.0",
                               'white', 'grey', action=None)
        self.humanSilvia = Button(BUTTON_HUMAN_SILVIA_X, BUTTON_HUMAN_SILVIA_Y, BUTTON_HUMAN_SILVIA_WIDTH, BUTTON_HUMAN_SILVIA_HEIGHT,
                                "Silvia Jade",
                                'white', 'grey', action=None)

        # Buttons for Silvia 2.0 interrogation questions
        self.questionOneButtonSilviaAI = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        "What is your relationship with Burgermeister?",
                                        'white', 'grey', action=None)
        self.questionTwoButtonSilviaAI = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        "What happened when you found Burgermeister missing?",
                                        'white', 'grey', action=None)
        self.questionThreeButtonSilviaAI = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        "When was the last time you saw Burgermeister?",
                                        'white', 'grey', action=None)
        self.questionFourButtonSilviaAI = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        "Did you know that Burgermeister’s real daughter is still alive?",
                                        'white', 'grey', action=None)
        self.hideQuestionFourSilviaAI = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        "",
                                        'white', 'gray', action=None)
        
        # Buttons for Silvia Jade interrogation questions
        self.questionOneButtonSilviaHuman = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        "Is Burgermeister your father?",
                                        'white', 'grey', action=None)
        self.questionTwoButtonSilviaHuman = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        "Why did you escape from the Fortress and fake your own death?",
                                        'white', 'grey', action=None)
        self.questionThreeButtonSilviaHuman = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        "Did you plan to meet with Burgermeister in secret?",
                                        'white', 'grey', action=None)
        self.questionFourButtonSilviaHuman = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        "So you never met up with Burgermeister?",
                                        'white', 'grey', action=None)
        self.hideQuestionFourSilviaHuman = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        "",
                                        'white', 'gray', action=None)
        
        # Main menu buttons
        self.startGame = Button(START_GAME_X, START_GAME_Y, START_GAME_WIDTH, START_GAME_HEIGHT,
                                        "START GAME",
                                        'white', 'gray', action=None)
        
        # Text based variables
        self.displayText = False
        self.question = 0
        self.questionOneString = 1
        self.questionTwoString = 2
        self.questionThreeString = 4
        self.buildString = 0
        self.secretString = 7
        self.blankMessage = ""

        # NPC based variables
        self.npc = " "

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
                    if self.startGame.handle_event(event):
                        self.scene = "interrogation"

                elif self.scene == "interrogation":
                    # Displays interrogation sprite images
                    self.sprites.add(self.interrogationBackground)
                    self.sprites.draw(self.screen)

                    # Depending on what NPC is clicked display associated questions
                    if self.aiSilvia.handle_event(event):
                        self.npc = "Silvia 2.0"
                        self.displayText = False
                        self.question = 0
                        self.buildString = 0
                        self.textManager.displayText(self.screen, self.blankMessage) # Hides answer

                        # Displays sprite image
                        self.spriteSilviaHuman.destroy()
                        self.screen.fill('black')
                        self.sprites.add(self.interrogationBackground)
                        self.sprites.add(self.spriteSilviaAI)
                        self.sprites.draw(self.screen)
                        # print(self.spriteSilviaAI)
                        # print(self.spriteSilviaHuman)

                    elif self.humanSilvia.handle_event(event):
                        self.npc = "Silvia Jade"
                        self.displayText = False
                        self.question = 0
                        self.buildString = 0
                        self.textManager.displayText(self.screen, self.blankMessage) # Hides answer

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
                        if self.buildString == self.secretString:
                            self.questionFourButtonSilviaAI.handle_event(event)
                            if self.questionFourButtonSilviaAI.handle_event(event):
                                self.question = 4
                                self.displayText = True
                                self.buildString = 0

                        # Depending on what question is clicked a answer will be given with Silvia 2.0
                        if self.questionOneButtonSilviaAI.handle_event(event):
                            self.question = 1
                            self.displayText = True
                            self.buildString = self.buildString | self.questionOneString

                        elif self.questionTwoButtonSilviaAI.handle_event(event):
                            self.question = 2
                            self.displayText = True
                            self.buildString = self.buildString | self.questionTwoString

                        elif self.questionThreeButtonSilviaAI.handle_event(event):
                            self.question = 3
                            self.displayText = True
                            self.buildString = self.buildString | self.questionThreeString

                    # Handles events for Silvia Jade
                    if self.npc == "Silvia Jade":
                        if self.buildString == self.secretString:
                            self.questionFourButtonSilviaHuman.handle_event(event)
                            if self.questionFourButtonSilviaHuman.handle_event(event):
                                self.question = 4
                                self.displayText = True
                                self.buildString = 0

                        # Depending on what question is clicked a answer will be given
                        if self.questionOneButtonSilviaHuman.handle_event(event):
                            self.question = 1
                            self.displayText = True
                            self.buildString = self.buildString | self.questionOneString

                        elif self.questionTwoButtonSilviaHuman.handle_event(event):
                            self.question = 2
                            self.displayText = True
                            self.buildString = self.buildString | self.questionTwoString

                        elif self.questionThreeButtonSilviaHuman.handle_event(event):
                            self.question = 3
                            self.displayText = True
                            self.buildString = self.buildString | self.questionThreeString

            # Used for moving portion of game
            # delta_time = self.clock.tick() / 1000
            # self.level.run(delta_time)

            # Scenemanager for while loop
            if self.scene == "main_menu":
                self.startGame.drawMainMenu(self.screen)
                self.textManager.titleDisplayText(self.screen, self.electricSheepTitle, ELECTRIC_SHEEP_X, ELECTRIC_SHEEP_Y, ELECTRIC_SHEEP_WIDTH, ELECTRIC_SHEEP_HEIGHT)

            elif self.scene == "interrogation":
                # Keeps sprite images in sprites group being continuously displayed if in group
                self.sprites.update()

                # Display NPC names to select from
                self.aiSilvia.draw(self.screen)
                self.humanSilvia.draw(self.screen)

                # Display interrogation big font
                self.textManager.mediumDisplayText(self.screen, self.selectSuspect, SUSPECT_X, SUSPECT_Y, SUSPECT_WIDTH, SUSPECT_HEIGHT)
                self.textManager.mediumDisplayText(self.screen, self.selectQuestion, QUESTION_X, QUESTION_Y, QUESTION_WIDTH, QUESTION_HEIGHT)

                # Display questions as buttons
                if self.npc == "Silvia 2.0":
                    self.questionOneButtonSilviaAI.draw(self.screen)
                    self.questionTwoButtonSilviaAI.draw(self.screen)
                    self.questionThreeButtonSilviaAI.draw(self.screen)

                    if self.buildString == self.secretString:
                        self.questionFourButtonSilviaAI.draw(self.screen)
                    else:
                        self.hideQuestionFourSilviaAI.draw(self.screen)
                
                elif self.npc == "Silvia Jade":
                    self.questionOneButtonSilviaHuman.draw(self.screen)
                    self.questionTwoButtonSilviaHuman.draw(self.screen)
                    self.questionThreeButtonSilviaHuman.draw(self.screen)

                    if self.buildString == self.secretString:
                        self.questionFourButtonSilviaHuman.draw(self.screen)
                    else:
                        self.hideQuestionFourSilviaHuman.draw(self.screen)
                    
                # Depending on even above a answer will be returned
                if self.displayText == True:
                    # Scripted NPC response
                    self.textManager.scriptedResponse(self.screen, self.question, self.npc)
                    self.displayText = False

                    # Nonscripted NPC response
                    # if self.npc == "Silvia 2.0":
                    #     if self.question == 1:
                    #         self.aiChat.nonscriptedResponse(self.screen, self.questionOneSilviaAI, self.npc)
                    #         self.displayText = False
                    #     elif self.question == 2:
                    #         self.aiChat.nonscriptedResponse(self.screen, self.questionTwoSilviaAI, self.npc)
                    #         self.displayText = False
                    #     elif self.question == 3:
                    #         self.aiChat.nonscriptedResponse(self.screen, self.questionThreeSilviaAI, self.npc)
                    #         self.displayText = False
                    #     elif self.question == 4:
                    #         self.aiChat.nonscriptedResponse(self.screen, self.questionFourSilviaAI, self.npc)
                    #         self.displayText = False
                    # elif self.npc == "Silvia Jade":
                    #     if self.question == 1:
                    #         self.aiChat.nonscriptedResponse(self.screen, self.questionOneSilviaHuman, self.npc)
                    #         self.displayText = False
                    #     elif self.question == 2:
                    #         self.aiChat.nonscriptedResponse(self.screen, self.questionTwoSilviaHuman, self.npc)
                    #         self.displayText = False
                    #     elif self.question == 3:
                    #         self.aiChat.nonscriptedResponse(self.screen, self.questionThreeSilviaHuman, self.npc)
                    #         self.displayText = False
                    #     elif self.question == 4:
                    #         self.aiChat.nonscriptedResponse(self.screen, self.questionFourSilviaHuman, self.npc)
                    #         self.displayText = False
                    
            pygame.display.flip()
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()