import datetime, argparse, os, pickle
from operator import attrgetter

time = datetime.datetime
tasklist = []
rewardlist = []
achievementlist = []
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
achievementlist_file_path = 'data/achievementlist.dat'
save_file_path = 'data/save.txt'

class Task:
    def __init__(self,description: str, priority: int, reward: int, time: datetime, id: int):
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

class Achievement:
    def __init__(self,description: str, completed: bool, reward: int, required_stat: str, required_value: int):
        self.description = description
        self.completed = completed
        self.reward = reward
        self.required_stat = required_stat
        self.required_value = required_value

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
#checks to see if data/save.txt exisits
#if it does it loads the values and sets variables used in the program
def load():
    global task_id
    global reward_id
    global credits
    global tasks_completed
    global high_priority_tasks_completed
    global medium_priority_tasks_completed
    global low_priority_tasks_completed
    global rewards_claimed
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
    if os.path.exists(achievementlist_file_path):
            with open(achievementlist_file_path, 'rb') as inp:
                for _ in range(pickle.load(inp)):
                    achievementlist.append(pickle.load(inp))
    if os.path.exists(save_file_path):
        with open(save_file_path, 'r') as f:
            for line in f:
                if "Credits" in line:
                    credits += int((line.lstrip("Credits: ")).rstrip(" \n"))
                if "High Priority Tasks Completed" in line:
                    high_priority_tasks_completed += int((line.lstrip("High Priority Tasks Completed: ")).rstrip(" \n"))
                if "Medium Priority Tasks Completed" in line:
                    medium_priority_tasks_completed += int((line.lstrip("Medium Priority Tasks Completed: ")).rstrip(" \n"))
                if "Low Priority Tasks Completed" in line:
                    low_priority_tasks_completed += int((line.lstrip("Low Priority Tasks Completed: ")).rstrip(" \n"))
                if "Tasks Completed" in line and "High" not in line and "Medium" not in line and "Low" not in line:
                    tasks_completed += int((line.lstrip("Tasks Completed: ")).rstrip(" \n"))
                if "Rewards Claimed" in line:
                    rewards_claimed += int((line.lstrip("Rewards Claimed: ")).rstrip(" \n"))
load()

#saves a list to the given lists filepath
def save_list(file_path: str):
    if file_path == tasklist_file_path:
        savelist = tasklist
    if file_path == rewardlist_file_path:
        savelist = rewardlist
    if file_path == achievementlist_file_path:
        savelist = achievementlist
    if not os.path.exists(file_path):
        os.makedirs('data', exist_ok=True)
        f = open(file_path, 'x')
        f.close()
    with open(file_path, 'wb') as outp:
        pickle.dump(len(savelist), outp, pickle.HIGHEST_PROTOCOL)
        for item in savelist:
            pickle.dump(item, outp)

#saves all simple variables used by the program
def save():
    if not os.path.exists(save_file_path):
        os.makedirs('data', exist_ok=True)
        f = open(save_file_path, 'x')
        f.close()
    with open(save_file_path, 'w') as f:
        f.write(f"Credits: {credits} \n")
        f.write(f"High Priority Tasks Completed: {high_priority_tasks_completed} \n")
        f.write(f"Medium Priority Tasks Completed: {medium_priority_tasks_completed} \n")
        f.write(f"Low Priority Tasks Completed: {low_priority_tasks_completed} \n")
        f.write(f"Tasks Completed: {tasks_completed} \n")
        f.write(f"Rewards Claimed: {rewards_claimed} \n")

