from pawpal_system import Task, Pet, Owner, Scheduler

def test_task_completion():
    task = Task(taskName="Feed", priority=1, duration=0.5, preference=1)
    assert not task.completed
    task.mark_complete()
    assert task.completed

def test_pet_task_addition():
    pet = Pet(petName="Fido")
    initial_count = len(pet.taskList)
    task = Task(taskName="Walk", priority=2, duration=1.0, preference=2)
    pet.add_task(task)
    assert len(pet.taskList) == initial_count + 1
    assert task in pet.taskList

def test_daily_task_not_marked_complete():
    task = Task(taskName="Feed", priority=1, duration=10, preference=1, frequency="daily")
    task.mark_complete()
    assert not task.completed, "Daily task should not be marked as complete."

def test_task_sorting():
    t1 = Task(taskName="A", priority=2, duration=30, preference=1)
    t2 = Task(taskName="B", priority=1, duration=20, preference=2)
    t3 = Task(taskName="C", priority=1, duration=10, preference=1)
    t4 = Task(taskName="D", priority=3, duration=5, preference=3)
    sorted_tasks = Scheduler.sort_tasks_by_time_and_priority([t1, t2, t3, t4])
    sorted_names = [t.taskName for t in sorted_tasks]
    assert sorted_names == ["C", "B", "A", "D"], f"Tasks not sorted correctly: {sorted_names}"

def test_sort_scheduled_by_priority_and_preference():
    t1 = Task(taskName="A", priority=2, duration=30, preference=3)
    t2 = Task(taskName="B", priority=2, duration=20, preference=1)
    t3 = Task(taskName="C", priority=1, duration=10, preference=2)
    t4 = Task(taskName="D", priority=1, duration=5, preference=1)
    sorted_tasks = Scheduler.sort_scheduled_by_priority_and_preference([t1, t2, t3, t4])
    sorted_names = [t.taskName for t in sorted_tasks]
    assert sorted_names == ["D", "C", "B", "A"], f"Tasks not sorted correctly: {sorted_names}"

def test_add_pet_to_owner():
    owner = Owner(ownerName="Jordan", startAvailability="08:00", endAvailability="10:00")
    pet1 = Pet(petName="Mochi")
    pet2 = Pet(petName="Luna")
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    assert pet1 in owner.petList and pet2 in owner.petList
    assert len(owner.petList) == 2

def test_owner_time_constraint_computed():
    owner = Owner(ownerName="Jordan", startAvailability="08:00", endAvailability="10:00")
    assert owner.timeConstraint == 2.0

def test_owner_time_constraint_overnight():
    owner = Owner(ownerName="Jordan", startAvailability="22:00", endAvailability="02:00")
    assert owner.timeConstraint == 4.0



def test_schedule_for_owner():
    # Owner has 2 hours = 120 minutes
    owner = Owner(ownerName="Test", startAvailability="09:00", endAvailability="11:00")
    pet = Pet(petName="Rex")
    owner.add_pet(pet)

    task1 = Task(taskName="Feed", priority=1, duration=30, preference=1)   # fits, total=30
    task2 = Task(taskName="Walk", priority=1, duration=40, preference=2)   # fits, total=70
    task3 = Task(taskName="Groom", priority=2, duration=20, preference=1)  # fits, total=90
    task4 = Task(taskName="Bath", priority=2, duration=80, preference=2)   # doesn't fit (90+80=170>120)

    pet.add_task(task1)
    pet.add_task(task2)
    pet.add_task(task3)
    pet.add_task(task4)

    schedule = Scheduler.schedule_for_owner(owner)
    scheduled_names = [t.taskName for t in schedule]

    assert "Feed" in scheduled_names
    assert "Walk" in scheduled_names
    assert "Groom" in scheduled_names
    assert "Bath" not in scheduled_names, "Bath should not fit within the time constraint"
    assert all(t.startTime != "" for t in schedule), "All scheduled tasks should have a startTime"

# no need to check for conflict detection because all pets' tasks are scheduled as a collective,
# so there is no opportunity for conflict.