from settings import *
from questions import *
from buttonManager import Button

# Main menu buttons
startGame = Button(START_GAME_X, START_GAME_Y, START_GAME_WIDTH, START_GAME_HEIGHT,
                                        "START GAME",
                                        'white', 'gray', action=None)

# Game description buttons
continueGame = Button(CONTINUE_GAME_X, CONTINUE_GAME_Y, CONTINUE_GAME_WIDTH, CONTINUE_GAME_HEIGHT,
                                        "CONTINUE",
                                        'white', 'gray', action=None)

# Interrogation buttons
guessGuiltySuspect = Button(NEXT_X, NEXT_Y, NEXT_WIDTH, NEXT_HEIGHT,
                                        "guess guilty suspect",
                                        'white', 'grey', action=None)

# Guilty select buttons
submit = Button(SUBMIT_X, SUBMIT_Y, SUBMIT_WIDTH, SUBMIT_HEIGHT,
                                        "SUBMIT",
                                        'white', 'grey', action=None)

# Buttons for selecting an NPC to interrogate
aiSilvia = Button(BUTTON_AI_SILVIA_X, BUTTON_AI_SILVIA_Y, BUTTON_AI_SILVIA_WIDTH, BUTTON_AI_SILVIA_HEIGHT,
                                        "Silvia 2.0",
                                        'white', 'grey', action=None)
humanSilvia = Button(BUTTON_HUMAN_SILVIA_X, BUTTON_HUMAN_SILVIA_Y, BUTTON_HUMAN_SILVIA_WIDTH, BUTTON_HUMAN_SILVIA_HEIGHT,
                                        "Silvia Jade",
                                        'white', 'grey', action=None)

# Buttons for selecting wich NPC is guilty
guiltySilviaAI = Button(GUILTY_AI_SILVIA_X, GUILTY_AI_SILVIA_Y, GUILTY_AI_SILVIA_WIDTH, GUILTY_AI_SILVIA_HEIGHT,
                                        "Silvia 2.0",
                                        'white', 'grey', action=None)
guiltySilviaHuman = Button(GUILTY_HUMAN_SILVIA_X, GUILTY_HUMAN_SILVIA_Y, GUILTY_HUMAN_SILVIA_WIDTH, GUILTY_HUMAN_SILVIA_HEIGHT,
                                        "Silvia Jade",
                                        'white', 'grey', action=None)

# Buttons for Silvia 2.0 interrogation questions
# Silvia 2.0 not guilty
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

# Silvia 2.0 guilty
hideSecretQuestionSilviaAI = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        "",
                                        'white', 'gray', action=None)
questionOneButtonSilviaAIGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionOneSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionTwoButtonSilviaAIGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionTwoSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionThreeButtonSilviaAIGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionThreeSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionFourButtonSilviaAIGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionFourSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionFiveButtonSilviaAIGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionFiveSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionSixButtonSilviaAIGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionSixSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionSevenButtonSilviaAIGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionSevenSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionEightButtonSilviaAIGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionEightSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionNineButtonSilviaAIGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionNineSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionTenButtonSilviaAIGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionTenSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionElevenButtonSilviaAIGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionElevenSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionTwelveButtonSilviaAIGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionTwelveSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionThirteenButtonSilviaAIGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionThirteenSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionFourteenButtonSilviaAIGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionFourteenSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionFifteenButtonSilviaAIGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionFifteenSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionSixteenButtonSilviaAIGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionSixteenSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionSeventeenButtonSilviaAIGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionSeventeenSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionEighteenButtonSilviaAIGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionEighteenSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionNineteenButtonSilviaAIGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionNineteenSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionTwentyButtonSilviaAIGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionTwentySilviaAIGuilty,
                                        'white', 'grey', action=None)
questionTwentyOneButtonSilviaAIGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionTwentyOneSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionTwentyTwoButtonSilviaAIGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionTwentyTwoSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionTwentyThreeButtonSilviaAIGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionTwentyThreeSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionTwentyFourButtonSilviaAIGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionTwentyFourSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionTwentyFiveButtonSilviaAIGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionTwentyFiveSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionTwentySixButtonSilviaAIGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionTwentySixSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionTwentySevenButtonSilviaAIGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionTwentySevenSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionTwentyEightButtonSilviaAIGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionTwentyEightSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionTwentyNineButtonSilviaAIGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionTwentyNineSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionThirtyButtonSilviaAIGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionThirtySilviaAIGuilty,
                                        'white', 'grey', action=None)
questionThirtyOneButtonSilviaAIGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionThirtyOneSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionThirtyTwoButtonSilviaAIGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionThirtyTwoSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionThirtyThreeButtonSilviaAIGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionThirtyThreeSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionThirtyFourButtonSilviaAIGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionThirtyFourSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionThirtyFiveButtonSilviaAIGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionThirtyFiveSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionThirtySixButtonSilviaAIGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionThirtySixSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionThirtySevenButtonSilviaAIGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionThirtySevenSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionThirtyEightButtonSilviaAIGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionThirtyEightSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionThirtyNineButtonSilviaAIGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionThirtyNineSilviaAIGuilty,
                                        'white', 'grey', action=None)
questionFourtyButtonSilviaAIGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionFourtySilviaAIGuilty,
                                        'white', 'grey', action=None)


# Buttons for Silvia Jade interrogation questions
# Silvia Jade guilty
hideSecretQuestionSilviaHuman = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        "",
                                        'white', 'gray', action=None)
questionOneButtonSilviaHumanGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionOneSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionTwoButtonSilviaHumanGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionTwoSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionThreeButtonSilviaHumanGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionThreeSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionFourButtonSilviaHumanGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionFourSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionFiveButtonSilviaHumanGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionFiveSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionSixButtonSilviaHumanGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionSixSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionSevenButtonSilviaHumanGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionSevenSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionEightButtonSilviaHumanGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionEightSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionNineButtonSilviaHumanGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionNineSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionTenButtonSilviaHumanGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionTenSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionElevenButtonSilviaHumanGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionElevenSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionTwelveButtonSilviaHumanGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionTwelveSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionThirteenButtonSilviaHumanGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionThirteenSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionFourteenButtonSilviaHumanGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionFourteenSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionFifteenButtonSilviaHumanGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionFifteenSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionSixteenButtonSilviaHumanGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionSixteenSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionSeventeenButtonSilviaHumanGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionSeventeenSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionEighteenButtonSilviaHumanGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionEighteenSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionNineteenButtonSilviaHumanGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionNineteenSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionTwentyButtonSilviaHumanGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionTwentySilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionTwentyOneButtonSilviaHumanGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionTwentyOneSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionTwentyTwoButtonSilviaHumanGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionTwentyTwoSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionTwentyThreeButtonSilviaHumanGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionTwentyThreeSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionTwentyFourButtonSilviaHumanGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionTwentyFourSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionTwentyFiveButtonSilviaHumanGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionTwentyFiveSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionTwentySixButtonSilviaHumanGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionTwentySixSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionTwentySevenButtonSilviaHumanGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionTwentySevenSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionTwentyEightButtonSilviaHumanGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionTwentyEightSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionTwentyNineButtonSilviaHumanGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionTwentyNineSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionThirtyButtonSilviaHumanGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionThirtySilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionThirtyOneButtonSilviaHumanGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionThirtyOneSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionThirtyTwoButtonSilviaHumanGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionThirtyTwoSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionThirtyThreeButtonSilviaHumanGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionThirtyThreeSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionThirtyFourButtonSilviaHumanGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionThirtyFourSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionThirtyFiveButtonSilviaHumanGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionThirtyFiveSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionThirtySixButtonSilviaHumanGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionThirtySixSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionThirtySevenButtonSilviaHumanGuilty = Button(BUTTON_ONE_X, BUTTON_ONE_Y, BUTTON_ONE_WIDTH, BUTTON_ONE_HEIGHT,
                                        questionThirtySevenSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionThirtyEightButtonSilviaHumanGuilty = Button(BUTTON_TWO_X, BUTTON_TWO_Y, BUTTON_TWO_WIDTH, BUTTON_TWO_HEIGHT,
                                        questionThirtyEightSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionThirtyNineButtonSilviaHumanGuilty = Button(BUTTON_THREE_X, BUTTON_THREE_Y, BUTTON_THREE_WIDTH, BUTTON_THREE_HEIGHT,
                                        questionThirtyNineSilviaHumanGuilty,
                                        'white', 'grey', action=None)
questionFourtyButtonSilviaHumanGuilty = Button(BUTTON_FOUR_X, BUTTON_FOUR_Y, BUTTON_FOUR_WIDTH, BUTTON_FOUR_HEIGHT,
                                        questionFourtySilviaHumanGuilty,
                                        'white', 'grey', action=None)

# Silvia Jade not guilty
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