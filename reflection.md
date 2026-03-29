# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**
Step 1: 3 core actions
- add a pet (owner should be able to add information for any pets they're taking care of)
- add/edit tasks (owner should be able to add or edit tasks related to a specific pet)
- display generated schedule (the app should calculate the optimal schedule -- optimized for highest priority tasks for a pet -- and display it to the user)

As directed, I included the 3 classes Task, Pet, and Owner. The Owner class has attributes ownerName (string), timeConstraint (float), and petList (a list of Pet objects). Time constraint is included so the schedule fits within the Owner's time constraint. petList is included to track pets. Pet has attributes petName (string), lowPriorityTasks (list of low priority tasks), mediumPriorityTasks (list of medium priority tasks), highPriorityTasks(list of high priority tasks). It makes sense to organize the tasks by priority, since the goal is to select from high priority tasks first and go down the line. The Task Class has attributes taskName (string) and duration (float) for the name and duration of the task respectively.

**b. Design changes**

- Did your design change during implementation?
No
- If yes, describe at least one change and why you made it.
Though my design did not change, Copilot did recommend changing the way tasklists were initialized. It also recommended changing the task priorities to be strings since the 3 task lists are categorical. However, since I write the logic, I will ensure only 1, 2, and 3 are options.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

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
