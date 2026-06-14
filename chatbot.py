def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Chatbot: Hi!")
        elif user == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user == "what is your name":
            print("Chatbot: My name is Chatbot.")
        elif user == "who created you":
            print("Chatbot: I was created by a programmer.")
        elif user == "what can you do":
            print("Chatbot: I can answer simple questions.")
        elif user == "good morning":
            print("Chatbot: Good morning! Have a nice day.")
        elif user == "good night":
            print("Chatbot: Good night! Sweet dreams.")
        elif user == "thank you":
            print("Chatbot: You're welcome!")
        elif user == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand.")


chatbot()
