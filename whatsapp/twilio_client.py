# whatsapp/twilio_client.py
from twilio.rest import Client
from config.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, USER_PHONE_NUMBER

def send_whatsapp_reminder(message_text: str):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message_text,
        from_=TWILIO_PHONE_NUMBER,
        to=USER_PHONE_NUMBER
    )
    print("📤 Reminder sent successfully! SID:", message.sid)
