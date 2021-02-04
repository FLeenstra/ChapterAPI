from flask import Flask, request
from checks import checkInput

app = Flask(__name__)

@app.route('/', methods=['POST'])
def root():
    data = request.data
    #headers = request.headers
    
    result = checkInput(data)
    return result
    
