import httplib, urllib, base64, json, re
from os import system


# CHANGE {MS_API_KEY} BELOW WITH YOUR MICROSOFT VISION API KEY
ms_api_key = ""

# setup vision API
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': ms_api_key,
}

params = urllib.urlencode({
    'visualFeatures': 'Description',
})

print('Analyze')
body = open('1.jpg', "rb").read()
conn = httplib.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
conn.request("POST", "/vision/v1.0/analyze?%s"%params, body, headers)
response = conn.getresponse()
analysis = json.loads(response.read())
#print(analysis)
caption_analysis = analysis["description"]["captions"][0]["text"].capitalize()
print(caption_analysis)

print('Describe')
conn.request("POST", "/vision/v1.0/describe?%s"%params, body, headers)
response0 = conn.getresponse()
analysis0 = json.loads(response0.read())
#print(analysis0)
caption_describe = analysis0["description"]["captions"][0]["text"].capitalize()
print(caption_describe)

print('OCR')
conn.request("POST", "/vision/v1.0/ocr?%s" % params, body, headers)
response1 = conn.getresponse()
analysis1 = json.loads(response1.read())
print(analysis1)
ocr = analysis1["text"].capitalize()
print(ocr)

print('Handwriting')
conn.request("POST", "/vision/v1.0/recognizeText[?handwriting]%s" % params, body, headers)
response2 = conn.getresponse()
analysis2 = json.loads(response2.read())
print(analysis2)
