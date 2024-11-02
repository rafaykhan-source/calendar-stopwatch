"""A module for running the calendar-stopwatch program.

This module is responsible for running the calendar-stopwatch
program. Start and stop a session and have it retroactively
logged to your calendar upon completion.
"""

import argparse
import logging
import logging.config

import calendar_interactor as cal
import database.db_interactor as db
from adt import Event, Session
from config.settings import get_logging_config

logger = logging.getLogger("run")


def __configure_logging() -> None:
    """Configures logging for the program."""
    config = get_logging_config()
    logging.config.dictConfig(config)


def __get_args() -> argparse.Namespace:
    """Returns arguments User supplied to program.

    Returns:
        argparse.Namespace: User args with named attributes.
    """
    parser = argparse.ArgumentParser(
        prog="calendar-stopwatch",
        description="A stopwatch that logs your session on calendar.",
    )
    parser.add_argument(
        "title",
        help="name of the session (and calendar event)",
    )
    parser.add_argument(
        "-d",
        metavar="description",
        help="description of the session (and calendar calendar event)",
        default="",
        required=False,
        dest="description",
    )
    return parser.parse_args()


def main() -> None:
    """Runs the calendar-stopwatch program."""
    __configure_logging()
    logger.info("Configured logging.")

    args = __get_args()
    logger.info("Retrieved command-line arguments.")

    session = Session(
        title=args.title,
        description=args.description,
    )

    session.begin()
    input("Press Enter to Stop Session: ")
    logger.info("User requested session stop.")
    session.end()

    event = Event(session=session)
    cal.add_event(event)
    db.add_session(session)


main()
