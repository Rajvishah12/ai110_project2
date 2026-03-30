# PawPal+ Project Reflection

Note: I had some confusion understanding how the scheduler was supposed to be setup in terms of what inputs about a task should be received and what should be outputted. I ended up setting it up so the owner provides a time slot when they are free and tasks with durations needed to complete them and other relevant information. Using an algorithm, I sort tasks into that interval (or not if there's too many/take too long). For example, the input would be the owner is available 9-11 am and they enter tasks like feeding the dog for 15 min, washing the dog for 45 min, etc. (with priorities and preferences) and those tasks get sorted into the 9-11am block.

## 1. System Design

**a. Initial design**
Step 1: 3 core actions
- add a pet (owner should be able to add information for any pets they're taking care of)
- add (owner should be able to add tasks related to a specific pet)
- display generated schedule (the app should calculate the optimal schedule -- optimized for highest priority tasks for a pet -- and display it to the user)

As directed, I included the 3 classes Task, Pet, and Owner. The Owner class has attributes ownerName (string), timeConstraint (float), and petList (a list of Pet objects). Time constraint is included so the schedule fits within the Owner's time constraint. petList is included to track pets. Pet has attributes petName (string), lowPriorityTasks (list of low priority tasks), mediumPriorityTasks (list of medium priority tasks), highPriorityTasks(list of high priority tasks). It makes sense to organize the tasks by priority, since the goal is to select from high priority tasks first and go down the line. The Task Class has attributes taskName (string) and duration (float) for the name and duration of the task respectively.

**b. Design changes**

- Did your design change during implementation?
Yes
- If yes, describe at least one change and why you made it.
Though my design did not change this, Copilot did recommend changing the way tasklists were initialized. It also recommended changing the task priorities to be strings since the 3 task lists are categorical. However, since I write the logic, I will ensure only 1, 2, and 3 are options. I added attributes to track owner preferences and the start and end times of their availabilities as well. 

Also, I forgot to include methods in my original UML diagram so I added them as I went.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
My scheduler considers duration of the 

- How did you decide which constraints mattered most?
All tasks must be completed at some point. So, preferences seemed the least important. Priority matters the most, as the highest priority tasks should be completed first. Duration of the tasks is less relevant than priority, as if there is a spsecific amount of time available, the higher priority task should be completed first.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification
Use 'python -m pytest' to run tests.

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
