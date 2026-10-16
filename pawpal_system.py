from dataclasses import dataclass, field
from datetime import date, time


@dataclass
class Task:
    """One care activity, such as a walk or a feeding."""

    title: str
    due_time: time
    duration_minutes: int
    priority: str
    is_done: bool = False

    def mark_done(self) -> None:
        pass


@dataclass
class Routine:
    """A named group of tasks, such as "morning care"."""

    name: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def get_tasks(self) -> list[Task]:
        pass


@dataclass
class Pet:
    """Information about one pet and the routines that care for it."""

    name: str
    species: str
    age: int
    routines: list[Routine] = field(default_factory=list)

    def add_routine(self, routine: Routine) -> None:
        pass

    def get_tasks(self) -> list[Task]:
        pass


class Schedule:
    """The daily plan shown to the owner."""

    def __init__(self, day: date) -> None:
        self.date: date = day
        self.events: list[Task] = []

    def add_event(self, task: Task) -> None:
        pass

    def get_events(self) -> list[Task]:
        pass

    def show_calendar(self) -> None:
        pass
