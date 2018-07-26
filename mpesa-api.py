from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import time
import base64
import json

app = Flask(__name__)


@app.route('/krafty', methods = ['POST'])
def api_message():
    data = request.data
    print(data)
    return "already run"


timestamp = str(time.strftime("%Y%m%d%H%M%S"))

password = base64.b64encode(bytes(u'174379' + '< pass code of the profile >' + timestamp, 'UTF-8'))


consumer_key = "< your app customer key>"
consumer_secret = " < your app customer secret > "
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

y = json.loads(requests.get(api_URL, auth=HTTPBasicAuth(consumer_key,consumer_secret)).text)

print(y['access_token'])

# import pdb; pdb.set_trace()

access_token = "{}".format(y['access_token'])
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = { "Authorization": "Bearer {}".format(access_token)}
request = {
    "BusinessShortCode": "< business name >",
    "Password": "{}".format(password),
    "Timestamp": "{}".format(timestamp),
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "1",
    "PartyA": "< phone number to be billed >",
    "PartyB": "174379",
    "PhoneNumber": "< phone number to be billed >",
    "CallBackURL": "http://<call back url must be a real url>",
    "AccountReference": "account",
    "TransactionDesc": "account"
}



response = requests.post(api_url, json = request, headers=headers)

print(response.text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

