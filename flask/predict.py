import requests
import json

def predict(img):
    headers = {'Prediction-Key':'2ba88bde2b634731bd9d4e34e68a3001',"Content-Type": "application/octet-stream",'cache-control': "no-cache"}
    url = 'https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/5c3a415d-068c-4a67-b725-7c74a84d660c/image'
    data = open(img, 'rb').read()
    r = requests.post(url, headers=headers, data=data)
    print(type(r.text))
    predictions = json.loads(r.text)['predictions']
    return predictions

if __name__ == "__main__":
    predict('test1.png')