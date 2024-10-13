"""This package contains ADTs relevant to running the stopwatch program.

The session and event ADT contain information for creating a google calendar
event and hosting a stopwatch session.
"""

from .event import Event
from .session import Session

__all__ = ["Event", "Session"]
