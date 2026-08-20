import datetime, argparse, os, pickle
from enum import Enum
from operator import attrgetter

time = datetime.datetime
tasklist = []
rewardlist = []
task_id = 1
reward_id = 1
credits = 0
tasks_completed = 0
high_priority_tasks_completed = 0
medium_priority_tasks_completed = 0
low_priority_tasks_completed = 0
rewards_claimed = 0
tasklist_file_path = 'data/tasklist.dat'
rewardlist_file_path = 'data/rewardlist.dat'
credits_file_path = 'data/credits.txt'

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

class Reward:
    def __init__(self,description: str, cost: int, id: int):
        self.description = description
        self.cost = cost
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

#helper function for load
#similar to getmax_task_id but for rewards instead
def getmax_reward_id():
    max_id = 0
    for reward in rewardlist:
        if reward.id > max_id:
            max_id = reward.id
    return max_id

#checks to see if data/tasklist.dat exisits
#if it does it loads the task objects from the file into the tasklist
#then uses getmax_task_id() helper to set the task_id
#checks to see if data/tasklist.dat exists
#follows similar flow as tasklist loading
#checks to see if data/credits.txt exisits
#if it does it loads the value and sets the credit variable
def load():
    global task_id
    global reward_id
    global credits
    if os.path.exists(tasklist_file_path):
        with open(tasklist_file_path, 'rb') as inp:
            #uses the first dump of the length of the list to know what to load from the file
            for _ in range(pickle.load(inp)):
                tasklist.append(pickle.load(inp))
        task_id += getmax_task_id()
    if os.path.exists(rewardlist_file_path):
        with open(rewardlist_file_path, 'rb') as inp:
            for _ in range(pickle.load(inp)):
                rewardlist.append(pickle.load(inp))
        reward_id += getmax_reward_id()
    if os.path.exists(credits_file_path):
        with open(credits_file_path, 'r') as f:
            for line in f:
                if "Credits" in line:
                    credits += int(line.lstrip("Credits: "))
load()

#saves the tasklist to the tasklist file
#if the file does not exisit it creates it and any missing directories first
#is only called after adding a task and completing a task
def save_tasklist():
    if not os.path.exists(tasklist_file_path):
        os.makedirs('data', exist_ok=True)
        f = open(tasklist_file_path, 'x')
        f.close()
    with open(tasklist_file_path, 'wb') as outp:
        #first dump is the length of the list
        pickle.dump(len(tasklist), outp, pickle.HIGHEST_PROTOCOL)
        for task in tasklist:
            pickle.dump(task, outp)

#saves the rewardlist to the rewardlist file
#works similar to save_tasklist
def save_rewardlist():
    if not os.path.exists(rewardlist_file_path):
        os.makedirs('data', exist_ok=True)
        f = open(rewardlist_file_path, 'x')
        f.close()
    with open(rewardlist_file_path, 'wb') as outp:
        pickle.dump(len(rewardlist), outp, pickle.HIGHEST_PROTOCOL)
        for reward in rewardlist:
            pickle.dump(reward, outp)

#saves total available credits
def save_credits():
    if not os.path.exists(credits_file_path):
        os.makedirs('data', exist_ok=True)
        f = open(credits_file_path, 'x')
        f.close()
    with open(credits_file_path, 'w') as f:
        f.write(f"Credits: {credits}")           

#adds a task object to the task list
def add_task(description, priority, reward):
    task = Task(description,priority,reward,time.now(),task_id)
    tasklist.append(task)
    save_tasklist()

#removes a task object from the task list and awards credits
def complete_task(task_id):
    global credits
    global tasks_completed
    global high_priority_tasks_completed
    global medium_priority_tasks_completed
    global low_priority_tasks_completed
    found = False
    for i in range(len(tasklist)):
        if tasklist[i].id == task_id:
            index_to_remove = i
            found = True
            credits_to_add = tasklist[i].reward
    if found:
        if tasklist[index_to_remove].priority == 1:
            high_priority_tasks_completed += 1
        if tasklist[index_to_remove].priority == 2:
            medium_priority_tasks_completed += 1
        if tasklist[index_to_remove].priority == 3:
            low_priority_tasks_completed += 1
        tasks_completed += 1
        credits += credits_to_add
        del tasklist[index_to_remove]
        save_tasklist()
        save_credits()
        print(f"Tasks Completed: {tasks_completed}")
        print(f"High Priority Tasks Completed: {high_priority_tasks_completed}")
        print(f"Medium Priority Tasks Completed: {medium_priority_tasks_completed}")
        print(f"Low Priority Tasks Completed: {low_priority_tasks_completed}")
    else:
        print("Task not found, check task ID.")

