import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

#GENERATING THE ACCESS TOKEN
consumer_key = "< your app customer key>"
consumer_secret = " < your app customer secret > "

api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials" #AUTH URL

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

data = r.json()
access_token = "Bearer" + ' ' + data['access_token']

#GETTING THE PASSWORD
timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
passkey = '< pass code of the profile >'
business_short_code = "< business short code >"
data = business_short_code + passkey + timestamp
encoded = base64.b64encode(data.encode())
password = encoded.decode('utf-8')


# BODY OR PAYLOAD
payload = {
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

#POPULAING THE HTTP HEADER
headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest" #C2B URL

response = requests.post(url, json=payload, headers=headers)

print (response.text)

