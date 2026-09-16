from save import save_list
from file_paths import rewardlist_file_path

class Reward:
    def __init__(self,description: str, cost: int, id: int):
        self.description = description
        self.cost = cost
        self.id = id

#add a reward object to the reward list
def add_reward(description: str, cost: int, reward_id: int, rewardlist: list):
    reward = Reward(description,cost,reward_id)
    rewardlist.append(reward)
    save_list(rewardlist_file_path, rewardlist)
    print("Reward Added.")

#removes a reward object from the reward list only
def remove_reward(reward_id: int, rewardlist: list, remove=True):
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