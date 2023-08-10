"""This module is responsible for handling database interactions.

This module should hold several functions related to data production
and consumption.
"""

import sys
import logging
import sqlite3
from datetime import datetime

sys.path.append("./")
from ADTs import Session

# logger = logging.getLogger("database")


def create_sessions_table() -> None:
    """Creates sessions table if it doesn't already exist."""
    con = sqlite3.connect("database/session-history.sqlite")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS sessions(id INTEGER PRIMARY KEY, title TEXT, description TEXT, start TIMESTAMP, end TIMESTAMP, posted NUMERIC)"
    )
    con.close()
    return


def add_session(session: Session, posted: bool) -> None:
    params = extract_params_from_session(session, posted)

    con = sqlite3.connect("database/session-history.sqlite")
    with con:
        con.execute(
            "INSERT INTO sessions (title, description, start, end, posted) VALUES (?, ?, ?, ?, ?)",
            params,
        )
    con.close()
    return


def extract_params_from_session(
    session: Session, posted: bool
) -> tuple[str, str, datetime, datetime, bool]:
    """Extracts parameters for sqlite query from session.

    Client should also provide whether event has been posted or not.

    Args:
        session (Session): Completed session.
        posted (bool): Whether event has been posted or not.

    Returns:
        tuple[str, str, datetime, datetime, bool]: params
    """
    start, end = session.get_session_time_range()
    params = (session.title, session.description, start, end, posted)
    return params


def main() -> None:
    """Unit Testing."""
    create_sessions_table()
    # con = sqlite3.connect("database/session-history.sqlite")
    # cur = con.cursor()
    # with con:
    #     con.execute("DROP TABLE IF EXISTS sessions")
    # cur = con.cursor()
    # cur.execute("SELECT name FROM sqlite_schema")
    # print(cur.fetchone())
    # row = cur.fetchone()
    # print(row[0], type(row[0]))
    # print(row[1], type(row[1]))
    # print(row[2], type(row[2]))
    # print(row[3], type(row[3]))
    # print(row[4], type(row[4]))
    # con.close()
    return


if __name__ == "__main__":
    main()
