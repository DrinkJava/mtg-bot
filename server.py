from flask import Flask, request, json
import api
import requests
app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def recv_data():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    res = parse(data)
    print(res)
    if res["Status"] > -1:
        send_message(res)
    return "Poop"

def parse(data):
    body = data['text']
    if body.startswith("!"):
        result = api.fetch_by_name(body[1:])
        return result
    else:
        return {"Status" : -1, "Message" : "", "Content" :""}

def send_message(res):
    print("FUCK")
    body = { "bot_id" : "50d89f4106b186b5fe4f1c3e4a",
             "text" : res['Content'].name,
             "attachments" : [
                 {
                     "type" : "image",
                     "url" : res['Content'].image_url
                 }
             ]
    }

    re = requests.post("https://api.groupme.com/v3/bots/post", json=body)
    print(vars(re))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
