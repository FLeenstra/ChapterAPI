from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def root():
    data = request.data
    #headers = request.headers

    if data:
        try:
            jsondata = json.loads(data)
            return jsondata, 200
        except:
            return 'please supply valid json', 400
    else:
        return 'please add a json payload', 400
