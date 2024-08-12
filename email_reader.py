from multion.client import MultiOn
import os
import json
from dotenv import load_dotenv

load_dotenv()
multi_on_api_key = os.getenv("MULTION_API_KEY")


client = MultiOn(api_key=multi_on_api_key)

retrieve_response = client.retrieve(
    cmd="Get me all the emails asking to schedule a meeting with me.",
    url="https://mail.google.com/mail/u/0/#inbox",
    fields=["name", "email_received_time", "body"],
    local=True
)


data = retrieve_response.data
print('Response from Calendar: ')
print(json.dumps(data, indent=2))

