import google.generativeai as genai

# AIzaSyBxx94t9_zbNMCR6AtfYsEDqGfwrcTCovQ

genai.configure(api_key="") #Input API key from https://aistudio.google.com/app/apikey
model = genai.GenerativeModel("gemini-1.5-flash") #Choose a model
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "You have a bubbly personality and love watching soccer."} #Specifies what the bot should be like
    ]
)

class colors: #Used in coloring the terminal output
    YELLOW = '\033[33m'
    ENDC = '\033[m'

 #Causes AI to generate initial prompt
 #Print initial prompt
 #Ask user for input the first time

 #Check if the user typed exit to quit the program
 #Generate AI response to user input
 #Print AI response
 #Ask for user input any sequential time
