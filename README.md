# Electric-Sheep
 
INSTRUCTIONS ON HOW TO DOWNLOAD AND MAKE PLAYABLE ON LOCAL MACHINE:

Download Visual Studio Code
https://code.visualstudio.com/download

Download Python
https://www.python.org/downloads/

Video on how to download and install Python on Windows
https://www.youtube.com/watch?v=fjzwqEoFTww&t=24s

Once Visual Studio Code and Python is installed
Open Visual Studio Code and click extensions on the left hand side
-Find Python extension and download

Install pygame
-In terminal type
	pip install pygame

Video on how to install pygame
https://www.youtube.com/watch?v=ZqSV0x4nIjk&t=222s

Install the Google AI Python SDK
-In terminal type
	pip install google-generativeai
	
In Visual Studio Code
-create a file named .env
-Input GEMINI_API_KEY = (google gemini api key goes here in a string)
-In terminal type
	pip install python-dotenv
	
Video on how download and use Google Gemini API
https://www.youtube.com/watch?v=CaxPa1FuHx4&list=PLvMpiyxnnwmoejD_EXadNUbVQAl8EatVY&index=19

Should be able to play game on you rlocal machine at this point.

To change from scripted and non-scripted responses:
In main.py
self.responseType = "nonscripted"
self.responseType = "scripted"
-Comment out which ever one you don't want to use and leave the one you would like to use active

To change from Silvia 2.0 guilty or Silvia Jade guilty:
In main.py
self.npcGuilty = "Silvia Jade"
self.npcGuilty = "Silvia 2.0"
-Comment out which ever one you don't want to use and leave the one you would like to use active
