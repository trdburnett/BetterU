from operator import attrgetter
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
    print("Reward Added.")
    return rewardlist

#removes a reward object from the reward list only
def remove_reward(reward_id: int, rewardlist: list, credits:int, called_from_claim_reward=False):
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
        if not called_from_claim_reward:
            del rewardlist[index_to_remove]
            print("Reward Removed.")
            return rewardlist
        else:
            if cost <= credits:
                del rewardlist[index_to_remove]
                return {"description": description,
                        "cost": cost,
                        "rewardlist": rewardlist}
            else:
                print("You don't have enough credits for that reward yet.")
                return None
    else:
        print("Reward not found, check reward ID.")
        if called_from_claim_reward:
            return None
        else:
            return rewardlist

#removes a reward object from the reward list and removes the cost from available credits
def claim_reward(reward_id: int, rewardlist: int, credits: int, repeat=False)->dict:
    credits_to_add = 0
    rewards_claimed_to_add = 0
    retdict_rr = remove_reward(reward_id, rewardlist, credits, called_from_claim_reward=True)
    if not retdict_rr == None:
        credits_to_add -= retdict_rr["cost"]
        rewards_claimed_to_add += 1
        print(f"Reward Claimed, {retdict_rr["cost"]} credit(s) have been deducted.")
        if repeat:
            rewardlist = add_reward(retdict_rr["description"],retdict_rr["cost"],reward_id,retdict_rr["rewardlist"])
        else:
            rewardlist = retdict_rr["rewardlist"]
    return {"credits_to_add": credits_to_add,
            "rewards_claimed_to_add": rewards_claimed_to_add,
            "rewardlist": rewardlist}

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