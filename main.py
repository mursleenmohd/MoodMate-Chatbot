from responses.mood_responses import get_response

print("Hello! I’m MoodMate – Tumhara emotional support chatbot.")
print("Apna mood type karo (happy, sad, angry, bored, etc.)")
print("Type 'exit' to end the chat.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bye! Take care of yourself ")
        break
    
    response = get_response(user_input)
    print("MoodMate:", response)
