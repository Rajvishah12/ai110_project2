from pawpal_system import Task, Pet, Owner, Scheduler

def main():
    # Owner Creation
    ownerMiles = Owner(ownerName="Miles", startAvailability="09:00", endAvailability="14:00")  # Miles has 5 hours available for pet care

    # Pet Creation
    petTeddy = Pet(petName="Teddy")
    petBiscuit = Pet(petName="Biscuit")

    ownerMiles.add_pet(petTeddy)
    ownerMiles.add_pet(petBiscuit)

    # Task Creation
    task1 = Task(taskName="Feed Teddy", priority=1, duration=30, preference=1)
    task2 = Task(taskName="Walk Teddy", priority=2, duration=60, preference=2)
    task3 = Task(taskName="Wash Teddy", priority=2, duration=180, preference=3)
    task4 = Task(taskName="Feed Biscuit", priority=1, duration=30, preference=1)
    task5 = Task(taskName="Walk Biscuit", priority=2, duration=60, preference=3)
    task6 = Task(taskName="Wash Biscuit", priority=2, duration=70, preference=2)

    # adding tasks out of order to test sorting
    petTeddy.add_task(task3)
    petTeddy.add_task(task1)
    petTeddy.add_task(task2)
    petBiscuit.add_task(task6)
    petBiscuit.add_task(task4)
    petBiscuit.add_task(task5)

    # print unsorted tasks
    unsorted_tasks = Scheduler.get_all_tasks(ownerMiles)
    print("Unsorted Tasks for Miles:")
    for task in unsorted_tasks:
        print(f"{task.taskName} (Priority: {task.priority}, Duration: {task.duration} minutes)")
    # print sorted tasks
    sorted_tasks = Scheduler.sort_tasks_by_time_and_priority(unsorted_tasks)
    print("\nSorted Tasks for Miles:")
    for task in sorted_tasks:
        print(f"{task.taskName} (Priority: {task.priority}, Duration: {task.duration} minutes)")
    

    # schedule should be feed, feed, walk, walk, wash biscuit (Teddy's wash wouldn't fit)
    schedule = Scheduler.schedule_for_owner(ownerMiles)
    print("\nScheduled Tasks for Miles:")
    for task in schedule:
        print(f"{task.taskName} (StartTime: {task.startTime}, Priority: {task.priority}, Duration: {task.duration} minutes)")

if __name__ == "__main__":    main()



