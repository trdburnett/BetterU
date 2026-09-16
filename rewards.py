from operator import attrgetter
from save import save_list
from file_paths import rewardlist_file_path
from achievements import check_achievements
from display import display_banner, display_padding, display_credits

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
def remove_reward(reward_id: int, rewardlist: list, credits:int, remove=True):
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
def claim_reward(reward_id: int, rewardlist: int, credits: int, achievementlist: list, tasks_completed: int, high_priority_tasks_completed: int, medium_priority_tasks_completed: int, low_priority_tasks_completed: int, rewards_claimed: int, repeat=False):
    credits_to_add = 0
    rewards_claimed_to_add = 0
    dc = remove_reward(reward_id, rewardlist, credits, False)
    if not dc[0] == None and not dc[1] == None:
        credits_to_add -= dc[1]
        rewards_claimed_to_add += 1
        print(f"Reward Claimed, {dc[1]} credit(s) have been deducted.")
        credits_to_add += check_achievements(achievementlist,tasks_completed,high_priority_tasks_completed,medium_priority_tasks_completed,low_priority_tasks_completed,rewards_claimed)
        if repeat:
            add_reward(dc[0],dc[1],reward_id,rewardlist)
    return (credits_to_add,rewards_claimed_to_add)

#displays the rewards list in cost order
def display_rewards(rewardlist: list, credits: int):
    if rewardlist == []:
        print("No rewards to display. please add some rewards.")
    else:
        display_credits(credits)
        print(display_banner("Rewards"))
        sorted_rewardlist = sorted(rewardlist, key=attrgetter('cost'))
        for reward in sorted_rewardlist:
            print(f"Reward[{reward.id}]: {reward.description}{display_padding(reward.description)}| Cost: {reward.cost} Credits")