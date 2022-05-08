# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from decouple import config


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
print('TWILIO_ACCOUNT_SID:',config('TWILIO_ACCOUNT_SID'))
print('TWILIO_AUTH_TOKEN',config('TWILIO_AUTH_TOKEN'))


print('TWILIO_PHONE_NUMBER',config('TWILIO_PHONE_NUMBER'))
account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')


client = Client(account_sid, auth_token)

message = client.messages.create(
        #  messaging_service_sid='MG9752274e9e519418a7406176694466fa',
        from_=config('TWILIO_PHONE_NUMBER'),
        body='Hello from Python!{}'.format(config('TWILIO_PHONE_NUMBER')),
        to='+256775236691'
     )

print(message.sid)
