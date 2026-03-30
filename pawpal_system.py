
from dataclasses import dataclass, field
from typing import List
import datetime

@dataclass
class Task:
    """Represents a pet care task"""
    taskName: str
    priority: int  # 1 for high, 2 for medium, 3 for low
    duration: float  # Time required to complete the task in minutes
    preference: int # 1 for high, 2 for medium, 3 for low
    description: str = ""
    frequency: str = "" # daily, weekly, etc. (optional)
    completed: bool = False
    startTime: str = "" # will be filled in when scheduled, format "HH:MM"

    def mark_complete(self):
        """Mark this task as completed."""
        if self.frequency != "daily": 
            # if task needs to be done daily, it's never really completed
            self.completed = True

@dataclass
class Pet:
    """Represents a pet in the PawPal system"""
    petName: str
    species: str = ""
    taskList: list = field(default_factory=list)

    def add_task(self, task):
        """Add a task to the pet's task list."""
        self.taskList.append(task)

    def remove_task(self, task):
        """Remove a task from the pet's task list if it exists."""
        if task in self.taskList:
            self.taskList.remove(task)
    
@dataclass
class Owner:
    """Represents a pet owner"""
    ownerName: str
    startAvailability: str # HH:MM
    endAvailability: str # HH:MM
    timeConstraint: float = 0.0 # Time available for pet care in hours
    petList: list = field(default_factory=list)    
    
    def __post_init__(self):
        """Convert start and end availability to datetime objects and compute time constraint using timedelta."""
        start_dt = datetime.datetime.strptime(self.startAvailability, "%H:%M")
        end_dt = datetime.datetime.strptime(self.endAvailability, "%H:%M")
        if end_dt < start_dt: # so need to worry about military time
            # If end time is past midnight, add a day
            end_dt += datetime.timedelta(days=1)
        delta = end_dt - start_dt
        self.timeConstraint = delta.total_seconds() / 3600.0

    def add_pet(self, pet):
        """Add a pet to the owner's pet list."""
        self.petList.append(pet)

    def remove_pet(self, pet):
        """Remove a pet from the owner's pet list if it exists."""
        if pet in self.petList:
            self.petList.remove(pet)

@dataclass
class Scheduler:
    """Handles scheduling of tasks for all of an owner's pets based on owner's time constraints"""

    @staticmethod
    def get_all_tasks(owner: Owner) -> List[Task]:
        """Retrieve all tasks for the owner's pets (not completed)."""
        ownerTaskList = []
        for pet in owner.petList:
            ownerTaskList.extend([task for task in pet.taskList if not task.completed])
        return ownerTaskList

    @staticmethod
    def sort_tasks_by_time_and_priority(task_list: List[Task]) -> List[Task]:
        """Sort tasks by priority (1=high, 2=medium, 3=low), then by duration ascending."""
        return sorted(task_list, key=lambda t: (t.priority, t.duration))
    
    @staticmethod
    def sort_scheduled_by_priority_and_preference(scheduled: List[Task]) -> List[Task]:
        """Sort a scheduled task list by priority (1=high, 2=medium, 3=low), then by preference (1=high, 2=medium, 3=low)."""
        return sorted(scheduled, key=lambda t: (t.priority, t.preference))

    @staticmethod
    def schedule_for_owner(owner: Owner) -> List[Task]:
        """Return a schedule of tasks for all of the owner's pets, sorted by priority and fitting within the owner's time constraint."""
        all_tasks = Scheduler.get_all_tasks(owner)
        sorted_tasks = Scheduler.sort_tasks_by_time_and_priority(all_tasks) # sort tasks
        # no need to check for overlap between schedules because all pets' tasks are scheduled as a collective
        scheduled = []
        total_time = 0.0
        for task in sorted_tasks:
            if total_time + task.duration <= owner.timeConstraint*60:
                scheduled.append(task)
                task.startTime = (datetime.datetime.strptime(owner.startAvailability, "%H:%M") + datetime.timedelta(minutes=total_time)).strftime("%H:%M")
                task.mark_complete() # Mark task as completed when scheduled
                total_time += task.duration
        sorted_scheduled = Scheduler.sort_scheduled_by_priority_and_preference(scheduled)
        return sorted_scheduled
