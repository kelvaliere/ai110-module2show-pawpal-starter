# PawPal+ Project Reflection

## 1. System Design

For my PawPal project, I want the user to be able to add a couple of pets to manage, show the tasks for the day, and show the schedule for the owner.

> **Attributes:**
> - It should hold information about the pets, tasks maybe in an index of some sort (list?), the times for each task/schedule event, and the schedule itself.
>
> **Methods:**
> - It should be able to add pets, add events, store schedule events, show the tasks and events, and show the event calendar.


**Classes**
- **Pet**: holds information about one pet.
  - Attributes: `name`, `species`, `age`, `routines`
  - Methods: `add_routine()`, `get_tasks()`
- **Task**: one care activity, such as a walk or a feeding.
  - Attributes: `title`, `due_time`, `duration_minutes`, `priority`, `pet_name`, `is_done`
  - Methods: `mark_done()`
- **Routine**: a group of tasks, such as "morning care".
  - Attributes: `name`, `tasks`
  - Methods: `add_task()`, `get_tasks()`
- **Schedule**: the daily plan shown to the owner.
  - Attributes: `date`, `events`
  - Methods: `add_event()`, `add_routine()`, `get_events()`, `show_calendar()`

(authored by Claude)

**a. Initial design**

- Briefly describe your initial UML design.

My UML design has a `Pet` that you insert to let the system know which `Pet` should have which `Routine`. Then, the `Routines` and `Tasks` are connected to the `Schedule`.

- What classes did you include, and what responsibilities did you assign to each?

I decided on `Pet`, `Task`, `Routines`, and `Schedule` for the classes I wanted to include. I believed that the individual `Task` would be beneficial as it could be included into a `Schedule`.

I also wanted to add `Routines` as a recurring class that can add onto `Schedule`.

**b. Design changes**

- Did your design change during implementation?

Yes.

- If yes, describe at least one change and why you made it.

I wanted to make a daily refresh so that each day would have its schedule. I'm not sure if the data would carry over to the next day, so I added this constraint so it would not pile up previous events and todos.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?

I used Claude to brainstorm the Mermaid diagram, make test cases in `test_pawpal.py`, and flesh out the PawPal system, according to assignment guidelines. I did try to write `main.py` on my own, but I am still not that great at Python, so I asked Claude to tutor me a bit on how to call these classes.

Thankfully, since I'm learning basic C++ object-oriented programming in university, the classes were straightforward, but I had to ask it what the parameters and `self` meant.

- What kinds of prompts or questions were most helpful?

I've downloaded a skill someone made called `socratic-tutor` to help me learn or break down some of these confusing Python topics, and also how the codebase itself works.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

I think I did not accept some suggestions because I did not know how these things worked. It would be bad to just have arbitrary code without me knowing what it does, so I asked it to explain it to me, and I briefly looked over it.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
