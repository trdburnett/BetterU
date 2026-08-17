import datetime
from enum import Enum

time = datetime.datetime
tasklist = []

class Priority(Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

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
    for task in tasklist:
        if task.priority == Priority.LOW:
            print("1")

#hard coded inputs
add_task("Do 3 sets of bicep curls for 5 reps", "Low", 1)
display_tasks()
for task in tasklist:
    print(f"Task: {task.description} ----- Reward: {task.reward} Credits")
