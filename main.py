from datetime import time
from pawpal_system import Task, Pet, Owner, Scheduler

owner = Owner('Kelvin')
dog = Pet('Arf', 'dog', 4)
cat = Pet('Meow', 'cat', 2)

owner.add_pet(dog)
owner.add_pet(cat)


feed = Task('Feed', time(20, 0))
walk = Task('Go on a walk', time(3, 0))

dog.add_task(feed)
dog.add_task(walk)

bathe = Task('Bathe', time(5, 0))
cat.add_task(bathe)

# Same start time as the dog's "Feed" task, so the scheduler should warn.
meds = Task('Give meds', time(20, 0))
cat.add_task(meds)

print(owner.get_all_tasks())

scheduler = Scheduler(owner)
scheduler.show_plan()

'''
tested output:

Daily plan for Kelvin
  [ ] 10/21 03:00 Go on a walk (Arf, 15 min, medium, daily)
  [ ] 10/21 05:00 Bathe (Meow, 15 min, medium, daily)
  [ ] 10/21 20:00 Feed (Arf, 15 min, medium, daily)
  [ ] 10/21 20:00 Give meds (Meow, 15 min, medium, daily)
  Warning: 10/21 20:00 has 2 tasks: Feed (Arf), Give meds (Meow)
'''