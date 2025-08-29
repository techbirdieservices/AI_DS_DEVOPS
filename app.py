from flask import Flask, render_template, request, jsonify
import wikipedia
import datetime
import webbrowser
import openai
import random
from config import OPENAI_API_KEY

app = Flask(__name__)
openai.api_key = OPENAI_API_KEY

def get_ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message['content']
    except Exception:
        return "I'm sorry, I couldn't process that right now. Please try again!"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_command', methods=['POST'])
def process_command():
    data = request.json
    command = data.get('command', '').lower()

    # Introduction
    introduction = (
        "Hello! I am Carlos, your personal virtual assistant. "
        "I can open your favorite websites and search anything online. "
        "I can answer questions using AI intelligence. "
        "I can tell you the current time and help with tasks. "
        "Ready to assist you whenever you need!"
    )

    # Websites Carlos can open
    websites = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "facebook": "https://facebook.com",
        "instagram": "https://instagram.com",
        "twitter": "https://twitter.com",
        "github": "https://github.com",
        "stack overflow": "https://stackoverflow.com",
        "netflix": "https://netflix.com",
        "amazon": "https://amazon.com",
        "abp news": "https://www.abplive.com",
        "ndtv": "https://www.ndtv.com",
        "times of india": "https://timesofindia.indiatimes.com",
        "india today": "https://www.indiatoday.in",
        "music": "https://music.youtube.com"
    }

    # Fun jokes
    jokes = [
        "Why did the computer get cold? Because it forgot to close its Windows!",
        "Why was the math book sad? Because it had too many problems.",
        "I'm reading a book about anti-gravity. It's impossible to put down!",
        "What do you call fake spaghetti? An impasta!"
    ]

    # Random positive moods
    moods = [
        "Alright!", "Sure thing!", "Got it!", "Here you go!", "Coming right up!", "Opening as you wish!"
    ]

    # Greetings
    greetings = [
        "Hey there! I'm Carlos, always ready to help.",
        "Hello! Carlos here — what can I do for you?",
        "Hi! Need assistance? Carlos is here.",
        "Greetings! Carlos at your service.",
        "Good to see you! I'm Carlos, your buddy."
    ]

    if 'introduce yourself' in command:
        response = introduction

    elif 'wikipedia' in command:
        query = command.replace("wikipedia", "").strip()
        try:
            results = wikipedia.summary(query, sentences=2)
            response = "According to Wikipedia: " + results
        except Exception:
            response = "Oops, I couldn't find that on Wikipedia."

    elif 'the time' in command or 'current time' in command:
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {strTime}."

    elif 'joke' in command:
        response = random.choice(jokes)

    elif any(site in command for site in websites):
        for site in websites:
            if site in command:
                webbrowser.open(websites[site])
                mood = random.choice(moods)
                site_name = site.replace("stack overflow", "Stack Overflow").replace("times of india", "Times of India").title()
                response = f"{mood} Opening {site_name} for you."
                break

    elif any(word in command for word in ['search', 'find', 'look up']):
        query = command.replace('search', '').replace('find', '').replace('look up', '').strip()
        if query:
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
            mood = random.choice(moods)
            response = f"{mood} Searching the web for {query}."
        else:
            response = "I'm here to help, please tell me what you want to search for."

    elif any(word in command for word in ['hello', 'hi', 'hey']):
        response = random.choice(greetings)

    else:
        ai_response = get_ai_response(command)
        if ai_response:
            response = ai_response
        else:
            response = "I'm sorry, I didn't quite catch that. Could you please repeat?"

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5000, debug=True)