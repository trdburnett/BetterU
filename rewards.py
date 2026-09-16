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