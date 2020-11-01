from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render 
from django.views.decorators.csrf import csrf_exempt

import json
import requests

from .mpesa_credentials import MpesaAccessToken, LipaNaMpesaPassword
from .models import MpesaPayment

from proxima_user.forms import LoginUserForm


def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    if request.user.is_authenticated:
        request = {
            "BusinessShortCode": LipaNaMpesaPassword.Business_short_code,
            "Password": LipaNaMpesaPassword.decode_password,
            "Timestamp": LipaNaMpesaPassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": int(request.POST['exped_price']),
            "PartyA": int(request.user.phone.lstrip("+")),  # replace with your phone number to get stk push
            "PartyB": LipaNaMpesaPassword.Business_short_code,
            "PhoneNumber": int(request.user.phone.lstrip("+")),  # replace with your phone number to get stk push
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": request.user.user_name,
            "TransactionDesc": "Testing stk push"
        }

        response = requests.post(api_url, json=request, headers=headers)
        return redirect('home')
    else:
        form = LoginUserForm()
        return render(request, "users/login.html", {'form': form})


@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipaNaMpesaPassword.Business_short_code,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://de2fa9d106b0.ngrok.io/api/v1/c2b/confirmation",
               "ValidationURL": "https://de2fa9d106b0.ngrok.io/api/v1/c2b/validation"}

    response = requests.post(api_url, json=options, headers=headers)
    return HttpResponse(response.text)


@csrf_exempt
def call_back(request):
    pass


@csrf_exempt
def validation(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))


@csrf_exempt
def confirmation(request):
    mpesa_body = request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    payment = MpesaPayment(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['LastName'],
        middle_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        organization_balance=mpesa_payment['OrgAccountBalance'],
        payment_type=mpesa_payment['TransactionType'],
    )
    payment.save()
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))

