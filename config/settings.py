# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
USER_PHONE_NUMBER = os.getenv("USER_PHONE_NUMBER")
