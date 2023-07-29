import calendar_interactor as cal
from event import Event
from session import Session


def main() -> None:
    session = Session(
        title="Marshmallow Development",
        description="Intensive Refactoring",
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
