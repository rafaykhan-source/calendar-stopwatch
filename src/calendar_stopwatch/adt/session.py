"""A class representing a Session.

This module defines the Session ADT, which stores information and supports
operations relevant to logic associated with a timed session.

Typical usage example:

  session = Session()
  session.begin()
  session.end()
"""

import logging
import time
from dataclasses import dataclass, field
from datetime import datetime

from adt.timer import Timer

logger = logging.getLogger("ADTs")


@dataclass
class Session:
    """This class wraps information pertaining to a timer session."""

    title: str
    description: str
    __timer: Timer = field(init=False, default_factory=Timer)
    __began: bool = field(init=False, repr=False, default=False)
    __ended: bool = field(init=False, repr=False, default=False)

    def begin(self) -> None:
        """Begins the Session."""
        if self.__began:
            logger.error("Error: Cannot begin session that has already begun.")
            return
        self.__began = True
        self.__timer.start()
        logger.info("Session has begun.")
        return

    def end(self) -> None:
        """Ends the session."""
        if not self.__began:
            logger.error("Error: Cannot end session that has not yet begun.")
            return
        if self.__ended:
            logger.error("Error: Cannot end session that has already ended.")
            return
        self.__ended = True
        self.__timer.stop()
        logger.info("Session has ended.")
        return

    def get_duration(self) -> str:
        """Returns the duration of the session.

        Returns:
            str: duration of the session
        """
        return str(self.__timer)

    def is_complete(self) -> bool:
        """Returns whether session is complete.

        Returns:
            bool: Whether session is completed.
        """
        return self.__began and self.__ended

    def get_time_range(self) -> tuple[datetime | None, datetime | None]:
        """Returns the start and end datetimes if complete.

        Returns None if session is incomplete.

        Returns:
            tuple[datetime]: start and end datetimes
        """
        if not self.is_complete():
            logger.error("Error: Session is incomplete.")
            return (None, None)
        return (self.__timer.start_time, self.__timer.stop_time)

    def __str__(self) -> str:
        """Returns a string representation of the session.

        Returns:
            str: Session's information.
        """
        return f"""
Title: {self.title}
Description: {self.description}
Duration: {self.get_duration()}
"""


def main() -> None:
    """Unit Testing."""
    session = Session(
        title="Marshmallow Development",
        description="Doing Intensive Refactoring",
    )
    session.end()
    print(session)
    session.begin()
    print(session)
    time.sleep(5)
    session.end()
    print(session)
    session.begin()
    session.end()
    print(str(session.get_time_range()) + ": " + session.get_duration())


if __name__ == "__main__":
    main()
