"""A class representing a Google Calendar Event.

This module defines the Event ADT, which wraps the Google Calendar Event.

Typical usage example:

  event = Event()
"""

from datetime import datetime

class Event:
    def __init__(
        self,
        summary: str,
        description: str,
        start_date: datetime,
        end_date: datetime,
    ) -> None:
        self.event = {
            "summary": f"{summary}",
            "description": f"{description}",
            "start": {
                "dateTime": f"{start_date.isoformat()}",
                "timeZone": "America/New_York",
            },
            "end": {
                "dateTime": f"{end_date.isoformat()}",
                "timeZone": "America/New_York",
            },
        }
        return

    def get_event_dictionary(self) -> dict:
        """Returns the Event Information as a dictionary.

        Returns:
            dict: event information dictionary
        """
        return self.event

    def __str__(self):
        return str(self.event)


def main() -> None:
    event = Event(
        summary="Marshmallow Development",
        description="Intensive Refactoring",
        start_date=datetime(year=2023, month=7, day=29, hour=16),
        end_date=datetime(year=2023, month=7, day=29, hour=18),
    )
    event_info = event.get_event_dictionary()
    for key, value in event_info.items():
        print(key, value)
    print(event)
    return


if __name__ == "__main__":
    main()
