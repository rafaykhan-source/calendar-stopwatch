#!/usr/bin/env python

"""A module for running the google-stopwatch program.

This module is responsible for running the google-stopwatch
program. Start and stop a stopwatch and have it retroactively
logged on google calendar upon completion.

Typical usage example:

$ python run.py -t "Stopwatch Session Title" -d "Stopwatch Session Description"
"""

import argparse
import logging
import logging.config
from config import settings as stg
import calendar_interactor as cal
from ADTs.event import Event
from ADTs.session import Session

logger = logging.getLogger(__name__)

def __configure_logging() -> None:

    config = stg.get_logging_config()
    logging.config.dictConfig(config)

    return

# TODO: make get_args private
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
    __configure_logging()
    
    args = get_args()
    logger.info("Retrieved command-line arguments.")

    session = Session(
        title=args.t,
        description=args.d,
    )

    session.begin()
    input("Press Enter to Stop Session: ")
    logger.info("User requested session stop.")
    session.end()

    event = Event()
    event.create_event_from_session(session)

    cal.add_event(event)

    return


if __name__ == "__main__":
    main()
