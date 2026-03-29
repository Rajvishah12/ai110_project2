
from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    """Represents a pet care task"""
    taskName: str
    priority: int  # 1 for high, 2 for medium, 3 for low
    duration: float  # Time required to complete the task in hours
    description: str = ""
    frequency: str = "" # times per week? times per month? etc.
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    """Represents a pet in the PawPal system"""
    petName: str
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
    timeConstraint: float  # Time available for pet care in hours
    petList: list = field(default_factory=list)    
    
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

    @staticmethod # static so never needs to be instantiated. just call Scheduler.method with owner var as parameter.
    def get_all_tasks(owner: Owner) -> List[Task]:
        """Retrieve all tasks for the owner's pets (not completed)."""
        ownerTaskList = []
        for pet in owner.petList:
            ownerTaskList.extend([task for task in pet.taskList if not task.completed])
        return ownerTaskList

    @staticmethod
    def schedule_for_owner(owner: Owner) -> List[Task]:
        """Return a schedule of tasks for all of the owner's pets, sorted by priority and fitting within the owner's time constraint."""
        all_tasks = Scheduler.get_all_tasks(owner)
        # Sort by priority (1=high, 2=medium, 3=low), then by duration ascending
        all_tasks.sort(key=lambda t: (t.priority, t.duration))
        scheduled = []
        total_time = 0.0
        for task in all_tasks:
            if total_time + task.duration <= owner.timeConstraint:
                scheduled.append(task)
                task.mark_complete() # Mark task as completed when scheduled
                total_time += task.duration
            else:
                break
        return scheduled