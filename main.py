from pawpal_system import Task, Pet, Owner, Scheduler

def main():
    # Owner Creation
    ownerMiles = Owner(ownerName="Miles", timeConstraint=5.0)  # Miles has 5 hours available for pet care

    # Pet Creation
    petTeddy = Pet(petName="Teddy")
    petBiscuit = Pet(petName="Biscuit")

    ownerMiles.add_pet(petTeddy)
    ownerMiles.add_pet(petBiscuit)

    # Task Creation
    task1 = Task(taskName="Feed Teddy", priority=1, duration=0.5)
    task2 = Task(taskName="Walk Teddy", priority=2, duration=1)
    task3 = Task(taskName="Wash Teddy", priority=3, duration=3)
    task4 = Task(taskName="Feed Biscuit", priority=1, duration=0.5)
    task5 = Task(taskName="Walk Biscuit", priority=2, duration=1)
    task6 = Task(taskName="Wash Biscuit", priority=3, duration=2)

    petTeddy.add_task(task1)
    petTeddy.add_task(task2)
    petTeddy.add_task(task3)
    petBiscuit.add_task(task4)
    petBiscuit.add_task(task5)
    petBiscuit.add_task(task6)

    # schedule should be feed, feed, walk, walk, wash biscuit (Teddy's wash wouldn't fit)

    schedule = Scheduler.schedule_for_owner(ownerMiles)
    print("Scheduled Tasks for Miles:")
    for task in schedule:
        print(f"{task.taskName} (Priority: {task.priority}, Duration: {task.duration} hours)")

if __name__ == "__main__":    main()



