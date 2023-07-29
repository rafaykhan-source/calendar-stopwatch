from __future__ import print_function

import datetime
import os.path
import sys

sys.path.append("..")

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from event import Event

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def get_credentials() -> Credentials:
    creds = None
    
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("config/token.json"):
        creds = Credentials.from_authorized_user_file(
            "config/token.json", SCOPES
        )
        
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "config/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("config/token.json", "w") as token:
            token.write(creds.to_json())
    
    return creds
    
def get_service() -> Any:
    creds = get_credentials()
    try:
        service = build("calendar", "v3", credentials=creds)
    except HttpError as error:
        print(f"Error: {error}")
        return None
    return service
    

def add_event(cal_event: Event) -> None:
    service = get_service()
    event = service.events().insert(calendarId="primary", body=cal_event.get_event_dictionary()).execute()
    print(f"Event created: {event.get('htmlLink')}")
    return
    
    
def main() -> None:
    event = Event(
        summary="Marshmallow Development",
        description="Intensive Refactoring",
        start_date=datetime.datetime(year=2023, month=7, day=29, hour=16),
        end_date=datetime.datetime(year=2023, month=7, day=29, hour=18),
    )
    add_event(event)
    return

if __name__ == "__main__":
    main()