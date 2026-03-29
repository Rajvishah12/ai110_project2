import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
owner_time_constraint = st.number_input("Owner time constraint (hours)", value=2.0)
if "owner" not in st.session_state:
    st.session_state.owner = Owner(ownerName=owner_name, timeConstraint=owner_time_constraint)
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
# Add new pet
if st.button("Add pet"):
    newPet = Pet(petName=pet_name, species=species)
    st.session_state.owner.add_pet(newPet)

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

petNames = [pet.petName for pet in st.session_state.owner.petList]
selected_pet_name = st.selectbox("Select pet", petNames)
selected_pet = next((pet for pet in st.session_state.owner.petList if pet.petName == selected_pet_name), None)
if selected_pet is None:
    st.error("Selected pet not found.")

if st.button("Add task"):
    if priority == "high":
        priority_value = 1
    elif priority == "medium":
        priority_value = 2
    else:        
        priority_value = 3
    new_task = Task(taskName=task_title, priority=priority_value, duration=duration)
    # Add task to selected_pet
    selected_pet.add_task(new_task)

if selected_pet and selected_pet.taskList:
    st.write("Selected Pet tasks:")
    st.table(selected_pet.taskList)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    # Example: generate schedule for the current owner
    schedule = Scheduler.schedule_for_owner(st.session_state.owner)
    if schedule:
        st.write("Generated Schedule:")
        schedule_data = [
            {
                "Task": task.taskName,
                "Pet": next((pet.petName for pet in st.session_state.owner.petList if task in pet.taskList), "Unknown"),
                "Priority": task.priority,
                "Duration (min)": int(task.duration),
            }
            for task in schedule
        ]
        st.table(schedule_data)
    else:
        st.info("No tasks could be scheduled with the current constraints.")
    st.write("Your schedule has been created to prioritize high priority tasks and get as many tasks done as possible. All pets' tasks are considered in this schedule.")

st.divider()
