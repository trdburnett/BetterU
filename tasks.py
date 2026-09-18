import datetime
from operator import attrgetter
from achievements import check_achievements
from streak import daily_reward
from display import display_banner, display_padding
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
    print("Task Added.")
    return tasklist

#removes a task object from the task list only
def remove_task(task_id: int, tasklist: list, called_from_complete_task=False):
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
        #save_list(tasklist_file_path, tasklist)
        if not called_from_complete_task:
            print("Task Removed.")
            return tasklist
        else:
            return {"description": description,
                          "priority": priority,
                          "reward": reward,
                          "task_time": task_time,
                          "tasklist": tasklist}
    else:
        print("Task not found, check task ID.")
        if called_from_complete_task:
            return None
        else:
            return tasklist

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

#removes a task object from the task list and awards credits
def complete_task(task_id: int, tasklist: list, achievementlist: list, last_accessed: datetime, tasks_completed: int, high_priority_tasks_completed: int, medium_priority_tasks_completed: int, low_priority_tasks_completed: int, rewards_claimed: int, streak: int, repeat=False)->set:
    credits_to_add = 0
    tasks_completed_to_add = 0
    high_priority_tasks_completed_to_add = 0
    medium_priority_tasks_completed_to_add = 0
    low_priority_tasks_completed_to_add = 0
    streak_to_add = 0
    retdict = remove_task(task_id, tasklist, called_from_complete_task=True)
    if not retdict == None:
        if retdict["priority"] == 1:
            high_priority_tasks_completed_to_add += 1
        if retdict["priority"] == 2:
            medium_priority_tasks_completed_to_add += 1
        if retdict["priority"] == 3:
            low_priority_tasks_completed_to_add += 1
        tasks_completed_to_add += 1
        t = time_remaining(retdict["priority"],retdict["task_time"])
        if t == "Expired!":
            print(f"Task Completed, however no credits have been awarded due to the task not being completed in time.")
        else:
            credits_to_add += retdict["reward"]
            print(f"Task Completed, you have been awarded {retdict["reward"]} credit(s)")
        lacs = daily_reward(time.now(), last_accessed, streak)
        last_accessed = lacs[0]
        credits_to_add += lacs[1]
        streak_to_add += lacs[2]
        credits_to_add += check_achievements(achievementlist,tasks_completed,high_priority_tasks_completed,medium_priority_tasks_completed,low_priority_tasks_completed,rewards_claimed)
        if repeat:
            tasklist = add_task(retdict["description"],retdict["priority"],retdict["reward"],task_id,retdict["tasklist"])
        else:
            tasklist = retdict["tasklist"]
    return (credits_to_add, tasks_completed_to_add, high_priority_tasks_completed_to_add, medium_priority_tasks_completed_to_add, low_priority_tasks_completed_to_add, streak_to_add, last_accessed, tasklist)

#sorts the tasklist by priority and then time
#the oldest tasks with the highest priority will display at the top
def display_tasks(tasklist: list):
    if tasklist == []:
        print("No tasks to display, please add some tasks.")
    else:
        print(display_banner("Tasks"))
        sorted_tasklist = sorted(tasklist, key=attrgetter('priority','time'))
        for task in sorted_tasklist:
            print(f"Task[{task.id}]: {task.description}{display_padding(task.description)}| Reward: {task.reward} Credits | Time Remaining: {time_remaining(task.priority,task.time)}")

