import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from weather import get_sydney_weather

# Load environment variables from .env
load_dotenv()

slack_token = os.getenv("SLACK_TOKEN")
user_id = os.getenv("USER_ID")
client = WebClient(token=slack_token)
data = get_sydney_weather()

try:
    response = client.chat_postMessage(
        channel=user_id, 
        text=data
        
    )
    print("Message sent successfully:", response["ts"])
except SlackApiError as e:
    print(f"Error sending message: {e.response['error']}")
