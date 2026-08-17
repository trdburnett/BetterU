import datetime
from enum import Enum
from operator import attrgetter

time = datetime.datetime
tasklist = []

class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

class Task:
    def __init__(self,description: str, priority: Priority, reward: int, time: datetime):
        self.description = description
        self.priority = priority
        self.reward = reward
        self.time = time

#adds a task object to the task list
def add_task(description, priority, reward):
    task = Task(description,priority,reward,time.now())
    tasklist.append(task)

def display_tasks():
    tasklist_by_priority = sorted(tasklist, key=attrgetter('priority'))
    for task in tasklist_by_priority:
        print(f"Task: {task.description}       Reward: {task.reward} Credits")
    #sorts by time if reverse is true shows oldest last
    tasklist_by_time = sorted(tasklist, key=lambda task: task.time, reverse=True)
    for task in tasklist_by_time:
        print(f"Task: {task.description} ===== Reward: {task.reward} Credits")


#hard coded inputs
add_task("Do 3 sets of bicep curls for 5 reps", 3, 1)
add_task("Do 3 lessons on boot.dev", 1, 3)
add_task("Go for a 10K walk", 2, 2)
task = Task("Touch grass",3,1,time(2025,1,1))
tasklist.append(task)
display_tasks()

