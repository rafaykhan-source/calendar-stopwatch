import argparse
import calendar_interactor as cal
from event import Event
from session import Session


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="google-stopwatch",
        description="A stopwatch that logs your session on google calendar.",
    )
    parser.add_argument(
        "-t",
        help="name of the session (and google calendar event)",
        metavar="title",
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
        title=args.title,
        description=args.description,
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
