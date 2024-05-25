from flask import Flask, render_template, request, jsonify
import requests

RASA_API_URL = "http://localhost:5005/webhooks/rest/webhook"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json['message']
    print("User Message:", user_message)
    
    # Send user message to Rasa and get bot's response
    rasa_response = requests.post(RASA_API_URL, json={'sender': 'user', 'message': user_message})
    rasa_response_json = rasa_response.json()

    print("Rasa Response:", rasa_response_json)

    responses = []
    for message in rasa_response_json:
        if 'text' in message:
            responses.append({'type': 'text', 'content': message['text']})
        if 'image' in message:
            responses.append({'type': 'image', 'content': message['image']})
        if 'buttons' in message:
            buttons = [{'title': button['title'], 'payload': button['payload']} for button in message['buttons']]
            responses.append({'type': 'buttons', 'buttons': buttons})

    return jsonify({'responses': responses})

if __name__ == "__main__":
    app.run(debug=True, port=3000)
