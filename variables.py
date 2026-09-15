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

