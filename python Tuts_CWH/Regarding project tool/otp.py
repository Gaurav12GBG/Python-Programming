import twilio
import os
from twilio.rest import Client
import random

otp = random.randint(1000, 9999)
print(otp)

mobile_number = int(input("Enter your mobile number"))

account_sid = 'ACb109542d3db0e02155aefe38239f06c5'
auth_token = '25d605663b3b4e6ff46d9a4c2f0fcb49'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='Your OTP is -'+str(otp),
         from_='+12056497664',
         to='+91'+str(mobile_number)
     )

print(message.sid)



