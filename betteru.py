import datetime, argparse, os
from operator import attrgetter
from save import save_list, save
from load import load_list
from file_paths import  save_file_path, tasklist_file_path, rewardlist_file_path, achievementlist_file_path
from tasks import Task, add_task, remove_task
from achievements import Achievement, populate_achievement_list

time = datetime.datetime
tasklist = []
rewardlist = []
achievementlist = []
credits = 0
task_id = 1
reward_id = 1
tasks_completed = 0
high_priority_tasks_completed = 0
medium_priority_tasks_completed = 0
low_priority_tasks_completed = 0
rewards_claimed = 0
last_accessed = None
streak = 0

class Reward:
    def __init__(self,description: str, cost: int, id: int):
        self.description = description
        self.cost = cost
        self.id = id



#cycles through the tasks/rewards list based on mode and returns highest found ID
#used to add to task_id/reward_id which is initialised at 1
#ensures all tasks and rewards have a unique ID 
def getmax_id(mode:str)->int:
    max_id = 0
    if mode == "task":
        for task in tasklist:
            if task.id > max_id:
                max_id = task.id
    if mode == "reward":
        for reward in rewardlist:
            if reward.id > max_id:
                max_id = reward.id
    return max_id

#checks to see if data/save.txt exisits
#if it does it loads the values and sets variables used in the program
def load_variables():
    global credits
    global high_priority_tasks_completed
    global medium_priority_tasks_completed
    global low_priority_tasks_completed
    global tasks_completed
    global rewards_claimed
    global last_accessed
    global streak
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
                #as last_accessed is a datetime object the below converts the extracted string to a datetime object and saves it the last_accessed variable
                if "Last Accessed" in line:
                    date_str = ((line.lstrip("Last Accessed: ")).rstrip(" \n"))
                    date_format = '%Y-%m-%d %H:%M:%S.%f'
                    last_accessed = datetime.datetime.strptime(date_str, date_format)
                if "Streak" in line:
                    streak += int((line.lstrip("Streak: ")).rstrip(" \n"))

load_variables()
tasklist = load_list(tasklist_file_path)
task_id += getmax_id("task")
rewardlist = load_list(rewardlist_file_path)
reward_id += getmax_id("reward")
achievementlist = load_list(achievementlist_file_path)

#packages the simple variables into a list ready for saving
def variables_as_list():
    variablelist = []
    variablelist.append(f"Credits: {credits} \n")
    variablelist.append(f"High Priority Tasks Completed: {high_priority_tasks_completed} \n")
    variablelist.append(f"Medium Priority Tasks Completed: {medium_priority_tasks_completed} \n")
    variablelist.append(f"Low Priority Tasks Completed: {low_priority_tasks_completed} \n")
    variablelist.append(f"Tasks Completed: {tasks_completed} \n")
    variablelist.append(f"Rewards Claimed: {rewards_claimed} \n")
    variablelist.append(f"Last Accessed: {last_accessed} \n")
    variablelist.append(f"Streak: {streak} \n")
    return variablelist

#helper for daily reward
#checks if last_accessed day was yesterday to be used in the event that it had been less than 24 hours
def yesterday_check(last_accessed_day: str, access_day: str) -> bool:
    yesterday = False
    if last_accessed_day == "Monday":
        if access_day == "Sunday":
            yesterday = True
    if last_accessed_day == "Tuesday":
        if access_day == "Monday":
            yesterday = True
    if last_accessed_day == "Wednesday":
        if access_day == "Tuesday":
            yesterday = True
    if last_accessed_day == "Thursday":
        if access_day == "Wednesday":
            yesterday = True
    if last_accessed_day == "Friday":
        if access_day == "Thursday":
            yesterday = True
    if last_accessed_day == "Saturday":
        if access_day == "Friday":
            yesterday = True
    if last_accessed_day == "Sunday":
        if access_day == "Saturday":
            yesterday = True
    return yesterday

#helper for daily reward
#resets streak when not upheld
def streak_reset():
    global streak
    streak = 0

