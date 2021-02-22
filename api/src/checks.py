import xml.etree.ElementTree as ET

def checkInput(data):
    if data: 
        try:
            xmlTree = ET.fromstring(data)
            xmlstr = ET.tostring(xmlTree, encoding='utf8', method='xml')
            return xmlstr, 200
        except:
            return 'please supply valid xml', 400
    else:
        return 'please add a xml payload', 400