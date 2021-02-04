import json

def checkInput(data):
    if data: 
        try:
            jsondata = json.loads(data)
            return jsondata, 200
        except:
            return 'please supply valid json', 400
    else:
        return 'please add a json payload', 400