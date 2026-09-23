import datetime, argparse, os
from save import save, save_list
from load import load_list
from file_paths import  save_file_path, tasklist_file_path, rewardlist_file_path, achievementlist_file_path
from tasks import Task, add_task, remove_task, complete_task, display_tasks
from rewards import Reward, add_reward, remove_reward, claim_reward, display_rewards
from achievements import Achievement, display_achievements, check_achievements
from streak import daily_reward
from display import display_stats, display_credits

if __name__ == "__main__":
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
    freeze = 0

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
                if "Freeze" in line:
                    freeze += int((line.lstrip("Freeze: ")).rstrip(" \n"))
#loads lists and sets id tracking
    tasklist = load_list(tasklist_file_path)
    task_id += getmax_id("task")
    rewardlist = load_list(rewardlist_file_path)
    reward_id += getmax_id("reward")
    achievementlist = load_list(achievementlist_file_path)

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
        display_tasks(tasklist)

#branch for calling display_rewards()
    if args.rewards:
        display_rewards(rewardlist, credits)

#branch for calling display_credits()
    if args.credits:
        display_credits(credits)

#branch for calling display_stats()
    if args.stats:
        display_stats(tasks_completed, high_priority_tasks_completed, medium_priority_tasks_completed, low_priority_tasks_completed, rewards_claimed, streak)

#branch for calling display_achievements()
    if args.achievements:
        achievementlist = display_achievements(achievementlist)
        save_list(achievementlist_file_path, achievementlist)

#branch for calling add_task
    if 'task_description' in args and 'task_priority' in args and 'task_reward' in args:
        tasklist = add_task(args.task_description, args.task_priority, args.task_reward, task_id, tasklist)
        save_list(tasklist_file_path, tasklist)

#branch for calling remove_task
    if 'remove_task_id' in args:
        tasklist = remove_task(args.remove_task_id, tasklist)
        save_list(tasklist_file_path, tasklist)

#branch for calling complete_task
    if 'complete_task_id' in args:
        if args.repeat:
            retdict_ct = complete_task(args.complete_task_id, tasklist, args.repeat)
        else:
            retdict_ct = complete_task(args.complete_task_id, tasklist)
        credits += retdict_ct["credits_to_add"]
        tasks_completed += retdict_ct["tasks_completed_to_add"]
        high_priority_tasks_completed += retdict_ct["high_priority_tasks_completed_to_add"]
        medium_priority_tasks_completed += retdict_ct["medium_priority_tasks_completed_to_add"]
        low_priority_tasks_completed += retdict_ct["low_priority_tasks_completed_to_add"]
        tasklist = retdict_ct["tasklist"]
        retdict_dr = daily_reward(time.now(), last_accessed, streak, freeze)
        last_accessed = retdict_dr["last_accessed"]
        credits += retdict_dr["credits_to_add"]
        streak += retdict_dr["streak_to_add"]
        freeze += retdict_dr["freeze_to_add"]
        retdict_ca = check_achievements(achievementlist,tasks_completed,high_priority_tasks_completed,medium_priority_tasks_completed,low_priority_tasks_completed,rewards_claimed)
        credits += retdict_ca["credits_to_add"]
        achievementlist = retdict_ca["achievementlist"]
        save(save_file_path, credits, high_priority_tasks_completed, medium_priority_tasks_completed, low_priority_tasks_completed, tasks_completed, rewards_claimed, last_accessed, streak, freeze)
        save_list(tasklist_file_path, tasklist)
        save_list(achievementlist_file_path, achievementlist)

#branch for calling add_reward
    if 'reward_description' in args and 'reward_cost' in args:
        rewardlist = add_reward(args.reward_description, args.reward_cost, reward_id, rewardlist)
        save_list(rewardlist_file_path, rewardlist)

#branch for calling remove reward
    if 'remove_reward_id' in args:
        rewardlist = remove_reward(args.remove_reward_id, rewardlist, credits)
        save_list(rewardlist_file_path, rewardlist)

#branch for calling claim_reward
    if 'claim_reward_id' in args:
        if args.repeat:
            retdict_cr = claim_reward(args.claim_reward_id, rewardlist, credits, args.repeat)
        else:
            retdict_cr = claim_reward(args.claim_reward_id, rewardlist, credits)
        credits += retdict_cr["credits_to_add"]
        rewards_claimed += retdict_cr["rewards_claimed_to_add"]
        rewardlist = retdict_cr["rewardlist"]
        retdict_ca = check_achievements(achievementlist,tasks_completed,high_priority_tasks_completed,medium_priority_tasks_completed,low_priority_tasks_completed,rewards_claimed)
        credits += retdict_ca["credits_to_add"]
        achievementlist = retdict_ca["achievementlist"]
        save(save_file_path, credits, high_priority_tasks_completed, medium_priority_tasks_completed, low_priority_tasks_completed, tasks_completed, rewards_claimed, last_accessed, streak, freeze)
        save_list(rewardlist_file_path, rewardlist)
        save_list(achievementlist_file_path, achievementlist)