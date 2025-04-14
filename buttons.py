from settings import *
from questions import *
from buttonManager import Button

# # Main menu buttons
startGame = Button(START_GAME_X, START_GAME_Y, START_GAME_WIDTH, START_GAME_HEIGHT,
                                        "START GAME",
                                        'white', 'gray', action=None)

# Buttons for selecting an NPC to interrogate
aiSilvia = Button(BUTTON_AI_SILVIA_X, BUTTON_AI_SILVIA_Y, BUTTON_AI_SILVIA_WIDTH, BUTTON_AI_SILVIA_HEIGHT,
                                        "Silvia 2.0",
                                        'white', 'grey', action=None)
humanSilvia = Button(BUTTON_HUMAN_SILVIA_X, BUTTON_HUMAN_SILVIA_Y, BUTTON_HUMAN_SILVIA_WIDTH, BUTTON_HUMAN_SILVIA_HEIGHT,
                                        "Silvia Jade",
                                        'white', 'grey', action=None)

# Buttons for Silvia 2.0 interrogation questions
hideSecretQuestionSilviaAI = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        "",
                                        'white', 'gray', action=None)
questionOneButtonSilviaAI = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionOneSilviaAI,
                                        'white', 'grey', action=None)
questionTwoButtonSilviaAI = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionTwoSilviaAI,
                                        'white', 'grey', action=None)
questionThreeButtonSilviaAI = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionThreeSilviaAI,
                                        'white', 'grey', action=None)
questionFourButtonSilviaAI = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionFourSilviaAI,
                                        'white', 'grey', action=None)
questionFiveButtonSilviaAI = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionFiveSilviaAI,
                                        'white', 'grey', action=None)
questionSixButtonSilviaAI = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionSixSilviaAI,
                                        'white', 'grey', action=None)
questionSevenButtonSilviaAI = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionSevenSilviaAI,
                                        'white', 'grey', action=None)
questionEightButtonSilviaAI = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionEightSilviaAI,
                                        'white', 'grey', action=None)
questionNineButtonSilviaAI = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionNineSilviaAI,
                                        'white', 'grey', action=None)
questionTenButtonSilviaAI = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionTenSilviaAI,
                                        'white', 'grey', action=None)
questionElevenButtonSilviaAI = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionElevenSilviaAI,
                                        'white', 'grey', action=None)
questionTwelveButtonSilviaAI = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionTwelveSilviaAI,
                                        'white', 'grey', action=None)
questionThirteenButtonSilviaAI = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionThirteenSilviaAI,
                                        'white', 'grey', action=None)
questionFourteenButtonSilviaAI = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionFourteenSilviaAI,
                                        'white', 'grey', action=None)
questionFifteenButtonSilviaAI = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionFifteenSilviaAI,
                                        'white', 'grey', action=None)
questionSixteenButtonSilviaAI = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionSixteenSilviaAI,
                                        'white', 'grey', action=None)

# Buttons for Silvia Jade interrogation questions
hideSecretQuestionSilviaHuman = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        "",
                                        'white', 'gray', action=None)
questionOneButtonSilviaHuman = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionOneSilviaHuman,
                                        'white', 'grey', action=None)
questionTwoButtonSilviaHuman = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionTwoSilviaHuman,
                                        'white', 'grey', action=None)
questionThreeButtonSilviaHuman = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionThreeSilviaHuman,
                                        'white', 'grey', action=None)
questionFourButtonSilviaHuman = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionFourSilviaHuman,
                                        'white', 'grey', action=None)
questionFiveButtonSilviaHuman = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionFiveSilviaHuman,
                                        'white', 'grey', action=None)
questionSixButtonSilviaHuman = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionSixSilviaHuman,
                                        'white', 'grey', action=None)
questionSevenButtonSilviaHuman = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionSevenSilviaHuman,
                                        'white', 'grey', action=None)
questionEightButtonSilviaHuman = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionEightSilviaHuman,
                                        'white', 'grey', action=None)
questionNineButtonSilviaHuman = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionNineSilviaHuman,
                                        'white', 'grey', action=None)
questionTenButtonSilviaHuman = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionTenSilviaHuman,
                                        'white', 'grey', action=None)
questionElevenButtonSilviaHuman = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionElevenSilviaHuman,
                                        'white', 'grey', action=None)
questionTwelveButtonSilviaHuman = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionTwelveSilviaHuman,
                                        'white', 'grey', action=None)
questionThirteenButtonSilviaHuman = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionThirteenSilviaHuman,
                                        'white', 'grey', action=None)
questionFourteenButtonSilviaHuman = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionFourteenSilviaHuman,
                                        'white', 'grey', action=None)
questionFifteenButtonSilviaHuman = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionFifteenSilviaHuman,
                                        'white', 'grey', action=None)
questionSixteenButtonSilviaHuman = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionSixteenSilviaHuman,
                                        'white', 'grey', action=None)