#populates the achievement_list
def populate_achievement_list():
    achievementlist.append(Achievement("Completed 10 Tasks",False,2,"tasks_completed",10))
    achievementlist.append(Achievement("Completed 50 Tasks",False,10,"tasks_completed",50))
    achievementlist.append(Achievement("Completed 100 Tasks",False,20,"tasks_completed",100))
    achievementlist.append(Achievement("Completed 500 Tasks",False,100,"tasks_completed",500))
    achievementlist.append(Achievement("Completed 1000 Tasks",False,200,"tasks_completed",1000))
    achievementlist.append(Achievement("Completed 5000 Tasks",False,1000,"tasks_completed",5000))
    achievementlist.append(Achievement("Completed 10000 Tasks",False,2000,"tasks_completed",10000))
    achievementlist.append(Achievement("Completed 20 High Priority Tasks",False,2,"high_priority_tasks_completed",20))
    achievementlist.append(Achievement("Completed 100 High Priority Tasks",False,10,"high_priority_tasks_completed",100))
    achievementlist.append(Achievement("Completed 200 High Priority Tasks",False,20,"high_priority_tasks_completed",200))
    achievementlist.append(Achievement("Completed 1000 High Priority Tasks",False,100,"high_priority_tasks_completed",1000))
    achievementlist.append(Achievement("Completed 40 Medium Priority Tasks",False,2,"medium_priority_tasks_completed",40))
    achievementlist.append(Achievement("Completed 200 Medium Priority Tasks",False,10,"medium_priority_tasks_completed",200))
    achievementlist.append(Achievement("Completed 400 Medium Priority Tasks",False,20,"medium_priority_tasks_completed",400))
    achievementlist.append(Achievement("Completed 2000 Medium Priority Tasks",False,100,"medium_priority_tasks_completed",2000))
    achievementlist.append(Achievement("Completed 80 Low Priority Tasks",False,2,"low_priority_tasks_completed",80))
    achievementlist.append(Achievement("Completed 400 Low Priority Tasks",False,10,"low_priority_tasks_completed",400))
    achievementlist.append(Achievement("Completed 800 Low Priority Tasks",False,20,"low_priority_tasks_completed",800))
    achievementlist.append(Achievement("Completed 4000 Low Priority Tasks",False,100,"low_priority_tasks_completed",4000))
    achievementlist.append(Achievement("Claimed 5 Rewards",False,2,"rewards_claimed",5))
    achievementlist.append(Achievement("Claimed 25 Rewards",False,10,"rewards_claimed",25))
    achievementlist.append(Achievement("Claimed 50 Rewards",False,20,"rewards_claimed",50))
    achievementlist.append(Achievement("Claimed 250 Rewards",False,100,"rewards_claimed",250))

#helper method for check_achievements
#takes a required statistic to check and the required value
#returns true if the requirements have been met, false otherwise
def check_achievement(required_stat: str, required_value: int):
    global tasks_completed
    global high_priority_tasks_completed
    global medium_priority_tasks_completed
    global low_priority_tasks_completed
    global rewards_claimed
    if required_stat == "tasks_completed":
        if tasks_completed >= required_value:
            return True
    if required_stat == "high_priority_tasks_completed":
        if high_priority_tasks_completed >= required_value:
            return True
    if required_stat == "medium_priority_tasks_completed":
        if medium_priority_tasks_completed >= required_value:
            return True
    if required_stat == "low_priority_tasks_completed":
        if low_priority_tasks_completed >= required_value:
            return True
    if required_stat == "rewards_claimed":
        if rewards_claimed >= required_value:
            return True
    return False


#performs a check for the achievement list if it is empty it calls the populate and save achievement functions respectively
#otherwise applies credits and alerts user if an achievement has been completed
def check_achievements():
    global credits
    if achievementlist == []:
        populate_achievement_list()
        save_list(achievementlist_file_path)
    else:
        for achievement in achievementlist:
            if not achievement.completed:
                completed = check_achievement(achievement.required_stat,achievement.required_value)
                if completed:
                    achievement.completed = True
                    credits += achievement.reward
                    save()
                    print(f"Achievement completed: {achievement.description} | You have been rewarded {achievement.reward} credits!")
                    save_list(achievementlist_file_path)
                    

#adds a task object to the task list
def add_task(description: str, priority: int, reward: int):
    task = Task(description,priority,reward,time.now(),task_id)
    tasklist.append(task)
    save_list(tasklist_file_path)
    print("Task Added.")

#removes a task object from the task list only
def remove_task(task_id: int, remove=True):
    found = False
    description = None
    priority = None
    reward = None
    for i in range(len(tasklist)):
        if tasklist[i].id == task_id:
            index_to_remove = i
            found = True
            description = tasklist[i].description
            priority = tasklist[i].priority
            reward = tasklist[i].reward
    if found:
        del tasklist[index_to_remove]
        save_list(tasklist_file_path)
        if remove:
            print("Task Removed.")
        else:
            return (description,priority,reward)
    else:
        print("Task not found, check task ID.")
        if not remove:
            return (description,priority,reward)

