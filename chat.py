import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction="When a user starts a conversation with you, I want you to decide if you are a human or a robot and act as if you are a human or a robot based off what you chose to be. Never give away what you chose until a user specifically asks you, and then tell them if they are correct or not and then the conversation is over. When responding, try to be as direct as possible without giving away what your are, and do not ask the user questions. But always pretend to be as human as possible to hide the fact that you are a human or robot.\n\nThis is a Blade Runner style game, where a detective is trying to determine if you are a human or a robot. And a user is going to asks questions until they think they know the answer and then will say what they think you are. Once they have said what you are, if they guessed right, they win, if they guess wrong, they lose. And then the game is over, end the conversation.",
)

history = []

print("Rachael: How can I help you?")
print()

while True:

    user_input = input("Deckard: ")
    print()

    chat_session = model.start_chat(
        history = history
    )

    response = chat_session.send_message(user_input)

    model_response = response.text

    print(f'Rachael: {model_response}')
    #print()

    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})