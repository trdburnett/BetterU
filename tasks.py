import datetime
from save import save_list
from file_paths import tasklist_file_path
time = datetime.datetime

class Task:
    def __init__(self,description: str, priority: int, reward: int, time: datetime, id: int):
        self.description = description
        self.priority = priority
        self.reward = reward
        self.time = time
        self.id = id

#adds a task object to the task list
def add_task(description: str, priority: int, reward: int, task_id: int, tasklist: list):
    task = Task(description,priority,reward,time.now(),task_id)
    tasklist.append(task)
    save_list(tasklist_file_path, tasklist)
    print("Task Added.")