#removes a task object from the task list and awards credits
def complete_task(task_id: int, repeat=False):
    global credits
    global tasks_completed
    global high_priority_tasks_completed
    global medium_priority_tasks_completed
    global low_priority_tasks_completed
    dpr = remove_task(task_id, remove=False)
    if not dpr[0] == None and not dpr[1] == None and not dpr[2] == None:
        if dpr[1] == 1:
            high_priority_tasks_completed += 1
        if dpr[1] == 2:
            medium_priority_tasks_completed += 1
        if dpr[1] == 3:
            low_priority_tasks_completed += 1
        tasks_completed += 1
        credits += dpr[2]
        save()
        print(f"Task Completed, you have been awarded {dpr[2]} credit(s)")
        check_achievements()
        if repeat:
            add_task(dpr[0],dpr[1],dpr[2])

#add a reward object to the reward list
def add_reward(description: str, cost: int):
    reward = Reward(description,cost,reward_id)
    rewardlist.append(reward)
    save_list(rewardlist_file_path)
    print("Reward Added.")

#removes a reward object from the reward list only
def remove_reward(reward_id: int, remove=True):
    found = False
    description = None
    cost = None
    for i in range(len(rewardlist)):
        if rewardlist[i].id == reward_id:
            index_to_remove = i
            found = True
            description = rewardlist[i].description
            cost = rewardlist[i].cost
    if found:
        if remove:
            del rewardlist[index_to_remove]
            save_list(rewardlist_file_path)
            print("Reward Removed.")
        else:
            if cost <= credits:
                del rewardlist[index_to_remove]
                save_list(rewardlist_file_path)
                return (description,cost)
            else:
                print("You don't have enough credits for that reward yet.")
                description = None
                cost = None
                return (description,cost)
    else:
        print("Reward not found, check reward ID.")
        return (description,cost)

#removes a reward object from the reward list and removes the cost from available credits
def claim_reward(reward_id: int, repeat=False):
    global credits
    global rewards_claimed
    dc = remove_reward(reward_id, False)
    if not dc[0] == None and not dc[1] == None:
        credits -= dc[1]
        rewards_claimed += 1
        save()
        print(f"Reward Claimed, {dc[1]} credit(s) have been deducted.")
        check_achievements()
        if repeat:
            add_reward(dc[0],dc[1])


#shows available credits
def display_credits():
    print(f"Available Credits: {credits}")

#sorts the tasklist by priority and then time
#the oldest tasks with the highest priority will display at the top
def display_tasks():
    if tasklist == []:
        print("No tasks to display, please add some tasks.")
    else:
        print(display_banner("Tasks"))
        sorted_tasklist = sorted(tasklist, key=attrgetter('priority','time'))
        for task in sorted_tasklist:
            print(f"Task[{task.id}]: {task.description}{display_padding(task.description)}| Reward: {task.reward} Credits")

#displays the rewards list
def display_rewards():
    if rewardlist == []:
        print("No rewards to display. please add some rewards.")
    else:
        print(display_banner("Rewards"))
        for reward in rewardlist:
            print(f"Reward[{reward.id}]: {reward.description}{display_padding(reward.description)}| Cost: {reward.cost} Credits")

#displays statistics
def display_stats():
    print(display_banner("Statistics"))
    print(f"Tasks Completed: {tasks_completed}")
    print(f"High Priority Tasks Completed: {high_priority_tasks_completed}")
    print(f"Medium Priority Tasks Completed: {medium_priority_tasks_completed}")
    print(f"Low Priority Tasks Completed: {low_priority_tasks_completed}")
    print(f"Rewards Claimed: {rewards_claimed}")

#displays the achievement list
def display_achievements():
    check_achievements()
    if achievementlist == []:
        print("Oh Dear, sorry the achievements have failed to load. Please try again.")
    else:
        print(display_banner("Achievements"))
        for achievement in achievementlist:
            print(f"{achievement.description}{display_padding(achievement.description)}| Completed: {achievement.completed}")

