import os, datetime

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

save_file_path = 'data/save.txt'

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