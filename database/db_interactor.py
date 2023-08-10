"""This module is responsible for handling database interactions.

This module should hold several functions related to data production
and consumption.
"""

import logging
import sqlite3

from ADTs import Session

# logger = logging.getLogger("database")


def __get_cursor() -> sqlite3.Cursor:
    """Connect to the database and retrieve the cursor."""
    con = sqlite3.connect("session-history.sqlite")
    return con.cursor()

def adapt_session(session: Session) -> str:
    return f"{session.title};{session.description};{session.get_session_time_range()}"

def main() -> None:
    """Unit Testing."""
    cur = __get_cursor()

    cur.execute(
        "CREATE TABLE sessions(title, description, start_time, end_time, posted)"
    )

    res = cur.execute("SELECT name from sqlite_schema")
    print(res.fetchone())

    return


if __name__ == "__main__":
    main()
