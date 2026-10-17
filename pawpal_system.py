from dataclasses import dataclass, field
from datetime import time


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

    def mark_done(self) -> None:
        self.is_done = True


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

    def get_sorted_tasks(self) -> list[Task]:
        """Return all tasks by due time, with higher priority first on ties."""
        return sorted(
            self.owner.get_all_tasks(),
            key=lambda t: (t.due_time, self._PRIORITY_RANK.get(t.priority, 1)),
        )

    def get_pending_tasks(self) -> list[Task]:
        return [task for task in self.get_sorted_tasks() if not task.is_done]

    def get_tasks_for_pet(self, pet_name: str) -> list[Task]:
        return [task for task in self.get_sorted_tasks() if task.pet_name == pet_name]

    def show_plan(self) -> None:
        """Print today's tasks in time order."""
        tasks = self.get_sorted_tasks()
        print(f"Daily plan for {self.owner.name}")
        if not tasks:
            print("  (no tasks)")
        for task in tasks:
            mark = "x" if task.is_done else " "
            print(
                f"  [{mark}] {task.due_time:%H:%M} {task.description} "
                f"({task.pet_name}, {task.duration_minutes} min, "
                f"{task.priority}, {task.frequency})"
            )
