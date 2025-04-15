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
questionSeventeenButtonSilviaAI = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionSeventeenSilviaAI,
                                        'white', 'grey', action=None)
questionEighteenButtonSilviaAI = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionEighteenSilviaAI,
                                        'white', 'grey', action=None)
questionNineteenButtonSilviaAI = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionNineteenSilviaAI,
                                        'white', 'grey', action=None)
questionTwentyButtonSilviaAI = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionTwentySilviaAI,
                                        'white', 'grey', action=None)
questionTwentyOneButtonSilviaAI = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionTwentyOneSilviaAI,
                                        'white', 'grey', action=None)
questionTwentyTwoButtonSilviaAI = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionTwentyTwoSilviaAI,
                                        'white', 'grey', action=None)
questionTwentyThreeButtonSilviaAI = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionTwentyThreeSilviaAI,
                                        'white', 'grey', action=None)
questionTwentyFourButtonSilviaAI = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionTwentyFourSilviaAI,
                                        'white', 'grey', action=None)
questionTwentyFiveButtonSilviaAI = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionTwentyFiveSilviaAI,
                                        'white', 'grey', action=None)
questionTwentySixButtonSilviaAI = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionTwentySixSilviaAI,
                                        'white', 'grey', action=None)
questionTwentySevenButtonSilviaAI = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionTwentySevenSilviaAI,
                                        'white', 'grey', action=None)
questionTwentyEightButtonSilviaAI = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionTwentyEightSilviaAI,
                                        'white', 'grey', action=None)
questionTwentyNineButtonSilviaAI = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionTwentyNineSilviaAI,
                                        'white', 'grey', action=None)
questionThirtyButtonSilviaAI = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionThirtySilviaAI,
                                        'white', 'grey', action=None)
questionThirtyOneButtonSilviaAI = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionThirtyOneSilviaAI,
                                        'white', 'grey', action=None)
questionThirtyTwoButtonSilviaAI = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionThirtyTwoSilviaAI,
                                        'white', 'grey', action=None)
questionThirtyThreeButtonSilviaAI = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionThirtyThreeSilviaAI,
                                        'white', 'grey', action=None)
questionThirtyFourButtonSilviaAI = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionThirtyFourSilviaAI,
                                        'white', 'grey', action=None)
questionThirtyFiveButtonSilviaAI = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionThirtyFiveSilviaAI,
                                        'white', 'grey', action=None)
questionThirtySixButtonSilviaAI = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionThirtySixSilviaAI,
                                        'white', 'grey', action=None)
questionThirtySevenButtonSilviaAI = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionThirtySevenSilviaAI,
                                        'white', 'grey', action=None)
questionThirtyEightButtonSilviaAI = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionThirtyEightSilviaAI,
                                        'white', 'grey', action=None)
questionThirtyNineButtonSilviaAI = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionThirtyNineSilviaAI,
                                        'white', 'grey', action=None)
questionFourtyButtonSilviaAI = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionFourtySilviaAI,
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
questionSeventeenButtonSilviaHuman = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionSeventeenSilviaHuman,
                                        'white', 'grey', action=None)
questionEighteenButtonSilviaHuman = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionEighteenSilviaHuman,
                                        'white', 'grey', action=None)
questionNineteenButtonSilviaHuman = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionNineteenSilviaHuman,
                                        'white', 'grey', action=None)
questionTwentyButtonSilviaHuman = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionTwentySilviaHuman,
                                        'white', 'grey', action=None)
questionTwentyOneButtonSilviaHuman = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionTwentyOneSilviaHuman,
                                        'white', 'grey', action=None)
questionTwentyTwoButtonSilviaHuman = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionTwentyTwoSilviaHuman,
                                        'white', 'grey', action=None)
questionTwentyThreeButtonSilviaHuman = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionTwentyThreeSilviaHuman,
                                        'white', 'grey', action=None)
questionTwentyFourButtonSilviaHuman = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionTwentyFourSilviaHuman,
                                        'white', 'grey', action=None)
questionTwentyFiveButtonSilviaHuman = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionTwentyFiveSilviaHuman,
                                        'white', 'grey', action=None)
questionTwentySixButtonSilviaHuman = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionTwentySixSilviaHuman,
                                        'white', 'grey', action=None)
questionTwentySevenButtonSilviaHuman = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionTwentySevenSilviaHuman,
                                        'white', 'grey', action=None)
questionTwentyEightButtonSilviaHuman = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionTwentyEightSilviaHuman,
                                        'white', 'grey', action=None)
questionTwentyNineButtonSilviaHuman = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionTwentyNineSilviaHuman,
                                        'white', 'grey', action=None)
questionThirtyButtonSilviaHuman = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionThirtySilviaHuman,
                                        'white', 'grey', action=None)
questionThirtyOneButtonSilviaHuman = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionThirtyOneSilviaHuman,
                                        'white', 'grey', action=None)
questionThirtyTwoButtonSilviaHuman = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionThirtyTwoSilviaHuman,
                                        'white', 'grey', action=None)
questionThirtyThreeButtonSilviaHuman = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionThirtyThreeSilviaHuman,
                                        'white', 'grey', action=None)
questionThirtyFourButtonSilviaHuman = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionThirtyFourSilviaHuman,
                                        'white', 'grey', action=None)
questionThirtyFiveButtonSilviaHuman = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionThirtyFiveSilviaHuman,
                                        'white', 'grey', action=None)
questionThirtySixButtonSilviaHuman = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionThirtySixSilviaHuman,
                                        'white', 'grey', action=None)
questionThirtySevenButtonSilviaHuman = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionThirtySevenSilviaHuman,
                                        'white', 'grey', action=None)
questionThirtyEightButtonSilviaHuman = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionThirtyEightSilviaHuman,
                                        'white', 'grey', action=None)
questionThirtyNineButtonSilviaHuman = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionThirtyNineSilviaHuman,
                                        'white', 'grey', action=None)
questionFourtyButtonSilviaHuman = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionFourtySilviaHuman,
                                        'white', 'grey', action=None)