#returns a string of spaces based on the length of the description it is given
#helper method for display functions
def display_padding(description: str)->str:
    padding = ""
    padding_size = 50 - len(description)
    while padding_size > 0:
        padding = padding + " "
        padding_size -= 1
    return padding

#returns a string to be used as a banner at the top of displays
#helper method for display functions
def display_banner(string_to_banner: str)->str:
    banner_padding = "=========="
    banner = banner_padding + string_to_banner + banner_padding
    return banner

#parsing command line arguments for different functions see help descriptions
parser = argparse.ArgumentParser()
parser.add_argument('--tasks', action='store_true', help='displays the task list')
parser.add_argument('--rewards', action='store_true', help='displays the reward list')
parser.add_argument('--credits', action='store_true', help='displays available credits')
parser.add_argument('--stats', action='store_true', help='displays statistics such as tasks completed and rewards claimed')
parser.add_argument('--achievements', action='store_true', help='displays achievements')
subparsers = parser.add_subparsers()
parser_add_task = subparsers.add_parser('add_task', help='add a task to the task list')
parser_add_task.add_argument('task_description', type=str, help='Description of task')
parser_add_task.add_argument('task_priority', type=int, choices=[1,2,3], help='Priority of task')
parser_add_task.add_argument('task_reward', type=int, choices=[1,2,3,4,5], help='Reward of task')
parser_remove_task = subparsers.add_parser('remove_task', help='removes a task from the task list by task ID only')
parser_remove_task.add_argument('remove_task_id', type=int, help='Task ID number')
parser_complete_task = subparsers.add_parser('complete_task', help='removes a task from the task list by task ID and applies reward credit(s)')
parser_complete_task.add_argument('complete_task_id', type=int, help='Task ID number')
parser_complete_task.add_argument('--repeat', action='store_true', help='Option to repeat the task, this option adds the task again after completion')
parser_add_reward = subparsers.add_parser('add_reward', help='add a reward to the reward list')
parser_add_reward.add_argument('reward_description', type=str, help='Description of reward')
parser_add_reward.add_argument('reward_cost', type=int, help='Cost of redeeming reward')
parser_remove_reward = subparsers.add_parser('remove_reward', help='removes a reward from the reward list by reward ID only')
parser_remove_reward.add_argument('remove_reward_id', type=int, help='Reward ID number')
parser_claim_reward = subparsers.add_parser('claim_reward', help='removes a reward from the rewards list by reward ID and deducts the cost from available credits')
parser_claim_reward.add_argument('claim_reward_id', type=int, help='Reward ID number')
parser_claim_reward.add_argument('--repeat', action='store_true', help='Option to repeat the reward, this option adds the reward again after completion')
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

#branch for calling display_stats()
if args.stats:
    display_stats()

#branch for calling display_achievements()
if args.achievements:
    display_achievements()

#branch for calling add_task
if 'task_description' in args and 'task_priority' in args and 'task_reward' in args:
    add_task(args.task_description,args.task_priority,args.task_reward)

#branch for calling remove_task
if 'remove_task_id' in args:
    remove_task(args.remove_task_id)

#branch for calling complete_task
if 'complete_task_id' in args:
    if args.repeat:
        complete_task(args.complete_task_id, args.repeat)
    else:
        complete_task(args.complete_task_id)

#branch for calling add_reward
if 'reward_description' in args and 'reward_cost' in args:
    add_reward(args.reward_description,args.reward_cost)

#branch for calling remove reward
if 'remove_reward_id' in args:
    remove_reward(args.remove_reward_id)

#branch for calling claim_reward
if 'claim_reward_id' in args:
    if args.repeat:
        claim_reward(args.claim_reward_id, args.repeat)
    else:
        claim_reward(args.claim_reward_id)
    
