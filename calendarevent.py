import datetime
import os.path
import random
import json
from dateutil.parser import parse
from dateutil.parser import ParserError

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]
random_number = random.randint(1000, 9999)

def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)

        # Load messages from JSON file
        with open('messages.json', 'r') as file:
            data = json.load(file)

        user_message = data['User'][2]  # Example: "i want a Comcast technician to come look at it tomorrow"

        # Attempt to parse the date from the entire user message
        try:
            event_date = parse(user_message, fuzzy=True)
        except ParserError:
            raise ValueError("Could not parse any date from the user message.")

        event = {
            'summary': f'{user_message}#{random_number}',
            'location': 'Customer House',
            'description': 'Scheduled based on user request',
            'start': {
                'dateTime': event_date.isoformat(),
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': (event_date + datetime.timedelta(hours=1)).isoformat(),  # Assuming a 1-hour appointment
                'timeZone': 'America/Los_Angeles',
            },
            'attendees': [
                {'email': 'ml3653du@gmail.com'},
            ]
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))

    except HttpError as error:
        print(f"An error occurred: {error}")
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
