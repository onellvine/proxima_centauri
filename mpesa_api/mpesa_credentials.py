import requests
from requests.auth import HTTPBasicAuth
import json
import base64
from datetime import datetime


class MpesaC2bCredential:
    consumer_key = 'J1K4yO500AEGIjZmWBGVw86QUd0AFNMQ'
    consumer_secret = 'ZNfAygFtWutuAAO3'
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"


class MpesaAccessToken:
    auth = HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret)
    r = requests.get(MpesaC2bCredential.api_url, auth=auth)
    mpesa_access_token = json.loads(r.text)
    validated_access_token = mpesa_access_token['access_token']


class LipaNaMpesaPassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = '174379'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    data_to_encode = Business_short_code + passkey + lipa_time
    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')


