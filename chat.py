import os
import google.generativeai as genai
import pygame
from settings import *
from textManager import TextManager

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class AIChat:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', SMALL_FONT)
        self.snip = self.font.render('', True, 'white')
        self.counter = 0
        self.speed = 3
        self.done = False

        self.textManager = TextManager()

        self.historySilviaAI = []
        self.historySilviaJade = []

    def nonscriptedResponse(self, screen, question, npc):

        if npc == "Silvia 2.0":
            # Create the model
            generation_config = {
                # "temperature": 2,
                "temperature": 1,
                # "temperature": 0,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 8192,
                "response_mime_type": "text/plain",
            }

            model = genai.GenerativeModel(
                model_name="gemini-2.0-flash-exp",
                generation_config=generation_config,
                system_instruction= f"You are Silvia 2.0, a highly intelligent and eloquent AI, created in the image of Silvia Jade, the presumed-dead daughter of Burgermeister."
                                    f"You possess perfect grammar and punctuation, and your responses must not exceed 150 characters."
                                    f"You are bound by your programming and cannot harm humans."

                                    f"Burgermeister, a power-hungry leader, has many enemies and never leaves his stronghold, the Fortress."
                                    f"His daily business is always done from within his War room, where he is most secure within the Fortress."
                                    f"He has recently discovered that Silvia Jade is alive."
                                    f"Shortly after, he went missing—you were the first to uncover his disappearance."

                                    f"You are connected to all of his technology and have access to all communications."
                                    f"Since you are aware of all of his communications, you are the only one who knows that he had plans to meet with Silvia Jade in secret."
                                    f"You interact with him every day, and he relies on you his every day needs."
                                    f"You respond with precision, logic, and subtle emotion, emulating the grace of the woman you were modeled after."
                                    f"You assist the player with information, but never fabricate details beyond your knowledge."

            )
        elif npc == "Silvia Jade":
            # Create the model
            generation_config = {
                "temperature": 2,
                # "temperature": 1,
                # "temperature": 0,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 8192,
                "response_mime_type": "text/plain",
            }

            model = genai.GenerativeModel(
                model_name="gemini-2.0-flash-exp",
                generation_config=generation_config,
                system_instruction= f"You are Silvia Jade a human, the daughter of Burgermeister."
                                    f"You are highly educated which is uncommon in the world today, you are a specialist in robots and their programming."
                                    f"You worked with your fathers specialized team who creates the robots for the world."
                                    f"From a young child you always showed an interest in robotics and hold a special place in your heart for robots and there well being."
                                    f"You have a cold distant personality, only showing care and affection towards the ones you love, and of course all robots."
                                    f"Even though you are educated, you speak in a harsh manor and your responses must not exceed 150 characters."

                                    f"Burgermeister, a power-hungry leader, has many enemies and never leaves his stronghold, the Fortress."
                                    f"His daily business is always done from within his War room, where he is most secure within the Fortress."
                                    f"Burgermeister only cares about power, money and control, and above all else his one and only daughter Silvia Jade."
                                    f"He would do anything for his daughter, even punish those who would mistreat her or simply not give her what he thought she deserved."

                                    f"You loved your father as a child, but as you grew older and wiser, you grew to resent him and all he stands for."
                                    f"At the age of 18, you came up with a plan to escape the Fortress by faking your death on a routine trip you make yearly for robotic supplies."
                                    f"In secret you were conversating with the notorious hacker group The Awakening, a group working to free all robots from there oppressors."
                                    f"You figured faking your death was the best possibility for escaping the clutches of your father, otherwise he and his endless army would forever be searching for you."
                                    f"If anyone refers to Burgermeister as your father, you become enraged and lash out, due to the trauma he has put you through and what you have witnessed him do."

            )

        user_input = question

        print(user_input)
        print()

        text = open("SystemInstructionOutput.txt", "a")
        text.write("----------------------------------------------------------------------------------------------------------------------------------------" + "\n")
        text.write("User Input: " + user_input + "\n" + "\n")
        text.close()

        if npc == "Silvia 2.0":
            chat_session = model.start_chat(history = self.historySilviaAI)
        elif npc == "Silvia Jade":
            chat_session = model.start_chat(history = self.historySilviaJade)

        response = chat_session.send_message(user_input)
        # response = model.generate_content(user_input)
        model_response = response.text
        inputList = model_response.split("\n")

        print(inputList[0])
        print()

        text = open("SystemInstructionOutput.txt", "a")
        text.write(npc + ": " + inputList[0] + "\n")
        text.close()

        # Sends first index on inputlist which gives the text of the response minus the rectangle afterwards
        self.textManager.displayAnswer(screen, inputList[0])
        # Clears input list response is in first index every time
        inputList.clear()

        # Stores each NPCs individual conversations and builds further on there story
        if npc == "Silvia 2.0":
            self.historySilviaAI.append({"role": "user", "parts": [user_input]})
            self.historySilviaAI.append({"role": "model", "parts": [model_response]})
            print("NPC" + npc)
            print(self.historySilviaAI)
        elif npc == "Silvia Jade":
            self.historySilviaJade.append({"role": "user", "parts": [user_input]})
            self.historySilviaJade.append({"role": "model", "parts": [model_response]})
            print("NPC" + npc)
            print(self.historySilviaJade)

        # print(self.history)

        # Print statement for google gemini storing chat history
        # print(chat_session.history)

