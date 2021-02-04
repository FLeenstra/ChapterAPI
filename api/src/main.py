from flask import Flask, request
from checks import checkInput

app = Flask(__name__)

@app.route('/', methods=['POST'])
def root():
    data = request.data
    #headers = request.headers

    result = checkInput(data)

    if result[1] != 200:
        return result
    else:
        return 'kippiyayee', 200
    
