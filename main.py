from datetime import time
from pawpal_system import Task, Pet, Owner, Scheduler

owner = Owner('Kelvin')
dog = Pet('Arf', 'dog', 4)
cat = Pet('Meow', 'cat', 2)

owner.add_pet(dog)
owner.add_pet(cat)


feed = Task('Feed', time(12, 0))
walk = Task('Go on a walk', time(13, 0))

dog.add_task(feed)
dog.add_task(walk)

bathe = Task('Bathe', time(8, 0))
cat.add_task(bathe)

print(owner.get_all_tasks())

scheduler = Scheduler(owner)
scheduler.show_plan()
