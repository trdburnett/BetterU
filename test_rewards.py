import unittest
from rewards import Reward, add_reward, remove_reward, claim_reward

class TestRewards(unittest.TestCase):

    def test_reward_class(self):
        reward = Reward("Test Reward",1,1)
        self.assertEqual(reward.description, "Test Reward")
        self.assertEqual(reward.cost, 1)
        self.assertEqual(reward.id, 1)

    def test_add_reward(self):
        testrewardlist = [Reward("Test Reward",1,1)]
        rewardlist = add_reward("Test Reward",1,1,[])
        self.assertEqual(rewardlist[0].description, testrewardlist[0].description)
        self.assertEqual(rewardlist[0].cost, testrewardlist[0].cost)
        self.assertEqual(rewardlist[0].id, testrewardlist[0].id)

    def test_remove_reward_valid_not_called_by_claim_reward(self):
        testreward_id = 1
        testrewardlist = [Reward("Test Reward",1,1)]
        testcredits = 1
        self.assertEqual(remove_reward(testreward_id,testrewardlist,testcredits), [])

    def test_remove_reward_invalid_not_called_by_claim_reward(self):
        testreward_id = 2
        testrewardlist = [Reward("Test Reward",1,1)]
        testcredits = 1
        self.assertEqual(remove_reward(testreward_id,testrewardlist,testcredits), testrewardlist)

    def test_remove_reward_valid_called_by_claim_reward(self):
        testreward_id = 1
        testrewardlist = [Reward("Test Reward",1,1)]
        testcredits = 1
        expected_result = {"description": "Test Reward",
                           "cost": 1,
                           "rewardlist": []}
        self.assertEqual(remove_reward(testreward_id,testrewardlist,testcredits,True), expected_result)

    def test_remove_reward_invalid_not_found_called_by_claim_reward(self):
        testreward_id = 2
        testrewardlist = [Reward("Test Reward",1,1)]
        testcredits = 1
        self.assertEqual(remove_reward(testreward_id,testrewardlist,testcredits,True), None)

    def test_remove_reward_invalid_not_enough_credits_called_by_claim_reward(self):
        testreward_id = 1
        testrewardlist = [Reward("Test Reward",1,1)]
        testcredits = 0
        self.assertEqual(remove_reward(testreward_id,testrewardlist,testcredits,True), None)

    def test_claim_reward_valid(self):
        testreward_id = 1
        testrewardlist = [Reward("Test Reward",1,1)]
        testcredits = 1
        expected_result = {"credits_to_add": -1,
                           "rewards_claimed_to_add": 1,
                           "rewardlist": []}
        self.assertEqual(claim_reward(testreward_id,testrewardlist,testcredits), expected_result)

    def test_claim_reward_valid_repeat(self):
        testreward_id = 1
        testrewardlist = [Reward("Test Reward",1,1)]
        testcredits = 1
        expected_result = {"credits_to_add": -1,
                           "rewards_claimed_to_add": 1,
                           "rewardlist": testrewardlist}
        self.assertEqual(claim_reward(testreward_id,testrewardlist,testcredits,True), expected_result)

    def test_claim_reward_invalid_not_found(self):
        testreward_id = 2
        testrewardlist = [Reward("Test Reward",1,1)]
        testcredits = 1
        expected_result = {"credits_to_add": 0,
                           "rewards_claimed_to_add": 0,
                           "rewardlist": testrewardlist}
        self.assertEqual(claim_reward(testreward_id,testrewardlist,testcredits), expected_result)

    def test_claim_reward_invalid_not_found_repeat(self):
        testreward_id = 2
        testrewardlist = [Reward("Test Reward",1,1)]
        testcredits = 1
        expected_result = {"credits_to_add": 0,
                           "rewards_claimed_to_add": 0,
                           "rewardlist": testrewardlist}
        self.assertEqual(claim_reward(testreward_id,testrewardlist,testcredits,True), expected_result)

    def test_claim_reward_invalid_not_enough_credits(self):
        testreward_id = 1
        testrewardlist = [Reward("Test Reward",1,1)]
        testcredits = 0
        expected_result = {"credits_to_add": 0,
                           "rewards_claimed_to_add": 0,
                           "rewardlist": testrewardlist}
        self.assertEqual(claim_reward(testreward_id,testrewardlist,testcredits), expected_result)

    def test_claim_reward_invalid_not_enough_credits_repeat(self):
        testreward_id = 1
        testrewardlist = [Reward("Test Reward",1,1)]
        testcredits = 0
        expected_result = {"credits_to_add": 0,
                           "rewards_claimed_to_add": 0,
                           "rewardlist": testrewardlist}
        self.assertEqual(claim_reward(testreward_id,testrewardlist,testcredits,True), expected_result)

if __name__ == "__main__":
    unittest.main()