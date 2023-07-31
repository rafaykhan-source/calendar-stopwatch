"""A class representing a Google Calendar Event.

This module defines the Event ADT, which wraps the Google Calendar Event.

Typical usage example:

  event = Event()
  event.create_event_from_session(session)
  event_info = event.get_event_dictionary()
"""

import time
from datetime import datetime
from session import Session


class Event:
    def __init__(
        self,
        summary: str = "",
        description: str = "",
        start_date: datetime = None,
        end_date: datetime = None,
    ) -> None:
        self.event = {
            "summary": f"{summary}",
            "description": f"{description}",
            "start": {
                "dateTime": f"{start_date.isoformat() if start_date else ''}",
                "timeZone": "America/New_York",
            },
            "end": {
                "dateTime": f"{end_date.isoformat() if end_date else ''}",
                "timeZone": "America/New_York",
            },
        }
        return

    def create_event_from_session(self, session: Session) -> None:
        start_date, end_date = session.get_session_time_range()
        duration = f"Duration: {session.get_duration()}"
        self.event = {
            "summary": f"{session.title}",
            "description": f"{session.description}\n{duration}",
            "start": {
                "dateTime": f"{start_date.isoformat()}",
                "timeZone": "America/New_York",
            },
            "end": {
                "dateTime": f"{end_date.isoformat()}",
                "timeZone": "America/New_York",
            },
        }

    def get_event_dictionary(self) -> dict:
        """Returns the Event Information as a dictionary.

        Returns:
            dict: event information dictionary
        """
        return self.event

    def __str__(self):
        return f"""
Summary: {self.event["summary"]}
Description: {self.event["description"]}
Start Date: {self.event["start"]["dateTime"]}
End Date: {self.event["end"]["dateTime"]}
"""


def main() -> None:
    session = Session(
        title="Marshmallow Development",
        description="Intensive Refactoring",
    )

    session.begin()
    time.sleep(5)
    session.end()

    event = Event()
    event.create_event_from_session(session)
    print(event)
    event_info = event.get_event_dictionary()
    print(event_info)
    # event = Event(
    #     summary="Marshmallow Development",
    #     description="Intensive Refactoring",
    #     start_date=datetime(year=2023, month=7, day=29, hour=16),
    #     end_date=datetime(year=2023, month=7, day=29, hour=18),
    # )
    return


if __name__ == "__main__":
    main()
