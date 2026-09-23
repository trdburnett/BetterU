import os, pickle, datetime

#saves a list to the given lists filepath
def save_list(file_path: str, savelist: list):
    if not os.path.exists(file_path):
        os.makedirs('data', exist_ok=True)
        f = open(file_path, 'x')
        f.close()
    with open(file_path, 'wb') as outp:
        pickle.dump(len(savelist), outp, pickle.HIGHEST_PROTOCOL)
        for item in savelist:
            pickle.dump(item, outp)

#helper for save function
#packages the simple variables into a list ready for saving
def variables_as_list(credits: int, high_priority_tasks_completed: int, medium_priority_tasks_completed: int, low_priority_tasks_completed: int, tasks_completed: int, rewards_claimed: int, last_accessed: datetime, streak: int, freeze: int):
    variablelist = []
    variablelist.append(f"Credits: {credits} \n")
    variablelist.append(f"High Priority Tasks Completed: {high_priority_tasks_completed} \n")
    variablelist.append(f"Medium Priority Tasks Completed: {medium_priority_tasks_completed} \n")
    variablelist.append(f"Low Priority Tasks Completed: {low_priority_tasks_completed} \n")
    variablelist.append(f"Tasks Completed: {tasks_completed} \n")
    variablelist.append(f"Rewards Claimed: {rewards_claimed} \n")
    variablelist.append(f"Last Accessed: {last_accessed} \n")
    variablelist.append(f"Streak: {streak} \n")
    variablelist.append(f"Freeze: {freeze} \n")
    return variablelist

#saves all simple variables used by the program
#saves given list as plain text at given file path
def save(save_file_path: str, credits: int, high_priority_tasks_completed: int, medium_priority_tasks_completed: int, low_priority_tasks_completed: int, tasks_completed: int, rewards_claimed: int, last_accessed: datetime, streak: int, freeze: int):
    variablelist = variables_as_list(credits, high_priority_tasks_completed, medium_priority_tasks_completed, low_priority_tasks_completed, tasks_completed, rewards_claimed, last_accessed, streak, freeze)
    if not os.path.exists(save_file_path):
        os.makedirs('data', exist_ok=True)
        f = open(save_file_path, 'x')
        f.close()
    with open(save_file_path, 'w') as f:
        for variable in variablelist:
            f.write(variable)
