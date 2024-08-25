"""A class storing Google Calendar Event information.

This module defines the Event ADT, which wraps the information relevant
to a google calendar event.

Typical usage example:

  event = Event()
  event.create_event_from_session(session)
  event_info = event.get_event_dictionary()
"""

import logging
import time
from datetime import datetime

from adt.session import Session

logger = logging.getLogger("ADTs")


class Event:
    """This class wraps information pertaining to a google calendar event."""

    def __init__(
        self,
        session: Session | None = None,
        summary: str = "",
        description: str = "",
        start_date: datetime | None = None,
        end_date: datetime | None = None,
    ) -> None:
        """Instantiates the event.

        Args:
            session (Session, optional): Session to make event from. Defaults to None.
            summary (str, optional): Summary or event title. Defaults to "".
            description (str, optional): Details of the event.. Defaults to "".
            start_date (datetime, optional): Event's start datetime. Defaults to None.
            end_date (datetime, optional): Event's end datetime. Defaults to None.
        """
        if not isinstance(summary, str):
            logging.error("Error: summary is not of type str.")
            return
        if not isinstance(description, str):
            logging.error("Error: description is not of type str.")
            return
        self.summary = summary
        "The event title."
        self.description = description
        "The event description."
        self.start_date = start_date
        "The event start datetime."
        self.end_date = end_date
        "The event end datetime."
        if session:
            self.summary = session.title
            self.description = (
                session.description + f"Duration: {session.get_duration()}"
            )
            self.start_date, self.end_date = session.get_time_range()
        return

    def get_event_dictionary(self) -> dict:
        """Returns the Event Information as a dictionary.

        Returns:
            dict: event information dictionary
        """
        return {
            "summary": f"{self.summary}",
            "description": f"{self.description}",
            "start": {
                "dateTime": f"{self.start_date.isoformat() if self.start_date else ''}",
                "timeZone": "America/New_York",
            },
            "end": {
                "dateTime": f"{self.end_date.isoformat() if self.end_date else ''}",
                "timeZone": "America/New_York",
            },
        }

    def __str__(self) -> str:
        """Returns string representation of the event.

        Returns:
            str: Event's information.
        """
        return f"""
Summary: {self.summary}
Description: {self.description}
Start Date: {self.start_date.isoformat() if self.start_date else ""}
End Date: {self.end_date.isoformat() if self.end_date else ""}
"""


def main() -> None:
    """Unit Testing."""
    session = Session(
        title="Marshmallow Development",
        description="Intensive Refactoring",
    )

    session.begin()
    time.sleep(5)
    session.end()

    event = Event(session)
    print(event)
    event_info = event.get_event_dictionary()
    print(event_info)
    # event = Event(
    #     summary="Marshmallow Development",
    #     description="Intensive Refactoring",
    #     start_date=datetime(year=2023, month=7, day=29, hour=16),
    #     end_date=datetime(year=2023, month=7, day=29, hour=18),
    # )


if __name__ == "__main__":
    main()
