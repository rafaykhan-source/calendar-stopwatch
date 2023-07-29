"""A class representing a StopWatch.

This module defines the StopWatch ADT, which stores information and supports 
operations relevant to logic starting and stopping a stopwatch.

Typical usage example:

  stopwatch = StopWatch()
  stopwatch.start()
  stopwatch.stop()
"""


class StopWatch:
    def __init__(self) -> None:
        self.__started = False
        self.__stopped = False
        return

    def start(self) -> None:
        if self.__started:
            print("Error: StopWatch has already been started.")
            return

        self.__started = True
        # TODO: Implement a Start Functionality
        return

    def stop(self) -> None:
        if not self.__started:
            print("Error: Cannot stop StopWatch that has not been started.")
            return
        if self.__stopped:
            print("Error: StopWatch has already been stopped.")
            return

        self.__stopped = True
        # TODO: Implement a Stop Functionality
        return

    def __str__(self) -> str:
        return ""


def main() -> None:
    # TODO: Add Unit Testing
    return


if __name__ == "__main__":
    main()