#called by complete task
#checks the last time a task was completed and if it is a new day displays a welcome message and applies a credit
def daily_reward(access_time: datetime):
    global last_accessed
    global credits
    global streak
    access_day = access_time.strftime("%A")
    if last_accessed == None:
        last_accessed = access_time
        credits += 1
        print("Looks like this your first time. You have been awarded a credit to help motivate you on your task completion journey!")
        save(save_file_path, variables_as_list())
        return
    elif last_accessed <= access_time - datetime.timedelta(days=1):
        credits += 1
        streak_reset()
        last_accessed = access_time
        print("Looks like its been more than a day. You have been awarded a credit to get you motivated!")
        save(save_file_path, variables_as_list())
        return
    elif yesterday_check(last_accessed.strftime("%A"),access_day):
        credits += 1
        streak += 1
        last_accessed = access_time
        print(f"You are getting things done! Have a productive {access_day}. You have increased your streak to {streak} days and been awarded your daily credit!")
        if streak % 7 == 0:
            streak_weeks = streak / 7
            if streak_weeks % 4 == 0:
                streak_months = streak_weeks / 4
                if streak_months % 13 == 0:
                    credits += 100
                    streak_reset()
                    print(f"Amazing you have been getting tasks done for whole year! Your streak has now been reset and you have been awarded 100 credits")
                else:
                    credits += 28
                    print(f"Congratulations on reaching a streak of {streak_months} month(s)! You have awarded 28 credits")
            else:    
                credits += 7
                print(f"Congratulations on reaching a streak of {streak_weeks} week(s)! You have been awarded 7 credits")
        save(save_file_path, variables_as_list())
        return
    elif last_accessed > access_time:
        print(f"Well that is naughty, how has modifiying the last accessed time to the future helped you get things done?")
        return



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

#called by complete task
#performs a check for the achievement list if it is empty it calls the populate and save achievement functions respectively
#otherwise applies credits and alerts user if an achievement has been completed
def check_achievements():
    global credits
    if achievementlist == []:
        populate_achievement_list(achievementlist)
        save_list(achievementlist_file_path, achievementlist)
    else:
        for achievement in achievementlist:
            if not achievement.completed:
                completed = check_achievement(achievement.required_stat,achievement.required_value)
                if completed:
                    achievement.completed = True
                    credits += achievement.reward
                    save(save_file_path, variables_as_list())
                    print(f"Achievement completed: {achievement.description} | You have been rewarded {achievement.reward} credits!")
                    save_list(achievementlist_file_path, achievementlist)

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
def complete_task(task_id: int, repeat=False):
    global credits
    global tasks_completed
    global high_priority_tasks_completed
    global medium_priority_tasks_completed
    global low_priority_tasks_completed
    dprt = remove_task(task_id, tasklist, remove=False)
    if not dprt[0] == None and not dprt[1] == None and not dprt[2] == None and not dprt[3] == None:
        if dprt[1] == 1:
            high_priority_tasks_completed += 1
        if dprt[1] == 2:
            medium_priority_tasks_completed += 1
        if dprt[1] == 3:
            low_priority_tasks_completed += 1
        tasks_completed += 1
        t = time_remaining(dprt[1],dprt[3])
        if t == "Expired!":
            print(f"Task Completed, however no credits have been awarded due to the task not being completed in time.")
        else:
            credits += dprt[2]
            print(f"Task Completed, you have been awarded {dprt[2]} credit(s)")
        save(save_file_path, variables_as_list())
        daily_reward(time.now())
        check_achievements()
        if repeat:
            add_task(dprt[0],dprt[1],dprt[2],task_id,tasklist)

#add a reward object to the reward list
def add_reward(description: str, cost: int):
    reward = Reward(description,cost,reward_id)
    rewardlist.append(reward)
    save_list(rewardlist_file_path, rewardlist)
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
            save_list(rewardlist_file_path, rewardlist)
            print("Reward Removed.")
        else:
            if cost <= credits:
                del rewardlist[index_to_remove]
                save_list(rewardlist_file_path, rewardlist)
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
        save(save_file_path, variables_as_list())
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
            print(f"Task[{task.id}]: {task.description}{display_padding(task.description)}| Reward: {task.reward} Credits | Time Remaining: {time_remaining(task.priority,task.time)}")

#displays the rewards list in cost order
def display_rewards():
    if rewardlist == []:
        print("No rewards to display. please add some rewards.")
    else:
        display_credits()
        print(display_banner("Rewards"))
        sorted_rewardlist = sorted(rewardlist, key=attrgetter('cost'))
        for reward in sorted_rewardlist:
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
    left_banner_padding = "==============================["
    right_banner_padding = "]========================="
    uniform_padding = ""
    uniform_padding_size = 20 - len(string_to_banner)
    while uniform_padding_size > 0:
        uniform_padding = uniform_padding + "="
        uniform_padding_size -= 1
    banner = left_banner_padding + string_to_banner + right_banner_padding + uniform_padding
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
    add_task(args.task_description,args.task_priority,args.task_reward,task_id,tasklist)

#branch for calling remove_task
if 'remove_task_id' in args:
    remove_task(args.remove_task_id, tasklist)

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