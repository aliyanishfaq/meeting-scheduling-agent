from multion.client import MultiOn
import os
import json
from dotenv import load_dotenv

load_dotenv()
multi_on_api_key = os.getenv("MULTION_API_KEY")


client = MultiOn(api_key=multi_on_api_key)

follow_response = client.browse(
    cmd="Open my inbox and compose an email to 'aliyanishfaq200@gmail.com Ask them to meet at 12.30 PT tomorrow!",
    url="https://mail.google.com/mail/u/0/#inbox",
    local=True,
)

print(follow_response.message)


