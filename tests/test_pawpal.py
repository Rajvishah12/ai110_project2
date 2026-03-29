from pawpal_system import Task, Pet

def test_task_completion():
    task = Task(taskName="Feed", priority=1, duration=0.5)
    assert not task.completed
    task.mark_complete()
    assert task.completed

def test_pet_task_addition():
    pet = Pet(petName="Fido")
    initial_count = len(pet.taskList)
    task = Task(taskName="Walk", priority=2, duration=1.0)
    pet.add_task(task)
    assert len(pet.taskList) == initial_count + 1
    assert task in pet.taskList
