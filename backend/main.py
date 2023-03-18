# Import necessary libraries and modules
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS, cross_origin
import openai
import json
import array

# Set the OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Initialize messages as an array with a system prompt. This array will be used to keep track of conversation history.
messages = [
       {"role": "system", "content": "You are a webOS chatbot, your name is Universal Search. Answer as concisely as possible and make sure that your responses do not require any formatting."}
    ]

# Create a Flask application instance
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Define a route to handle incoming chat requests
@app.route("/chat", methods=["POST"])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def chat():
    # Get the user's message from the request form
    message = request.form["message"]
    global messages

    # Add the user's message to the messages array
    new_message = {"role": "user", "content": message}
    messages.append(new_message)

    # Convert the messages array to JSON for input to the OpenAI API
    input_text = json.dumps(messages)

    # Get a response from the OpenAI API using the GPT-3.5-Turbo model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=json.loads(input_text),
        temperature=0.7,
        max_tokens=1024,
        stop=None,
    )

    # Extract the response message and add it to the messages array
    response_message = response.choices[0].message['content'].strip()
    new_response = {"role": "assistant", "content": response_message}
    messages.append(new_response)

    # Build the response to be returned to the client
    response_data = {
        "messages": messages
    }

    # Create a Flask response with the JSON response data
    resp = make_response(jsonify({'message': response_message}))
    # Set CORS headers
    resp.headers['Access-Control-Allow-Origin'] = '*'
    # Return the response to the client
    return resp

# Start the Flask application
if __name__ == "__main__":
    app.run(debug=False)
