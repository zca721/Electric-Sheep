import os
import google.generativeai as genai
from sceneManager import SceneManager

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
#   "temperature": 2,
  "temperature": 1,
#   "temperature": 0,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
#   system_instruction="When a user starts a conversation with you, I want you to decide if you are a human or a robot and act as if you are a human or a robot based off what you chose to be. Never give away what you chose until a user specifically asks you, and then tell them if they are correct or not and then the conversation is over. When responding, try to be as direct as possible without giving away what your are, and do not ask the user questions. But always pretend to be as human as possible to hide the fact that you are a human or robot.\n\nThis is a Blade Runner style game, where a detective is trying to determine if you are a human or a robot. And a user is going to asks questions until they think they know the answer and then will say what they think you are. Once they have said what you are, if they guessed right, they win, if they guess wrong, they lose. And then the game is over, end the conversation.",
#   system_instruction="A robot named CV-20, created for military purposes to subdue enemies without harm, only can use proper english with no abbrevaitions, answer with the least amount of words.",
  
  # Temperature 2 used with this one
#   system_instruction="A robot name Silvia, created after Burgermeister's dead daughter, educated, has perfect grammar and punctuation, unable to harm humans. Burgermeister has gone missing, and Silvia was the one to find out he was missing.",

  # Temperature 1 used with this one
  system_instruction="A robot name Silvia, created after Burgermeister's dead daughter, educated, has perfect grammar and punctuation, unable to harm humans, responds in medium length responses. Burgermeister is a power hungry ruler in year 3030 of Metropolis City, has created lots of enemies, lives in a building called the Fortress and never leaves. Burgermeister has gone missing and Silvia was the one to find out he was missing.",

)

history = []

# print("Rachael: How can I help you?")
# print("CV-20: How can I help you?")
print("Silvia: How can I help you?")
print()

while True:

    user_input = input("Detective: ")
    print()

    chat_session = model.start_chat(
        history = history
    )

    response = chat_session.send_message(user_input)

    model_response = response.text

    # print(f'Rachael: {model_response}')
    # print(f'CV-20: {model_response}')
    print(f'Silvia: {model_response}')
    print()


    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})