import xml.etree.ElementTree as ET
import json

def checkInput(data, headers):
    contentType = headers['Content-Type']
    if data: 
        if contentType == 'application/xml':
            try:
                xmlTree = ET.fromstring(data)
                xmlstr = ET.tostring(xmlTree, encoding='utf8', method='xml')
                return xmlstr, 200
            except:
                return 'please supply valid xml', 400
        elif(contentType == 'application/json'):
            try:
                jsonData = json.loads(data)
                return jsonData, 200
            except:
                return 'please supply a valid json'
        else:
            return 'please add a Content-Type (either application/xml or application/json'
    else:
        return 'please add a valid payload', 400