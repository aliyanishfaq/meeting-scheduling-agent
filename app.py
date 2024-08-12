from multion.client import MultiOn
import os
import json
from dotenv import load_dotenv

load_dotenv()
multi_on_api_key = os.getenv("MULTION_API_KEY")


client = MultiOn(api_key=multi_on_api_key)

retrieve_response = client.retrieve(
    cmd="Get all the events in my calendar for today.",
    url="https://calendar.google.com/calendar/u/0/r/day?pli=1",
    fields=["name", "start time", "end time", "location", "description"],
    local=True
)


data = retrieve_response.data
print('Response from HackerNews: ')
print(json.dumps(data, indent=2))

