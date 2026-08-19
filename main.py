import datetime, argparse
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

#sorts the tasklist by priority and then time
#the oldest tasks with the highest priority will display at the top
def display_tasks():
    sorted_tasklist = sorted(tasklist, key=attrgetter('priority','time'))
    for task in sorted_tasklist:
        print(f"Task: {task.description}{display_padding(task.description)}| Reward: {task.reward} Credits")

#returns a string of spaces based on the length of the description it is given
#helper method for display tasks
def display_padding(description):
    padding = ""
    padding_size = 50 - len(description)
    while padding_size > 0:
        padding = padding + " "
        padding_size -= 1
    return padding

parser = argparse.ArgumentParser()
#parser.add_argument("--echo", help="echo the string you use here")
subparsers = parser.add_subparsers()
parser_add_task = subparsers.add_parser('add_task', help='Takes 3 positional arguments (Description,Priority,Reward)')
parser_add_task.add_argument('description', type=str, help='Description of task')
parser_add_task.add_argument('priority', type=int, choices=[1,2,3], help='Priority of task')
parser_add_task.add_argument('reward', type=int, help='Reward of task')
args = parser.parse_args()
print(args)
print(args.description)
display_tasks()


#hard coded inputs
#add_task("Do 3 sets of bicep curls for 5 reps", 3, 1)
#add_task("Do 3 lessons on boot.dev", 1, 3)
#add_task("Go for a 10K walk", 2, 2)
#task = Task("Touch grass",3,1,time(2025,1,1))
#tasklist.append(task)
#display_tasks()

