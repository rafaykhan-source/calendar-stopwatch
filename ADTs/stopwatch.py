"""A class representing a StopWatch.

This module defines the StopWatch ADT, which stores information and supports 
operations relevant to logic starting and stopping a stopwatch.

Typical usage example:

  stopwatch = StopWatch()
  stopwatch.start()
  stopwatch.stop()
"""

from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class StopWatch:
    def __init__(self) -> None:
        self.start_time: datetime = None
        "The start date and time of the StopWatch"
        self.stop_time: datetime = None
        "The stop date and time of the StopWatch"
        return

    def start(self) -> None:
        """Starts the StopWatch."""
        if self.start_time:
            logger.error("Error: StopWatch has already been started.")
            return

        self.start_time = datetime.now()
        return

    def stop(self) -> None:
        """Stops the StopWatch."""
        if not self.start_time:
            logger.error("Error: Cannot stop StopWatch that has not been started.")
            return
        if self.stop_time:
            logger.error("Error: StopWatch has already been stopped.")
            return

        self.stop_time = datetime.now()
        return

    def __str__(self) -> str:
        if self.start_time and self.stop_time:
            return f"{self.stop_time - self.start_time}"
        if self.start_time:
            return f"{datetime.now() - self.start_time}"
        return "StopWatch has not yet been started."


def main() -> None:
    stopwatch = StopWatch()
    stopwatch.stop()
    print(stopwatch)
    stopwatch.start()
    print(stopwatch)
    stopwatch.stop()
    print(stopwatch)
    stopwatch.start()
    stopwatch.stop()
    return


if __name__ == "__main__":
    main()
