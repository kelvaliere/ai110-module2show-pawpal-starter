from collections import defaultdict
from dataclasses import dataclass, field, replace
from datetime import date, datetime, time, timedelta


@dataclass
class Task:
    """A single care activity, such as a walk or a feeding."""

    description: str
    due_time: time
    frequency: str = "daily"  # "once", "daily", or "weekly"
    duration_minutes: int = 15
    priority: str = "medium"  # "low", "medium", or "high"
    pet_name: str = ""  # set by Pet.add_task()
    is_done: bool = False
    due_date: date = field(default_factory=date.today)

    _REPEAT_STEP = {"daily": timedelta(days=1), "weekly": timedelta(weeks=1)}

    @property
    def start(self) -> datetime:
        """The moment this task is due, combining its date and time."""
        return datetime.combine(self.due_date, self.due_time)

    def mark_done(self) -> None:
        self.is_done = True

    def next_occurrence(self) -> "Task | None":
        """Return a fresh copy of this task for its next occurrence.

        The copy keeps every field but is not done, and its due date moves
        forward by one period: 1 day for "daily", 7 days for "weekly". A
        "once" task (or any other frequency) does not repeat, so this returns
        None.

        Example: a daily task due 10/20 gives a new task due 10/21.
        """
        step = self._REPEAT_STEP.get(self.frequency)
        if step is None:
            return None
        return replace(self, is_done=False, due_date=self.due_date + step)


@dataclass
class Pet:
    """Stores pet details and the list of tasks for that pet."""

    name: str
    species: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        task.pet_name = self.name
        self.tasks.append(task)

    def complete_task(self, task: Task) -> None:
        """Mark a task done and add its next occurrence if it repeats.

        Call this instead of task.mark_done() when the task belongs to a pet.
        A Task cannot add itself to a pet's list, so the pet does it here.
        """
        task.mark_done()
        next_task = task.next_occurrence()
        if next_task is not None:
            self.add_task(next_task)

    def get_tasks(self) -> list[Task]:
        return list(self.tasks)


@dataclass
class Owner:
    """Manages several pets and gives one view of all their tasks."""

    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)

    def get_all_tasks(self) -> list[Task]:
        """Return every pet's tasks together."""
        return [task for pet in self.pets for task in pet.get_tasks()]


class Scheduler:
    """Retrieves, organizes, and manages tasks across all of an owner's pets.

    It reads tasks only through Owner.get_all_tasks(), never from a Pet directly.
    """

    _PRIORITY_RANK = {"high": 0, "medium": 1, "low": 2}

    def __init__(self, owner: Owner) -> None:
        self.owner: Owner = owner

    def sort_by_time(self) -> list[Task]:
        """Return every task, earliest first.

        Python compares the sort key (start, priority rank) from left to
        right. Tasks are ordered by start date and time. If two tasks start
        together, the lower priority rank comes first (high=0, medium=1,
        low=2). An unknown priority is treated as medium.
        """
        return sorted(
            self.owner.get_all_tasks(),
            key=lambda t: (t.start, self._PRIORITY_RANK.get(t.priority, 1)),
        )

    def filter_tasks(
        self, pet_name: str | None = None, is_done: bool | None = None
    ) -> list[Task]:
        """Return tasks in time order, keeping only those that match each filter given.

        A filter left as None is ignored, so both can be combined.

        Examples:
            filter_tasks(pet_name="Arf")               all of Arf's tasks
            filter_tasks(is_done=False)                every pending task
            filter_tasks(pet_name="Arf", is_done=True) Arf's finished tasks
        """
        return [
            task
            for task in self.sort_by_time()
            if (pet_name is None or task.pet_name == pet_name)
            and (is_done is None or task.is_done == is_done)
        ]

    def find_conflicts(self) -> list[str]:
        """Return one warning per start time shared by two or more pending tasks.

        How it works:
            1. Take the pending tasks (finished tasks cannot conflict).
            2. Group them by exact start date and time.
            3. Write one warning for each group that has more than one task.

        The check covers tasks for the same pet and for different pets. It
        compares start times only, not durations, so a 30-minute task at 08:00
        and another at 08:15 are not flagged. It never raises an error: no
        conflict gives an empty list.
        """
        tasks_by_start = defaultdict(list)
        for task in self.filter_tasks(is_done=False):
            tasks_by_start[task.start].append(task)

        return [
            f"Warning: {start:%m/%d %H:%M} has {len(tasks)} tasks: "
            + ", ".join(f"{t.description} ({t.pet_name})" for t in tasks)
            for start, tasks in tasks_by_start.items()
            if len(tasks) > 1
        ]

    def show_plan(self) -> None:
        """Print today's tasks in time order."""
        tasks = self.sort_by_time()
        print(f"Daily plan for {self.owner.name}")
        if not tasks:
            print("  (no tasks)")
        for task in tasks:
            mark = "x" if task.is_done else " "
            print(
                f"  [{mark}] {task.start:%m/%d %H:%M} {task.description} "
                f"({task.pet_name}, {task.duration_minutes} min, "
                f"{task.priority}, {task.frequency})"
            )
        for warning in self.find_conflicts():
            print(f"  {warning}")