#add a reward object to the reward list
def add_reward(description, cost):
    reward = Reward(description,cost,reward_id)
    rewardlist.append(reward)
    save_rewardlist()

#removes a reward object from the reward list and removes the cost from available credits
def claim_reward(reward_id):
    global credits
    global rewards_claimed
    found = False
    for i in range(len(rewardlist)):
        if rewardlist[i].id == reward_id:
            index_to_remove = i
            found = True
            credits_to_deduct = rewardlist[i].cost
    if found and credits >= credits_to_deduct:
        credits -= credits_to_deduct
        rewards_claimed += 1
        del rewardlist[index_to_remove]
        save_rewardlist()
        save_credits()
        print(f"Rewards Claimed: {rewards_claimed}")
    elif not found:
        print("Reward not found, check reward ID.")
    else:
        print("You don't have enough credits for that reward yet.")


#shows available credits
def display_credits():
    print(f"Available Credits: {credits}")

#sorts the tasklist by priority and then time
#the oldest tasks with the highest priority will display at the top
def display_tasks():
    sorted_tasklist = sorted(tasklist, key=attrgetter('priority','time'))
    for task in sorted_tasklist:
        print(f"Task[{task.id}]: {task.description}{display_padding(task.description)}| Reward: {task.reward} Credits")

#displays the rewards list
def display_rewards():
    for reward in rewardlist:
        print(f"Reward[{reward.id}]: {reward.description}{display_padding(reward.description)}| Cost: {reward.cost} Credits")

#returns a string of spaces based on the length of the description it is given
#helper method for display tasks and display rewards
def display_padding(description):
    padding = ""
    padding_size = 50 - len(description)
    while padding_size > 0:
        padding = padding + " "
        padding_size -= 1
    return padding

#parsing command line arguments for different functions see help descriptions
parser = argparse.ArgumentParser()
parser.add_argument('--tasks', action='store_true', help='displays the task list')
parser.add_argument('--rewards', action='store_true', help='displays the reward list')
parser.add_argument('--credits', action='store_true', help='displays available credits')
subparsers = parser.add_subparsers()
parser_add_task = subparsers.add_parser('add_task', help='add a task to the task list')
parser_add_task.add_argument('task_description', type=str, help='Description of task')
parser_add_task.add_argument('task_priority', type=int, choices=[1,2,3], help='Priority of task')
parser_add_task.add_argument('task_reward', type=int, choices=[1,2,3,4,5], help='Reward of task')
parser_complete_task = subparsers.add_parser('complete_task', help='removes a task from the task list by task ID and applies reward credit(s)')
parser_complete_task.add_argument('task_id', type=int, help='Task ID number')
parser_add_reward = subparsers.add_parser('add_reward', help='add a reward to the reward list')
parser_add_reward.add_argument('reward_description', type=str, help='Description of reward')
parser_add_reward.add_argument('reward_cost', type=int, help='Cost of redeeming reward')
parser_claim_reward = subparsers.add_parser('claim_reward', help='removes a reward from the rewards list by reward ID and deducts the cost from available credits')
parser_claim_reward.add_argument('reward_id', type=int, help='Reward ID number')
args = parser.parse_args()

#branch for calling display_tasks()
if args.tasks:
    display_tasks()

#branch for calling display_rewards()
if args.rewards:
    display_rewards()

#branch for calling display_credits()
if args.credits:
    display_credits()

#branch for calling add_task
if 'task_description' in args and 'task_priority' in args and 'task_reward' in args:
    add_task(args.task_description,args.task_priority,args.task_reward)

#branch for calling complete_task
if 'task_id' in args:
    complete_task(args.task_id)

#branch for calling reward_task
if 'reward_description' in args and 'reward_cost' in args:
    add_reward(args.reward_description,args.reward_cost)

#branch for calling claim_reward
if 'reward_id' in args:
    claim_reward(args.reward_id)
    


