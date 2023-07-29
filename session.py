"""A class representing a Session.

This module defines the Session ADT, which stores information and supports 
operations relevant to logic associated utilizing a StopWatch and information
of why a User needs the use the stopwatch.

Typical usage example:

  session = Session()
  session.begin()
  session.end()
"""


class Session:
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description
        self.__began = False
        self.__ended = False
        return

    def begin(self) -> None:
        if self.__began:
            print("Error: Cannot begin Session that has already begun.")
            return
        self.__began = True
        # TODO: Implement a Begin Functionality
        return

    def end(self) -> None:
        if not self.__began:
            print("Error: Cannot end Session that has not yet begun.")
            return
        if self.__ended:
            print("Error: Cannot end Session that has already ended.")
            return
        self.__ended = True
        # TODO: Implement a End Functionality
        return

    def __str__(self) -> str:
        return ""


def main() -> None:
    # TODO: Add Unit Testing
    return


if __name__ == "__main__":
    main()
