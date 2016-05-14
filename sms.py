import twilio
from twilio.rest import TwilioRestClient

print(twilio.__file__)
print(twilio.__version__)
print('test \n \n')


account_sid = "" # Your Account SID from www.twilio.com/console
auth_token  = ""  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Python",
    to="+",    # Replace with your phone number
    from_="+") # Replace with your Twilio number

print(message.sid)
# print 