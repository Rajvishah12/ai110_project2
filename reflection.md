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
My scheduler considers priority and duration of tasks when deciding what goes on the schedule. Once the tasks that go on the schedule are decided, they are then sorted by priority, then preference.

- How did you decide which constraints mattered most?
All tasks must be completed at some point. So, preferences seemed the least important. Priority matters the most, as the highest priority tasks should be completed first. Duration of the tasks is less relevant than priority, as if there is a spsecific amount of time available, the higher priority task should be completed first.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
My tradeoff maximizes for the greatest number of tasks that can be done at once. So, say there is a 1 hour block available with a 20 minute task and 50 minute task incomplete with the same priority level. The 20 minute task will be allocated for that time, even though the 50 minute task may be a better use of time.
- Why is that tradeoff reasonable for this scenario?
If there are several high priority tasks, it seems to make more sense to try to get as many of those done as possible, rather than (for example) holding off on 3 tasks to do 1 larger task when they are all the same priority level. So, I thought it made sense to focus on getting as many tasks done as possible (in order of priority) rather than filling in the more time consuming tasks first.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?

- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
Originally when building the class based on the UML diagram, Copilot added some extra classes and extra attributes to classes that were already designed. Though some of the attributes were relevant, others seemed like they came out of nowhere. Even though I had explained the intention of the project with the UML diagram, it did not ask before filling in the pawpal_system.py file with extra classes and attributes. So, I looked through each of the extra features it added and decided what made sense to keep and remove. For each of these extras, I tried to consider whether an attribute they added was something I forgot / something that could be useful down the line or beyond the scope of this project. 

---

## 4. Testing and Verification
Use 'python -m pytest' to run tests.

**a. What you tested**

- What behaviors did you test?
I tested the following behaviors
- marking tasks as complete unless they have daily frequency
- creating additional pets and adding them to owner
- each of my sorting methods (priority and duration, priority and preference)
- calculating owner time constraints based on their availability start and end times
- calculating a schedule (full workflow owner -> pets -> tasks -> schedule)

- Why were these tests important?
These tests are important to make sure each component of the logic works independently and that they all play well together. It's improtant to do the granular checks and not just overall ones, as it's easy to miss if details are working correctly if the larger program "seems" to be working fine.

**b. Confidence**

- How confident are you that your scheduler works correctly?
I am confident (4 stars) my scheduler works correctly (based on the functionality I described at the top of this reflection). 

- What edge cases would you test next if you had more time?
I would test what happens when trying to schedule a task with 0 minute duration. I would also test what happens if a owner enters their availability start and end times in a different format than dictated. Similarly, I would test what the scheduler returns if there are no pets, and therefore no tasks.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I'm most satisfied with the logic in this project. Based on my interpretation, I think I did a good job generating a schedule that acknowledges the task priorities and durations and tries to maximize how much can be done.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
In another iteration, I would make the UI more engaging and intuitive. Currently, there's no add owner button -- users are just supposed to select enter to update the owner's information which can be a bit confusing. Also, the project is only set up to work with one owner right now. In another iteration, allowing it to work for more owners at once would be interesting.

In another iteration, I would also consider updating the algorithm such that in addition to optimizing for priority, it also optimizes for least time wasted, rather than most tasks completed. For example, if the owner has 90 minutes and there are 20, 40, and 50 minute tasks available, my current algorithm will chose the 20 and 40 minute tasks. However, it would be a better use of time to do the 40 and 50 minute tasks to maximize the available time. This could turn into a situation with a tradeoff -- choosing between one longer task and multiple smaller ones.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
One key takeaway from working with AI on this project is that it often doesn't make changes in other places in the code based on one change you ask it to make. It is important to remember to ask it to make the appropriate change wherever relevant, not just in the one part of the codebase you're focused on.
