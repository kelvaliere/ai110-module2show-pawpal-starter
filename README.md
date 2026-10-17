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
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```zsh
================================================= test session starts ==================================================
platform darwin -- Python 3.15.0, pytest-9.1.1, pluggy-1.7.0
rootdir: /Users/kelvin/f2026/codepath/ai110-module2show-pawpal-starter
plugins: anyio-4.15.1
collected 2 items                                                                                                      

tests/test_pawpal.py ..                                                                                          [100%]

================================================== 2 passed in 0.01s ===================================================
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | | e.g., by priority, duration |
| Filtering | | e.g., skip tasks if time runs out |
| Conflict handling | | e.g., overlapping time slots |
| Recurring tasks | | e.g., daily vs. weekly |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
