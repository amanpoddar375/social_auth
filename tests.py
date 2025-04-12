# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print(f"GOOGLE_CLIENT_ID: {os.getenv('GOOGLE_CLIENT_ID')}")
print(f"GOOGLE_CLIENT_SECRET: {os.getenv('GOOGLE_CLIENT_SECRET')}")
print(f"FACEBOOK_APP_ID: {os.getenv('FACEBOOK_APP_ID')}")
print(f"FACEBOOK_APP_SECRET: {os.getenv('FACEBOOK_APP_SECRET')}")