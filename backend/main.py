import openai
import json
import array

openai.api_key = "YOUR_API_KEY"

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/chat", methods=["POST"])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def chat():
    message = request.form["message"]
    chat_log = request.form.get("chat_log")

    # Parse chat_log as a list of messages if it exists, else start with an empty list
    messages = json.loads(chat_log) if chat_log else []

    # Add the user's message to the messages array
    messages.append({"role": "user", "content": message})
    # Build the input to the OpenAI API
    input_text = json.dumps([{"role": "user", "content": message}])
    print(input_text)

    # Get the response from the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=input_text,
        temperature=0.7,
        max_tokens=1024,
        stop=None,
    )
    print(response)

    # Extract the response message and add it to the messages array
    response_message = response.choices[0].message['content'].strip()
    messages.append({"role": "assistant", "content": response_message})

    # Build the response to be returned to the client
    response_data = {
        "messages": messages
    }

    resp = make_response(jsonify(response_data))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == "__main__":
    app.run(debug=False)
