from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

with open('intents.json') as file:
    intents = json.load(file)['intents']

def get_intent(text):
    for intent in intents:
        for pattern in intent['patterns']:
            if pattern.lower() in text.lower():
                return intent
    return None

def generate_response(intent_tag):
    for intent in intents:
        if intent['tag'] == intent_tag:
            return random.choice(intent['responses'])
    return "Maaf, saya tidak mengerti."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def process_response():
    user_input = request.form['user_input']
    intent = get_intent(user_input)
    if intent:
        response = generate_response(intent['tag'])
    else:
        response = "Maaf, saya tidak mengerti pertanyaan Anda."
    return response 

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
