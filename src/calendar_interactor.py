"""A module responsible for google calendar API interactions.

This module contains several functions relevant to interacting
with the google calendar API (e.g. grabbing credentials,
starting a session, adding and reading events)

Typical usage example:

  read_event()
  add_event()
"""

import datetime
import os.path

from adt.event import Event
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_credentials() -> Credentials:
    """Returns credentials for accessing google calendar.

    Returns:
        Credentials: credentials for accessing google calendar.
    """
    creds = None

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("config/token.json"):
        creds = Credentials.from_authorized_user_file("config/token.json", SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "config/credentials.json",
                SCOPES,
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("config/token.json", "w") as token:
            token.write(creds.to_json())

    return creds


def get_service() -> any:
    """Returns service google calendar interactions."""
    creds = get_credentials()
    try:
        service = build("calendar", "v3", credentials=creds)
    except HttpError as error:
        print(f"Error: {error}")
        return None
    return service


def add_event(event: Event) -> None:
    """Adds event to the primary google calendar.

    Args:
        event (Event): event to add to google calendar.
    """
    service = get_service()
    cal_event = (
        service.events()
        .insert(calendarId="primary", body=event.get_event_dictionary())
        .execute()
    )
    print(f"Event created: {cal_event.get('htmlLink')}")
    return


def read_event(amount: int) -> None:
    """Prints upcoming events.

    Args:
        amount (int): number of upcoming events
    """
    service = get_service()
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    print(f"Getting the upcoming {amount} events.")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=amount,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
        print("No upcoming events found.")
        return

    # Prints the start and name of the next amount events
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        print(start, event["summary"])


def main() -> None:
    """Unit Testing."""
    # event = Event(
    #     summary="Marshmallow Development",
    #     description="Intensive Refactoring",
    #     start_date=datetime.datetime(year=2023, month=7, day=29, hour=10),
    #     end_date=datetime.datetime(year=2023, month=7, day=29, hour=12),
    # )
    # add_event(event)
    read_event(5)
    return


if __name__ == "__main__":
    main()
