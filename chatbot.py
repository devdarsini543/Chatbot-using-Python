# Building a Chatbot using if-else
print("🤖 ChatBot: Hi! I'm your friendly chatbot.")
print("Type 'bye' anytime to end the chat.\n")

while True:
    user_input = input("You: ").lower()
    
    if user_input == "hello" or user_input == "hi":
        print("🤖 ChatBot: Hello there! How are you today?")
    
    elif "how are you" in user_input:
        print("🤖 ChatBot: I'm doing great, thanks for asking! How about you?")
    
    elif "your name" in user_input:
        print("🤖 ChatBot: I’m ChatBot 1.0, created using Python if-else rules.")
    
    elif "time" in user_input:
        from datetime import datetime
        print("🤖 ChatBot: The current time is", datetime.now().strftime("%H:%M:%S"))
    
    elif "date" in user_input:
        from datetime import date
        print("🤖 ChatBot: Today's date is", date.today())
    
    elif "bye" in user_input:
        print("🤖 ChatBot: Goodbye! Have a nice day! 👋")
        break
    
    else:
        print("🤖 ChatBot: Sorry, I didn’t understand that. Can you rephrase?")
