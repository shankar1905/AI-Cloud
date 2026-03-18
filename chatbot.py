def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("🤖 Chatbot: Hi! How can I help you?")
        
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm doing great 😄")
        
        elif user_input == "your name":
            print("🤖 Chatbot: I'm your AI assistant 🤖")

        # 👉 ADD HERE 👇
        elif "price" in user_input:
            print("🤖 Chatbot: Please check our website for pricing 💰")
        
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye 👋")
            break
        
        else:
            print("🤖 Chatbot: I don't understand 😅")

chatbot()