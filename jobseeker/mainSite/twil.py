from twilio.rest import Client
import dotenv
import os

dotenv.load_dotenv()

# Your Account SID from twilio.com/console
account_sid = "AC2395b047e53f04d47b4010e11a9d81a4"

# Your Auth Token from twilio.com/console
auth_token = os.environ['TWILIO_SECRET']

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+447579065474",
    from_="+447700167693",
    body="SHUT UP PLEASE!")

def send_message(msg):
    client.messages.create(
        to="+447579065474",
        from_="+447700167693",
        body=msg)