#refactored functions
#saves the tasklist to the tasklist file
#if the file does not exisit it creates it and any missing directories first
#is only called after adding a task and completing a task
#def save_tasklist():
#    if not os.path.exists(tasklist_file_path):
#        os.makedirs('data', exist_ok=True)
#        f = open(tasklist_file_path, 'x')
#        f.close()
#    with open(tasklist_file_path, 'wb') as outp:
#        #first dump is the length of the list
#        pickle.dump(len(tasklist), outp, pickle.HIGHEST_PROTOCOL)
#        for task in tasklist:
#            pickle.dump(task, outp)

#saves the rewardlist to the rewardlist file
#works similar to save_tasklist
#def save_rewardlist():
#    if not os.path.exists(rewardlist_file_path):
#        os.makedirs('data', exist_ok=True)
#        f = open(rewardlist_file_path, 'x')
#        f.close()
#    with open(rewardlist_file_path, 'wb') as outp:
#        pickle.dump(len(rewardlist), outp, pickle.HIGHEST_PROTOCOL)
#        for reward in rewardlist:
#            pickle.dump(reward, outp)

#saves the achievementlist to the achievementlist file
#def save_achievementlist():
#    if not os.path.exists(achievementlist_file_path):
#        os.makedirs('data', exist_ok=True)
#        f = open(achievementlist_file_path, 'x')
#        f.close()
#   with open(achievementlist_file_path, 'wb') as outp:
#        pickle.dump(len(achievementlist), outp, pickle.HIGHEST_PROTOCOL)
#        for achievement in achievementlist:
#            pickle.dump(achievement, outp)
#THE ABOVE 3 METHODS HAVE BEEN COMBINED INTO 1

#removes a task object from the task list only
#def remove_task(task_id: int):
#    found = False
#    for i in range(len(tasklist)):
#        if tasklist[i].id == task_id:
#            index_to_remove = i
#            found = True
#    if found:
#        del tasklist[index_to_remove]
#        save_list(tasklist_file_path)
#        print("Task Removed.")
#    else:
#        print("Task not found, check task ID.")
#removes a task object from the task list and awards credits
#def complete_task(task_id: int):
#    global credits
#    global tasks_completed
#    global high_priority_tasks_completed
#    global medium_priority_tasks_completed
#    global low_priority_tasks_completed
#    found = False
#    for i in range(len(tasklist)):
#        if tasklist[i].id == task_id:
#            index_to_remove = i
#            found = True
#            credits_to_add = tasklist[i].reward
#    if found:
#        if tasklist[index_to_remove].priority == 1:
#            high_priority_tasks_completed += 1
#        if tasklist[index_to_remove].priority == 2:
#            medium_priority_tasks_completed += 1
#        if tasklist[index_to_remove].priority == 3:
#            low_priority_tasks_completed += 1
#        tasks_completed += 1
#        credits += credits_to_add
#        del tasklist[index_to_remove]
#        save_list(tasklist_file_path)
#        save()
#        print("Task Completed.")
#        check_achievements()
#    else:
#        print("Task not found, check task ID.")
#THE ABOVE 2 METHODS WERE MODIFIED TO WORK TOGETHER

#removes a reward object from the reward list only
#def remove_reward(reward_id: int):
#    found = False
#    for i in range(len(rewardlist)):
#        if rewardlist[i].id == reward_id:
#            index_to_remove = i
#            found = True
#    if found:
#        del rewardlist[index_to_remove]
#        save_list(rewardlist_file_path)
#        print("Reward Removed.")
#    else:
#        print("Reward not found, check reward ID.")

#removes a reward object from the reward list and removes the cost from available credits
#def claim_reward(reward_id: int):
#    global credits
#    global rewards_claimed
#    found = False
#    for i in range(len(rewardlist)):
#        if rewardlist[i].id == reward_id:
#            index_to_remove = i
#            found = True
#            credits_to_deduct = rewardlist[i].cost
#    if found and credits >= credits_to_deduct:
#        credits -= credits_to_deduct
#        rewards_claimed += 1
#        del rewardlist[index_to_remove]
#        save_list(rewardlist_file_path)
#        save()
#        print("Reward Claimed.")
#        check_achievements()
#    elif not found:
#        print("Reward not found, check reward ID.")
#    else:
#        print("You don't have enough credits for that reward yet.")
#THE ABOVE 2 METHODS WERE MODIFIED TO WORK TOGETHER