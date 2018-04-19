from flask import Flask, request, json
app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def recv_data():
    data = request.get_data()
    data = json.loads(data)
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
