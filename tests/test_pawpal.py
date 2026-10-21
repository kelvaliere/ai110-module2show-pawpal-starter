from datetime import date, time

from pawpal_system import Owner, Pet, Scheduler, Task


def test_mark_done_changes_task_status():
    task = Task("Feed", time(12, 0))
    assert task.is_done is False

    task.mark_done()

    assert task.is_done is True


def test_add_task_increases_pet_task_count():
    pet = Pet("Arf", "dog", 4)
    assert len(pet.get_tasks()) == 0

    pet.add_task(Task("Feed", time(12, 0)))

    assert len(pet.get_tasks()) == 1


def test_sort_by_time_orders_tasks_across_pets_with_priority_tiebreak():
    owner = Owner("Kelvin")
    dog = Pet("Arf", "dog", 4)
    cat = Pet("Mia", "cat", 2)
    owner.add_pet(dog)
    owner.add_pet(cat)
    dog.add_task(Task("Walk", time(18, 0)))
    dog.add_task(Task("Breakfast", time(8, 0), priority="low"))
    cat.add_task(Task("Meds", time(8, 0), priority="high"))

    result = [t.description for t in Scheduler(owner).sort_by_time()]

    assert result == ["Meds", "Breakfast", "Walk"]


def test_filter_tasks_by_pet_and_completion_status():
    owner = Owner("Kelvin")
    dog = Pet("Arf", "dog", 4)
    cat = Pet("Mia", "cat", 2)
    owner.add_pet(dog)
    owner.add_pet(cat)
    walk = Task("Walk", time(18, 0))
    feed = Task("Feed", time(8, 0))
    meds = Task("Meds", time(9, 0))
    dog.add_task(walk)
    dog.add_task(feed)
    cat.add_task(meds)
    feed.mark_done()
    scheduler = Scheduler(owner)

    assert scheduler.filter_tasks() == [feed, meds, walk]
    assert scheduler.filter_tasks(pet_name="Arf") == [feed, walk]
    assert scheduler.filter_tasks(is_done=False) == [meds, walk]
    assert scheduler.filter_tasks(pet_name="Arf", is_done=False) == [walk]


def test_completing_recurring_task_creates_next_occurrence():
    pet = Pet("Arf", "dog", 4)
    daily = Task("Walk", time(18, 0), frequency="daily", due_date=date(2026, 10, 20))
    weekly = Task("Bath", time(10, 0), frequency="weekly", due_date=date(2026, 10, 20))
    once = Task("Vet", time(9, 0), frequency="once", due_date=date(2026, 10, 20))
    for task in (daily, weekly, once):
        pet.add_task(task)

    for task in (daily, weekly, once):
        pet.complete_task(task)

    assert len(pet.get_tasks()) == 5  # daily and weekly each added one; once did not
    new_daily, new_weekly = pet.get_tasks()[3:]
    assert (new_daily.description, new_daily.due_date) == ("Walk", date(2026, 10, 21))
    assert (new_weekly.description, new_weekly.due_date) == ("Bath", date(2026, 10, 27))
    assert not new_daily.is_done and new_daily.pet_name == "Arf"


def test_find_conflicts_warns_for_same_pet_and_different_pets():
    owner = Owner("Kelvin")
    dog = Pet("Arf", "dog", 4)
    cat = Pet("Mia", "cat", 2)
    owner.add_pet(dog)
    owner.add_pet(cat)
    d = date(2026, 10, 21)
    dog.add_task(Task("Walk", time(8, 0), due_date=d))
    dog.add_task(Task("Feed", time(8, 0), due_date=d))  # same pet
    cat.add_task(Task("Meds", time(9, 0), due_date=d))
    dog.add_task(Task("Play", time(9, 0), due_date=d))  # different pets
    done = Task("Bath", time(10, 0), due_date=d)
    dog.add_task(done)
    cat.add_task(Task("Brush", time(10, 0), due_date=d))
    done.mark_done()  # finished task should not conflict
    cat.add_task(Task("Nap", time(11, 0), due_date=d))

    warnings = Scheduler(owner).find_conflicts()

    assert len(warnings) == 2
    assert "08:00" in warnings[0] and "Walk (Arf)" in warnings[0] and "Feed (Arf)" in warnings[0]
    assert "09:00" in warnings[1] and "Meds (Mia)" in warnings[1] and "Play (Arf)" in warnings[1]


def test_find_conflicts_returns_empty_list_when_no_overlap():
    owner = Owner("Kelvin")
    dog = Pet("Arf", "dog", 4)
    owner.add_pet(dog)
    dog.add_task(Task("Walk", time(8, 0)))
    dog.add_task(Task("Feed", time(9, 0)))

    assert Scheduler(owner).find_conflicts() == []
