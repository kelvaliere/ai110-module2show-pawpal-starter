from datetime import time

from pawpal_system import Pet, Task


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
