"""A class storing Google Calendar Event information.

This module defines the Event ADT, which wraps the information relevant
to a google calendar event.

Typical usage example:

  event = Event()
  event_info = event.get_event_dictionary()
"""

import logging
import time
from dataclasses import InitVar, dataclass
from datetime import datetime

from adt.session import Session

logger = logging.getLogger("ADTs")


@dataclass
class Event:
    """This class wraps information pertaining to a google calendar event."""

    summary: str = ""
    description: str = ""
    start_date: datetime | None = None
    end_date: datetime | None = None
    session: InitVar[Session | None] = None

    def __post_init__(self, session: Session | None) -> None:
        """Initializes an event from a session.

        Args:
            session (Session | None): The session to intialize an event from.
        """
        if session:
            self.summary = session.title
            self.description = (
                session.description + f"Duration: {session.get_duration()}"
            )
            self.start_date, self.end_date = session.get_time_range()

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

    event = Event(session=session)
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
