from multion.client import MultiOn
import os
import json
from dotenv import load_dotenv

load_dotenv()
multi_on_api_key = os.getenv("MULTION_API_KEY")


client = MultiOn(api_key=multi_on_api_key)

retrieve_response = client.browse(
    cmd="Go to Google Meet right now. Click on the new meeting button. Click on create a meeting for later. Copy the meeting link.",
    url="https://meet.google.com/landing",
    local=True
)


data = retrieve_response.message
print('Response from Calendar: ')
print(json.dumps(data, indent=2))

