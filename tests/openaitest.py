from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import openai

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Set your OpenAI API key here
openai.api_key = "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"

@app.route('/')
def index():
    return render_template('openaitest.html')

@socketio.on('message')
def handle_message(data):
    user_message = data.get('message')

    # Call the function to get the chatbot response
    response = generate_response(user_message)

    emit('response', {'response': response})

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    socketio.run(app, port=8000)
