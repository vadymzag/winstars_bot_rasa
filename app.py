from flask import Flask, render_template, request, Response
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=['GET', 'POST'])
def get_bot_response():
    userText = request.args.get('msg')
    print(userText)
    data = json.dumps({"sender": "Rasa", "message": userText})
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    res = requests.post('http://localhost:5005/webhooks/rest/webhook', data=data, headers=headers)
    res = res.json()
    print(res)
    response = res[0]["text"]

    return Response(response)



if __name__ == "__main__":
    app.run(debug=True)
