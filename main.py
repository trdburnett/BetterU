import datetime, argparse, os, pickle
from enum import Enum
from operator import attrgetter

time = datetime.datetime
tasklist = []
task_id = 1
tasklist_file_path = 'data/tasklist.dat'

class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

class Task:
    def __init__(self,description: str, priority: Priority, reward: int, time: datetime, id: int):
        self.description = description
        self.priority = priority
        self.reward = reward
        self.time = time
        self.id = id

#helper function for load
#cycles through the tasks in the task list to find the one with the highest number
#used to add to task_id which is initialised at 1
#this ensures all tasks have a unique ID 
def getmax_task_id():
    max_id = 0
    for task in tasklist:
        if task.id > max_id:
            max_id = task.id
    return max_id

#checks to see if data/tasklist.dat exisits
#if it does it loads the task objects from the file into the tasklist
#then uses getmax_task_id() helper to set the task_id
def load():
    if os.path.exists(tasklist_file_path):
        with open(tasklist_file_path, 'rb') as inp:
            #uses the first dump of the length of the list to know what to load from the file
            for _ in range(pickle.load(inp)):
                tasklist.append(pickle.load(inp))
        task_id = task_id + getmax_task_id()
load()

#saves the tasklist to the tasklist file
#if the file does not exisit it creates it and any missing directories first
#is only called after adding a task
def save():
    if not os.path.exists(tasklist_file_path):
        os.makedirs('data', exist_ok=True)
        f = open(tasklist_file_path, 'x')
        f.close()
    with open(tasklist_file_path, 'wb') as outp:
        #first dump is the length of the list
        pickle.dump(len(tasklist), outp, pickle.HIGHEST_PROTOCOL)
        for task in tasklist:
            pickle.dump(task, outp)            

#adds a task object to the task list
def add_task(description, priority, reward):
    task = Task(description,priority,reward,time.now(),task_id)
    tasklist.append(task)
    save()

#sorts the tasklist by priority and then time
#the oldest tasks with the highest priority will display at the top
def display_tasks():
    sorted_tasklist = sorted(tasklist, key=attrgetter('priority','time'))
    for task in sorted_tasklist:
        print(f"Task[{task.id}]: {task.description}{display_padding(task.description)}| Reward: {task.reward} Credits")

#returns a string of spaces based on the length of the description it is given
#helper method for display tasks
def display_padding(description):
    padding = ""
    padding_size = 50 - len(description)
    while padding_size > 0:
        padding = padding + " "
        padding_size -= 1
    return padding

#parsing command line arguments for different functions see help descriptions
parser = argparse.ArgumentParser()
parser.add_argument("--display", action='store_true', help="displays the task list")
subparsers = parser.add_subparsers()
parser_add_task = subparsers.add_parser('add_task', help='add a task to the task list')
parser_add_task.add_argument('task_description', type=str, help='Description of task')
parser_add_task.add_argument('task_priority', type=int, choices=[1,2,3], help='Priority of task')
parser_add_task.add_argument('task_reward', type=int, choices=[1,2,3,4,5], help='Reward of task')
args = parser.parse_args()

#branch for calling display_tasks()
if args.display:
    display_tasks()

#branch for calling add_task
if 'task_description' in args and 'task_priority' in args and 'task_reward' in args:
    add_task(args.task_description,args.task_priority,args.task_reward)


    


