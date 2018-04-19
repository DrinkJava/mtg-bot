from flask import Flask, request, json
app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def recv_data():
    data = request.get_data()
    data = json.loads(data)
    return data
