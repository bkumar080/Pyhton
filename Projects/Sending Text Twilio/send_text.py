from twilio.rest import TwilioRestClient

account_sid = "AC9e3a2a2b336043fb3cd15240fc5e013f" # Your Account SID from www.twilio.com/console
auth_token  = "63f70942a18a9c555a458342d1b5c2f5"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="My name is Bharath kumar",
    to="+12017906958",    # Replace with your phone number
    from_="+19734357648 ") # Replace with your Twilio number

print(message.sid)
