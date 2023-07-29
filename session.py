"""A class representing a Session.

This module defines the Session ADT, which stores information and supports 
operations relevant to logic associated utilizing a StopWatch and information
of why a client needs the use the stopwatch.

Typical usage example:

  session = Session()
  session.begin()
  session.end()
"""

from datetime import datetime
from stopwatch import StopWatch


class Session:
    def __init__(self, title: str, description: str) -> None:
        self.title: str = title
        "A general title for the timed session."
        self.description: str = description
        "A description for the session."
        self.stopwatch: StopWatch = StopWatch()
        "A stopwatch for the session."
        self.__began: bool = False
        "Whether the session has begun."
        self.__ended: bool = False
        "Whether the session has ended."
        return

    def begin(self) -> None:
        """Begins the Session."""
        if self.__began:
            print("Error: Cannot begin Session that has already begun.")
            return
        self.__began = True
        self.stopwatch.start()
        return

    def end(self) -> None:
        """Ends the session."""
        if not self.__began:
            print("Error: Cannot end Session that has not yet begun.")
            return
        if self.__ended:
            print("Error: Cannot end Session that has already ended.")
            return
        self.__ended = True
        self.stopwatch.stop()
        return

    def get_session_time_range(self) -> tuple[datetime]:
        """Returns the start and end datetimes.

        Returns:
            tuple[datetime]: start and end datetimes
        """
        return (self.stopwatch.start_time, self.stopwatch.stop_time)

    def __str__(self) -> str:
        return f"""
Title: {self.title}
Description: {self.description}
Duration: {self.stopwatch}
"""


def main() -> None:
    session = Session(
        title="Marshmallow Development", description="Doing Intensive Refactoring"
    )
    print(session)
    session.begin()
    print(session)
    session.end()
    print(session)
    print(session.get_session_time_range())
    return


if __name__ == "__main__":
    main()
