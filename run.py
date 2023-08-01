#!/usr/bin/env python

"""A module for running the google-stopwatch program.

This module is responsible for running the google-stopwatch
program. Start and stop a stopwatch and have it retroactively
logged on google calendar upon completion.

Typical usage example:

$ python run.py -t "Stopwatch Session Title" -d "Stopwatch Session Description"
"""

import argparse
import calendar_interactor as cal
from ADTs.event import Event
from ADTs.session import Session


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="google-stopwatch",
        description="A stopwatch that logs your session on google calendar.",
    )
    parser.add_argument(
        "-t",
        metavar="title",
        help="name of the session (and google calendar event)",
        required=True,
    )
    parser.add_argument(
        "-d",
        metavar="description",
        help="description of the session (and google calendar event)",
        required=True,
    )
    return parser.parse_args()


def main() -> None:
    args = get_args()
    session = Session(
        title=args.t,
        description=args.d,
    )

    session.begin()
    input("Press Enter to Stop: ")
    session.end()

    event = Event()
    event.create_event_from_session(session)

    cal.add_event(event)

    return


if __name__ == "__main__":
    main()
