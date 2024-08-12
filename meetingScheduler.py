from multion.client import MultiOn
import os
from dotenv import load_dotenv
import json
import re


load_dotenv()


class MeetingScheduler:
    def __init__(self):
        multi_on_api_key = os.getenv("MULTION_API_KEY")
        self.client = MultiOn(api_key=multi_on_api_key)
        self.email_address = ""
        self.sender_name = ""
        self.email_received_time = ""
        self.email_body = ""
    
    def meeting_request_search(self):
        create_session = self.client.sessions.create(
            url="https://mail.google.com/mail/u/0/#inbox",
            local=True
        )
        sessionId = create_session.session_id
        browse_response = self.client.browse(
            cmd="Search the email page for the latest email asking me to schedule meeting or meet and then open that email by clicking on it.",
            session_id=sessionId,
            local=True
        )
        retrieve_response = self.client.retrieve(
            cmd="I want to know the following contents about the email you see on the screen regarding scheduling a meeting: email address of the sender who sent the email [should be displayed as 'from:'], time the email was received, and the name of the sender, body of the email",
            session_id=sessionId,
            fields=["email_address", "email_received_time", "name", "body"],
            local=True
        )

        data = retrieve_response.data
        json_data = data[0] if data else {}
        print(json_data)
        self.sender_name = json_data["name"] if "name" in json_data else None
        if self.is_email_address(self.sender_name):
            self.email_address = self.sender_name
        else:
            self.email_address = json_data["email_address"] if "email_address" in json_data else None

        self.email_received_time = json_data["email_received_time"] if "email_received_time" in json_data else None
        self.email_body = json_data["body"] if "body" in json_data else None
    
    def is_email_address(self, email_address):
        # Simple email validation regex
        return re.match(r"[^@]+@[^@]+\.[^@]+", email_address) is not None


meeting_scheduler = MeetingScheduler()
meeting_scheduler.meeting_request_search()

print(meeting_scheduler.email_address)
print(meeting_scheduler.sender_name)
print(meeting_scheduler.email_received_time)
print(meeting_scheduler.email_body)


        