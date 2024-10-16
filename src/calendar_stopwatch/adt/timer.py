"""A class representing a timer.

This module defines the timer ADT, which stores information and supports
operations relevant to logic starting and stopping a timer.

Typical usage example:

  timer = Timer()
  timer.start()
  timer.stop()
"""

import logging
from dataclasses import dataclass, field
from datetime import datetime

logger = logging.getLogger("ADTs")


@dataclass
class Timer:
    """Represents a timer."""

    start_time: datetime | None = field(init=False, default=None)
    stop_time: datetime | None = field(init=False, default=None)

    def start(self) -> None:
        """Starts the timer."""
        if self.start_time:
            logger.error("Error: Timer already started.")
            return

        self.start_time = datetime.now()
        logger.info("Started Timer.")
        return

    def stop(self) -> None:
        """Stops the timer."""
        if not self.start_time:
            logger.error("Error: Attempted stop to Timer with no start.")
            return
        if self.stop_time:
            logger.error("Error: Timer has already been stopped.")
            return

        self.stop_time = datetime.now()
        logger.info("Stopped Timer.")
        return

    def __str__(self) -> str:
        """Returns the timer duration.

        Returns:
            str: The timer's duration.
        """
        if self.start_time and self.stop_time:
            return f"{self.stop_time - self.start_time}"
        if self.start_time:
            return f"{datetime.now() - self.start_time}"
        return "timer has not yet been started."


def main() -> None:
    """Unit Testing."""
    timer = Timer()
    timer.stop()
    print(timer)
    timer.start()
    print(timer)
    timer.stop()
    print(timer)
    timer.start()
    timer.stop()


if __name__ == "__main__":
    main()
