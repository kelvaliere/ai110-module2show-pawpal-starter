# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Short Implementation Summary
With the help of Claude, this app is a Python-based tool that allows for pet owners to manage their pet schedule.

First, we can start by initializing an object of the `Owner` class, and then some pets using the `Pet` class. Owner has a method named `add_pet()` to be able to connect `Pet`s to `Owner`s.

Then for pets, there is a class named `Task`, with the first parameter as the task name, and the second paramter using `datatime` as the time of day (in 24hr/military time). The user can then set tasks to pets using the `add_task()`.

Finally, there is a `Scheduler` class that takes an `Owner` parameter, and the `show_plan()` method will export a daily brief on the tasks that need to be accomplished.


## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```zsh
Daily plan for Kelvin
  [ ] 08:00 Bathe (Meow, 15 min, medium, daily)
  [ ] 12:00 Feed (Arf, 15 min, medium, daily)
  [ ] 13:00 Go on a walk (Arf, 15 min, medium, daily)
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
.venv ❯ pytest
================================================================ test session starts ================================================================
platform darwin -- Python 3.15.0, pytest-9.1.1, pluggy-1.7.0
rootdir: /Users/kelvin/f2026/codepath/ai110-module2show-pawpal-starter
plugins: anyio-4.15.1
collected 0 items                                                                                                                                   

=============================================================== no tests ran in 0.01s ===============================================================

# Run with coverage:
.venv ❯ pytest --cov
================================================================ test session starts ================================================================
platform darwin -- Python 3.15.0, pytest-9.1.1, pluggy-1.7.0
rootdir: /Users/kelvin/f2026/codepath/ai110-module2show-pawpal-starter
configfile: ov
plugins: anyio-4.15.1
collected 0 items                                                                                                                                   

=============================================================== no tests ran in 0.01s ===============================================================

```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | collecting every task from each pet, and returns the earliest first | by time, `task.start` combines the due date and due time together to be compared |
| Filtering | returns tasks in timed order, with filters passed | filters like `pet_name=""` or `is_done=""` are based on which pet, or what type of completion |
| Conflict handling | returns list of warnings, if empty it has no errors | checking for tasks that may collide, when there is more than one task |
| Recurring tasks | returns copy of task for next period, otherwise none | can be set weekly or daily, from `_REPEAT_STEP` |

# Features

- **Sorting by time:** `Scheduler.sort_by_time()` gathers every task from every pet and orders them by start date and time (`Task.start`). When two tasks start at the same moment, the higher priority comes first (high, then medium, then low). An unrecognized priority is treated as medium. Tasks on different dates sort by date first, so tomorrow's 08:00 comes after today's 23:00.
- **Filtering:** `Scheduler.filter_tasks()` keeps tasks by pet name, by completion status, or both. A filter left as `None` is ignored. Results stay in time order.
- **Conflict warnings:** `Scheduler.find_conflicts()` groups pending tasks by exact start date and time and returns one warning for each time shared by two or more tasks. It catches clashes for the same pet and across different pets. Finished tasks are ignored. It compares start times only, not durations, so a 30-minute task at 08:00 and another at 08:15 are not flagged.
- **Daily and weekly recurrence:** `Pet.complete_task()` marks a task done and adds a fresh, not-done copy due one day later (`daily`) or seven days later (`weekly`). `once` tasks do not repeat.
- **Daily plan:** `Scheduler.show_plan()` prints all tasks in time order with their status, pet, duration, priority and frequency, followed by any conflict warnings.

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. The goal is this app is to set tasks for pets and create a schedule plan around those tasks.
2. First, enter in the `Owner`'s name, for example, your name in the `Owner name` field, and details about your pet. You can always add more pets.
3. After adding your pets, select which pet for the task, and add the task title and the time (in 24-hr format).
4. Your schedule should automatically update in a table for you to view, provided that you add tasks.