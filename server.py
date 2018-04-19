from flask import Flask, request, json
import api
app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def recv_data():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    print(parse(data))


def parse(data):
    body = data['text']
    words = body.split(" ")
    if len(words) == 2 and words[0] == "!show":
        result = api.fetch_by_name(words[1])
        if result['Status'] == -1:
            return result['Message']
        else:
            return result['Content']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
