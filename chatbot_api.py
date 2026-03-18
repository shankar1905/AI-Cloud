from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ ADD THIS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow Angular
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Chatbot API running 🚀"}

@app.get("/chat")
def chat(user_input: str):
    user_input = user_input.lower()

    if user_input == "hello":
        return {"response": "Hi! How can I help you?"}
    
    elif user_input == "how are you":
        return {"response": "I'm doing great 😄"}
    
    elif "price" in user_input:
        return {"response": "Please check our website for pricing 💰"}
    
    elif user_input == "bye":
        return {"response": "Goodbye 👋"}

    elif user_input == "time":
        from datetime import datetime
        now = datetime.now().strftime("%H:%M")
        return {"response": f"The current time is {now} ⏰"}
    
    elif user_input == "date":
        from datetime import datetime
        today = datetime.now().strftime("%Y-%m-%d")
        return {"response": f"Today's date is {today} 📅"}
    
    else:
        return {"response": "I don't understand 😅"}