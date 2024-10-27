import requests


url = 'http://localhost:9696/predict'

customer_id = 'xyz-123'
client = {"job": "management", "duration": 400, "poutcome": "success"}
requests.post(url, json=client).json()


response = requests.post(url, json=client).json()
print(response)

if response['predict'] == True:
    print('sending promo email to %s' % customer_id)
else:
    print('not sending promo email to %s' % customer_id)