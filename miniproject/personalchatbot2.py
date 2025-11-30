import datetime
import time
import sys
import random

# Typing Effect Function
def bot_says(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(0.02)
    print()

# ---------------------------------------
# GREETING BASED ON TIME
# ---------------------------------------
name = input("Welcome, enter your name: ")

presentHour = datetime.datetime.now().hour

if 5 <= presentHour < 12:
    bot_says("Good Morning, " + name + " ☀️")
elif 12 <= presentHour < 17:
    bot_says("Good Afternoon, " + name + " 😊")
elif 17 <= presentHour < 20:
    bot_says("Good Evening, " + name + " 🌆")
else:
    bot_says("Hello, " + name + " 🌙")

bot_says("Namaste! Welcome to your ChatBot 🙏")
bot_says("You can ask me anything. Type 'bye' to exit.\n")

# ---------------------------------------
# MAIN RESPONSE BANK
# ---------------------------------------
responses = {
    "hello": ["Hi 😊", "Hello 👋", "Hey there ✨", "Namaste 🙏"],
    "hi": ["Hi 😊", "Hello 👋", "Hey there ✨"],
    "name": ["I'm your chatbot 🤖", "People call me MiniGPT 😎"],
    "creator": ["I was created by Anjali ❤️", "Anjali is my creator 😎"],
    "joke": [
        "Why don't programmers like nature? Too many bugs! 🐞",
        "Why did the computer catch a cold? It left its Windows open! 💨",
        "Debugging: Removing needles from a haystack. 🧵"
    ],
    "motivate": [
        "Believe in yourself! You are unstoppable 💪",
        "Every day is a chance to improve 🌟",
        "Hard work always pays off. Keep going 🚀"
    ],
    "love": [
        "Love is beautiful ❤️",
        "Self-love is the best kind of love 💖",
        "Spread love everywhere you go 😊"
    ]
}

# ---------------------------------------
# SMART RESPONSE FUNCTION
# ---------------------------------------
def get_response(userquestion):

    userquestion = userquestion.lower()

    # TIME
    if "time" in userquestion:
        return "⏰ The time is " + datetime.datetime.now().strftime("%H:%M:%S")

    # DATE
    if "date" in userquestion:
        return "📅 Today's date is " + datetime.datetime.now().strftime("%d-%m-%Y")

    # ADDITION
    if "add" in userquestion:
        nums = [int(n) for n in userquestion.split() if n.isdigit()]
        if len(nums) >= 2:
            return f"The sum is {sum(nums)} ➕"
        else:
            return "Please give at least two numbers!"

    # SEARCH IN RESPONSES
    for key in responses:
        if key in userquestion:
            return random.choice(responses[key])

    return None  # means bot didn't understand

# ---------------------------------------
# MAIN CHAT LOOP
# ---------------------------------------
while True:

    userinput = input("\nYou: ")

    if userinput.lower() in ["bye", "exit", "quit"]:
        bot_says("ChatBot: Goodbye! Take care ❤️")
        break

    reply = get_response(userinput)

    if reply:
        bot_says("ChatBot: " + reply)
    else:
        bot_says("ChatBot: I don't know that yet. Teach me! 🙂")
        new_answer = input("Type the correct answer: ")
        responses[userinput.lower()] = [new_answer]
        bot_says("ChatBot: Got it! I learned something new 🤝")
