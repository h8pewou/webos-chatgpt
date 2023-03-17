import openai
import json
import array

openai.api_key = "YOUR_API_KEY"

chat_log = []

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/chat", methods=["POST"])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def chat():
    message = request.form["message"]
    global chat_log

    # Overwrite messages with chat_log
    messages = []
    messages = chat_log

    # Add the user's message to the messages array
    new_message = {"role": "user", "content": message}
    messages.append(new_message)

    # Build the input to the OpenAI API
    input_text = json.dumps(messages)

    # Get the response from the OpenAI API
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

    resp = make_response(jsonify({'message': response_message}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == "__main__":
    app.run(debug=False)