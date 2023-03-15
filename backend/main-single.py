from flask import Flask, jsonify, make_response, request
from flask_cors import CORS, cross_origin
import openai

openai.api_key = "YOUR_KEY"

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/chat", methods=["POST"])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def chat():
    message = request.form["message"]
    prompt = {
        "role": "user",
        "content": message
    }
    messages = [prompt, {"role": "assistant", "content": ""}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=1024,
        stop=None,
    )
    generated_text = response.choices[0].message['content'].strip()
    resp = make_response(jsonify({'message': generated_text}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == "__main__":
    app.run()