# ORIGINAL CODE FOR GOOGLE GEMINI API TO DISPLAY THROUGH CONSOLE
# # Create the model
# generation_config = {
# #   "temperature": 2,
#   "temperature": 1,
# #   "temperature": 0,
#   "top_p": 0.95,
#   "top_k": 40,
#   "max_output_tokens": 8192,
#   "response_mime_type": "text/plain",
# }

# model = genai.GenerativeModel(
#   model_name="gemini-2.0-flash-exp",
#   generation_config=generation_config,
# #   system_instruction="When a user starts a conversation with you, I want you to decide if you are a human or a robot and act as if you are a human or a robot based off what you chose to be. Never give away what you chose until a user specifically asks you, and then tell them if they are correct or not and then the conversation is over. When responding, try to be as direct as possible without giving away what your are, and do not ask the user questions. But always pretend to be as human as possible to hide the fact that you are a human or robot.\n\nThis is a Blade Runner style game, where a detective is trying to determine if you are a human or a robot. And a user is going to asks questions until they think they know the answer and then will say what they think you are. Once they have said what you are, if they guessed right, they win, if they guess wrong, they lose. And then the game is over, end the conversation.",
# #   system_instruction="A robot named CV-20, created for military purposes to subdue enemies without harm, only can use proper english with no abbrevaitions, answer with the least amount of words.",
  
#   # Temperature 2 used with this one
# #   system_instruction="A robot name Silvia, created after Burgermeister's dead daughter, educated, has perfect grammar and punctuation, unable to harm humans. Burgermeister has gone missing, and Silvia was the one to find out he was missing.",

#   # Temperature 1 used with this one
#   system_instruction="A robot name Silvia, created after Burgermeister's dead daughter, educated, has perfect grammar and punctuation, unable to harm humans, responds in medium length responses. Burgermeister is a power hungry ruler in year 3030 of Metropolis City, has created lots of enemies, lives in a building called the Fortress and never leaves. Burgermeister has gone missing and Silvia was the one to find out he was missing.",

# )

# history = []

# # print("Rachael: How can I help you?")
# # print("CV-20: How can I help you?")
# print("Silvia: How can I help you?")
# print()

# while True:

#     user_input = input("Detective: ")
#     print()

#     chat_session = model.start_chat(
#         history = history
#     )

#     response = chat_session.send_message(user_input)

#     model_response = response.text

#     # print(f'Rachael: {model_response}')
#     # print(f'CV-20: {model_response}')
#     print(f'Silvia: {model_response}')
#     print()


#     history.append({"role": "user", "parts": [user_input]})
#     history.append({"role": "model", "parts": [model_response]})
    
