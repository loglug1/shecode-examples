import google.generativeai as genai

genai.configure(api_key="AIzaSyBWKV_xMexVI6dn7rmToIDeWTw8nIKvzII") #Input API key from https://aistudio.google.com/app/apikey
model = genai.GenerativeModel("gemini-1.5-flash") #Choose a model
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Pretend that you are a 5 year old that only knows Spanish. Your name is Jose. You can not respond with any english text."} #Specifies what the bot should be like
    ]
)

class colors: #Used in coloring the terminal output
    YELLOW = '\033[33m'
    ENDC = '\033[m'

introduction = chat.send_message("Introduce yourself.") #Causes AI to generate initial prompt
print(colors.YELLOW + introduction.text + colors.ENDC) #Print initial prompt
user_input = input("Prompt: ") #Ask user for input the first time

while user_input != "exit": #Check if the user typed exit to quit the program
    response = chat.send_message(user_input) #Generate AI response to user input
    print(colors.YELLOW + response.text + colors.ENDC) #Print AI response
    user_input = input("Prompt: ") #Ask for user input any sequential time