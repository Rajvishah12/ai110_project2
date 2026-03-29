from dataclasses import dataclass
from typing import List
from enum import Enum

# I did not ask for this -- in my project, a task will be deleted once completed
# class TaskStatus(Enum):
#     """Enumeration for task status"""
#     PENDING = "pending"
#     IN_PROGRESS = "in_progress"
#     COMPLETED = "completed"


@dataclass
class Task:
    """Represents a pet care task"""
    taskName: str
    priority: int  # 1 for high, 2 for medium, 3 for low
    duration: float  # Time required to complete the task in hours
    def __init__(self, taskName: str, priority: int, duration: float):
        self.taskName = taskName
        self.priority = priority
        self.duration = duration


@dataclass
class Pet:
    """Represents a pet in the PawPal system"""
    petName: str
    low_priority_tasks: List[Task] = None
    medium_priority_tasks: List[Task] = None
    high_priority_tasks: List[Task] = None

    def __init__(self, name:str):
        self.name = name
        if self.low_priority_tasks is None:
            self.low_priority_tasks = []
        if self.medium_priority_tasks is None:
            self.medium_priority_tasks = []
        if self.high_priority_tasks is None:
            self.high_priority_tasks = []


class Owner:
    """Represents a pet owner"""
    ownerName: str
    pets: List[Pet] = None
    timeConstraint: float  # Time available for pet care in hours
    def __init__(self, name: str, timeConstraint: float):
        self.name = name
        self.pets: List[Pet] = []
        self.timeConstraint = timeConstraint


# class PawPalSystem:
#     """Main system for managing pets and tasks"""
#     def __init__(self):
#         self.owners: List[Owner] = []
#         self.pets: List[Pet] = []
#         self.tasks: List[Task] = []

#     def add_owner(self, owner: Owner) -> None:
#         """Add a new pet owner"""
#         pass

#     def add_pet(self, pet: Pet) -> None:
#         """Add a new pet"""
#         pass

#     def create_task(self, task: Task) -> None:
#         """Create a new task"""
#         pass