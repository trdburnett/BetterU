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

#removes a task object from the task list only
def remove_task(task_id: int, tasklist: list, remove=True):
    found = False
    description = None
    priority = None
    reward = None
    task_time = None
    for i in range(len(tasklist)):
        if tasklist[i].id == task_id:
            index_to_remove = i
            found = True
            description = tasklist[i].description
            priority = tasklist[i].priority
            reward = tasklist[i].reward
            task_time = tasklist[i].time
    if found:
        del tasklist[index_to_remove]
        save_list(tasklist_file_path, tasklist)
        if remove:
            print("Task Removed.")
        else:
            return (description,priority,reward,task_time)
    else:
        print("Task not found, check task ID.")
        if not remove:
            return (description,priority,reward,task_time)

#returns either the time remaining to complete a task or expired string
#helper for display_tasks and complete_tasks                    
def time_remaining(task_priority: int, task_time: datetime):
    if task_priority == 1:
        task_deadline = task_time + datetime.timedelta(days=2)
    if task_priority == 2:
        task_deadline = task_time + datetime.timedelta(days=7)
    if task_priority == 3:
        task_deadline = task_time + datetime.timedelta(days=28)
    if task_deadline - time.now() < datetime.timedelta(seconds=0):
        return "Expired!"
    else:
        return task_deadline - time.now()


