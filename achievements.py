from save import save_list
from file_paths import achievementlist_file_path

class Achievement:
    def __init__(self,description: str, completed: bool, reward: int, required_stat: str, required_value: int):
        self.description = description
        self.completed = completed
        self.reward = reward
        self.required_stat = required_stat
        self.required_value = required_value

#populates the achievement_list
def populate_achievement_list(achievementlist: list)->list:
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
    return achievementlist

#helper method for check_achievements
#takes a required statistic to check and the required value
#returns true if the requirements have been met, false otherwise
def check_achievement(required_stat: str, required_value: int, tasks_completed: int, high_priority_tasks_completed: int, medium_priority_tasks_completed: int, low_priority_tasks_completed: int, rewards_claimed: int)->bool:
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
def check_achievements(achievementlist: list, variableslist: list, tasks_completed: int, high_priority_tasks_completed: int, medium_priority_tasks_completed: int, low_priority_tasks_completed: int, rewards_claimed: int)->int:
    credits_to_add = 0
    if achievementlist == []:
        populate_achievement_list(achievementlist)
        save_list(achievementlist_file_path, achievementlist)
    else:
        for achievement in achievementlist:
            if not achievement.completed:
                completed = check_achievement(achievement.required_stat,achievement.required_value,tasks_completed,high_priority_tasks_completed,medium_priority_tasks_completed,low_priority_tasks_completed,rewards_claimed)
                if completed:
                    achievement.completed = True
                    credits_to_add += achievement.reward
                    print(f"Achievement completed: {achievement.description} | You have been rewarded {achievement.reward} credits!")
                    save_list(achievementlist_file_path, achievementlist)
    return credits_to_add