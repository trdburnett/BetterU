import unittest
from achievements import Achievement, populate_achievement_list, check_achievement, check_achievements

class TestAchievements(unittest.TestCase):

    def test_populate_achievement_list(self):
        testachievementlist = [Achievement("Completed 10 Tasks",False,2,"tasks_completed",10),
                               Achievement("Completed 50 Tasks",False,10,"tasks_completed",50),
                               Achievement("Completed 100 Tasks",False,20,"tasks_completed",100),
                               Achievement("Completed 500 Tasks",False,100,"tasks_completed",500),
                               Achievement("Completed 1000 Tasks",False,200,"tasks_completed",1000),
                               Achievement("Completed 5000 Tasks",False,1000,"tasks_completed",5000),
                               Achievement("Completed 10000 Tasks",False,2000,"tasks_completed",10000),
                               Achievement("Completed 20 High Priority Tasks",False,2,"high_priority_tasks_completed",20),
                               Achievement("Completed 100 High Priority Tasks",False,10,"high_priority_tasks_completed",100),
                               Achievement("Completed 200 High Priority Tasks",False,20,"high_priority_tasks_completed",200),
                               Achievement("Completed 1000 High Priority Tasks",False,100,"high_priority_tasks_completed",1000),
                               Achievement("Completed 40 Medium Priority Tasks",False,2,"medium_priority_tasks_completed",40),
                               Achievement("Completed 200 Medium Priority Tasks",False,10,"medium_priority_tasks_completed",200),
                               Achievement("Completed 400 Medium Priority Tasks",False,20,"medium_priority_tasks_completed",400),
                               Achievement("Completed 2000 Medium Priority Tasks",False,100,"medium_priority_tasks_completed",2000),
                               Achievement("Completed 80 Low Priority Tasks",False,2,"low_priority_tasks_completed",80),
                               Achievement("Completed 400 Low Priority Tasks",False,10,"low_priority_tasks_completed",400),
                               Achievement("Completed 800 Low Priority Tasks",False,20,"low_priority_tasks_completed",800),
                               Achievement("Completed 4000 Low Priority Tasks",False,100,"low_priority_tasks_completed",4000),
                               Achievement("Claimed 5 Rewards",False,2,"rewards_claimed",5),
                               Achievement("Claimed 25 Rewards",False,10,"rewards_claimed",25),
                               Achievement("Claimed 50 Rewards",False,20,"rewards_claimed",50),
                               Achievement("Claimed 250 Rewards",False,100,"rewards_claimed",250)]
        self.assertEqual(populate_achievement_list([]), testachievementlist)

    def test_check_achievement_tasks_completed_met(self):
        testrequired_stat = "tasks_completed"
        testrequired_value = 10 
        testtasks_completed = 10
        testhigh_priority_tasks_completed = 10
        testmedium_priority_tasks_completed = 0 
        testlow_priority_tasks_completed = 0
        testrewards_claimed = 0
        self.assertEqual(check_achievement(testrequired_stat,testrequired_value,testtasks_completed,testhigh_priority_tasks_completed,testmedium_priority_tasks_completed,testlow_priority_tasks_completed,testrewards_claimed), True)

    def test_check_achievement_tasks_completed_not_met(self):
        testrequired_stat = "tasks_completed"
        testrequired_value = 10 
        testtasks_completed = 9
        testhigh_priority_tasks_completed = 9
        testmedium_priority_tasks_completed = 0 
        testlow_priority_tasks_completed = 0
        testrewards_claimed = 0
        self.assertEqual(check_achievement(testrequired_stat,testrequired_value,testtasks_completed,testhigh_priority_tasks_completed,testmedium_priority_tasks_completed,testlow_priority_tasks_completed,testrewards_claimed), False)

    def test_check_achievement_high_priority_tasks_completed_met(self):
        testrequired_stat = "high_priority_tasks_completed"
        testrequired_value = 20 
        testtasks_completed = 20
        testhigh_priority_tasks_completed = 20
        testmedium_priority_tasks_completed = 0 
        testlow_priority_tasks_completed = 0
        testrewards_claimed = 0
        self.assertEqual(check_achievement(testrequired_stat,testrequired_value,testtasks_completed,testhigh_priority_tasks_completed,testmedium_priority_tasks_completed,testlow_priority_tasks_completed,testrewards_claimed), True)

    def test_check_achievement_high_priority_tasks_completed_not_met(self):
        testrequired_stat = "high_priority_tasks_completed"
        testrequired_value = 20 
        testtasks_completed = 19
        testhigh_priority_tasks_completed = 19
        testmedium_priority_tasks_completed = 0 
        testlow_priority_tasks_completed = 0
        testrewards_claimed = 0
        self.assertEqual(check_achievement(testrequired_stat,testrequired_value,testtasks_completed,testhigh_priority_tasks_completed,testmedium_priority_tasks_completed,testlow_priority_tasks_completed,testrewards_claimed), False)

    def test_check_achievement_medium_priority_tasks_completed_met(self):
        testrequired_stat = "medium_priority_tasks_completed"
        testrequired_value = 40 
        testtasks_completed = 40
        testhigh_priority_tasks_completed = 0
        testmedium_priority_tasks_completed = 40 
        testlow_priority_tasks_completed = 0
        testrewards_claimed = 0
        self.assertEqual(check_achievement(testrequired_stat,testrequired_value,testtasks_completed,testhigh_priority_tasks_completed,testmedium_priority_tasks_completed,testlow_priority_tasks_completed,testrewards_claimed), True)

    def test_check_achievement_medium_priority_tasks_completed_not_met(self):
        testrequired_stat = "medium_priority_tasks_completed"
        testrequired_value = 40 
        testtasks_completed = 39
        testhigh_priority_tasks_completed = 0
        testmedium_priority_tasks_completed = 39 
        testlow_priority_tasks_completed = 0
        testrewards_claimed = 0
        self.assertEqual(check_achievement(testrequired_stat,testrequired_value,testtasks_completed,testhigh_priority_tasks_completed,testmedium_priority_tasks_completed,testlow_priority_tasks_completed,testrewards_claimed), False)

    def test_check_achievement_low_priority_tasks_completed_met(self):
        testrequired_stat = "low_priority_tasks_completed"
        testrequired_value = 80 
        testtasks_completed = 80
        testhigh_priority_tasks_completed = 0
        testmedium_priority_tasks_completed = 0 
        testlow_priority_tasks_completed = 80
        testrewards_claimed = 0
        self.assertEqual(check_achievement(testrequired_stat,testrequired_value,testtasks_completed,testhigh_priority_tasks_completed,testmedium_priority_tasks_completed,testlow_priority_tasks_completed,testrewards_claimed), True)

    def test_check_achievement_low_priority_tasks_completed_not_met(self):
        testrequired_stat = "low_priority_tasks_completed"
        testrequired_value = 80 
        testtasks_completed = 79
        testhigh_priority_tasks_completed = 0
        testmedium_priority_tasks_completed = 0 
        testlow_priority_tasks_completed = 79
        testrewards_claimed = 0
        self.assertEqual(check_achievement(testrequired_stat,testrequired_value,testtasks_completed,testhigh_priority_tasks_completed,testmedium_priority_tasks_completed,testlow_priority_tasks_completed,testrewards_claimed), False)

    def test_check_achievement_rewards_claimed_met(self):
        testrequired_stat = "rewards_claimed"
        testrequired_value = 5 
        testtasks_completed = 80
        testhigh_priority_tasks_completed = 0
        testmedium_priority_tasks_completed = 0 
        testlow_priority_tasks_completed = 80
        testrewards_claimed = 5
        self.assertEqual(check_achievement(testrequired_stat,testrequired_value,testtasks_completed,testhigh_priority_tasks_completed,testmedium_priority_tasks_completed,testlow_priority_tasks_completed,testrewards_claimed), True)

    def test_check_achievement_rewards_claimed_not_met(self):
        testrequired_stat = "rewards_claimed"
        testrequired_value = 5 
        testtasks_completed = 80
        testhigh_priority_tasks_completed = 0
        testmedium_priority_tasks_completed = 0 
        testlow_priority_tasks_completed = 80
        testrewards_claimed = 4
        self.assertEqual(check_achievement(testrequired_stat,testrequired_value,testtasks_completed,testhigh_priority_tasks_completed,testmedium_priority_tasks_completed,testlow_priority_tasks_completed,testrewards_claimed), False)

    def test_check_achievements_all_completed_empty_list(self):
        testachievementlist = []
        testtasks_completed = 10000
        testhigh_priority_tasks_completed = 2000
        testmedium_priority_tasks_completed = 3000
        testlow_priority_tasks_completed = 5000
        testrewards_claimed = 250
        testresultachievementlist = [Achievement("Completed 10 Tasks",True,2,"tasks_completed",10),
                                     Achievement("Completed 50 Tasks",True,10,"tasks_completed",50),
                                     Achievement("Completed 100 Tasks",True,20,"tasks_completed",100),
                                     Achievement("Completed 500 Tasks",True,100,"tasks_completed",500),
                                     Achievement("Completed 1000 Tasks",True,200,"tasks_completed",1000),
                                     Achievement("Completed 5000 Tasks",True,1000,"tasks_completed",5000),
                                     Achievement("Completed 10000 Tasks",True,2000,"tasks_completed",10000),
                                     Achievement("Completed 20 High Priority Tasks",True,2,"high_priority_tasks_completed",20),
                                     Achievement("Completed 100 High Priority Tasks",True,10,"high_priority_tasks_completed",100),
                                     Achievement("Completed 200 High Priority Tasks",True,20,"high_priority_tasks_completed",200),
                                     Achievement("Completed 1000 High Priority Tasks",True,100,"high_priority_tasks_completed",1000),
                                     Achievement("Completed 40 Medium Priority Tasks",True,2,"medium_priority_tasks_completed",40),
                                     Achievement("Completed 200 Medium Priority Tasks",True,10,"medium_priority_tasks_completed",200),
                                     Achievement("Completed 400 Medium Priority Tasks",True,20,"medium_priority_tasks_completed",400),
                                     Achievement("Completed 2000 Medium Priority Tasks",True,100,"medium_priority_tasks_completed",2000),
                                     Achievement("Completed 80 Low Priority Tasks",True,2,"low_priority_tasks_completed",80),
                                     Achievement("Completed 400 Low Priority Tasks",True,10,"low_priority_tasks_completed",400),
                                     Achievement("Completed 800 Low Priority Tasks",True,20,"low_priority_tasks_completed",800),
                                     Achievement("Completed 4000 Low Priority Tasks",True,100,"low_priority_tasks_completed",4000),
                                     Achievement("Claimed 5 Rewards",True,2,"rewards_claimed",5),
                                     Achievement("Claimed 25 Rewards",True,10,"rewards_claimed",25),
                                     Achievement("Claimed 50 Rewards",True,20,"rewards_claimed",50),
                                     Achievement("Claimed 250 Rewards",True,100,"rewards_claimed",250)]
        expected_result = {"credits_to_add": 3860,
                           "achievementlist": testresultachievementlist}
        self.assertEqual(check_achievements(testachievementlist,testtasks_completed,testhigh_priority_tasks_completed,testmedium_priority_tasks_completed,testlow_priority_tasks_completed,testrewards_claimed), expected_result)

    def test_check_achievements_all_completed_populated_list_some_achievements_already_met(self):
        testachievementlist = [Achievement("Completed 10 Tasks",True,2,"tasks_completed",10),
                               Achievement("Completed 50 Tasks",True,10,"tasks_completed",50),
                               Achievement("Completed 100 Tasks",True,20,"tasks_completed",100),
                               Achievement("Completed 500 Tasks",True,100,"tasks_completed",500),
                               Achievement("Completed 1000 Tasks",True,200,"tasks_completed",1000),
                               Achievement("Completed 5000 Tasks",True,1000,"tasks_completed",5000),
                               Achievement("Completed 10000 Tasks",False,2000,"tasks_completed",10000),
                               Achievement("Completed 20 High Priority Tasks",True,2,"high_priority_tasks_completed",20),
                               Achievement("Completed 100 High Priority Tasks",True,10,"high_priority_tasks_completed",100),
                               Achievement("Completed 200 High Priority Tasks",True,20,"high_priority_tasks_completed",200),
                               Achievement("Completed 1000 High Priority Tasks",True,100,"high_priority_tasks_completed",1000),
                               Achievement("Completed 40 Medium Priority Tasks",True,2,"medium_priority_tasks_completed",40),
                               Achievement("Completed 200 Medium Priority Tasks",True,10,"medium_priority_tasks_completed",200),
                               Achievement("Completed 400 Medium Priority Tasks",True,20,"medium_priority_tasks_completed",400),
                               Achievement("Completed 2000 Medium Priority Tasks",True,100,"medium_priority_tasks_completed",2000),
                               Achievement("Completed 80 Low Priority Tasks",True,2,"low_priority_tasks_completed",80),
                               Achievement("Completed 400 Low Priority Tasks",True,10,"low_priority_tasks_completed",400),
                               Achievement("Completed 800 Low Priority Tasks",True,20,"low_priority_tasks_completed",800),
                               Achievement("Completed 4000 Low Priority Tasks",True,100,"low_priority_tasks_completed",4000),
                               Achievement("Claimed 5 Rewards",True,2,"rewards_claimed",5),
                               Achievement("Claimed 25 Rewards",True,10,"rewards_claimed",25),
                               Achievement("Claimed 50 Rewards",True,20,"rewards_claimed",50),
                               Achievement("Claimed 250 Rewards",True,100,"rewards_claimed",250)]
        testtasks_completed = 10000
        testhigh_priority_tasks_completed = 2000
        testmedium_priority_tasks_completed = 3000
        testlow_priority_tasks_completed = 5000
        testrewards_claimed = 250
        testresultachievementlist = [Achievement("Completed 10 Tasks",True,2,"tasks_completed",10),
                                     Achievement("Completed 50 Tasks",True,10,"tasks_completed",50),
                                     Achievement("Completed 100 Tasks",True,20,"tasks_completed",100),
                                     Achievement("Completed 500 Tasks",True,100,"tasks_completed",500),
                                     Achievement("Completed 1000 Tasks",True,200,"tasks_completed",1000),
                                     Achievement("Completed 5000 Tasks",True,1000,"tasks_completed",5000),
                                     Achievement("Completed 10000 Tasks",True,2000,"tasks_completed",10000),
                                     Achievement("Completed 20 High Priority Tasks",True,2,"high_priority_tasks_completed",20),
                                     Achievement("Completed 100 High Priority Tasks",True,10,"high_priority_tasks_completed",100),
                                     Achievement("Completed 200 High Priority Tasks",True,20,"high_priority_tasks_completed",200),
                                     Achievement("Completed 1000 High Priority Tasks",True,100,"high_priority_tasks_completed",1000),
                                     Achievement("Completed 40 Medium Priority Tasks",True,2,"medium_priority_tasks_completed",40),
                                     Achievement("Completed 200 Medium Priority Tasks",True,10,"medium_priority_tasks_completed",200),
                                     Achievement("Completed 400 Medium Priority Tasks",True,20,"medium_priority_tasks_completed",400),
                                     Achievement("Completed 2000 Medium Priority Tasks",True,100,"medium_priority_tasks_completed",2000),
                                     Achievement("Completed 80 Low Priority Tasks",True,2,"low_priority_tasks_completed",80),
                                     Achievement("Completed 400 Low Priority Tasks",True,10,"low_priority_tasks_completed",400),
                                     Achievement("Completed 800 Low Priority Tasks",True,20,"low_priority_tasks_completed",800),
                                     Achievement("Completed 4000 Low Priority Tasks",True,100,"low_priority_tasks_completed",4000),
                                     Achievement("Claimed 5 Rewards",True,2,"rewards_claimed",5),
                                     Achievement("Claimed 25 Rewards",True,10,"rewards_claimed",25),
                                     Achievement("Claimed 50 Rewards",True,20,"rewards_claimed",50),
                                     Achievement("Claimed 250 Rewards",True,100,"rewards_claimed",250)]
        expected_result = {"credits_to_add": 2000,
                           "achievementlist": testresultachievementlist}
        self.assertEqual(check_achievements(testachievementlist,testtasks_completed,testhigh_priority_tasks_completed,testmedium_priority_tasks_completed,testlow_priority_tasks_completed,testrewards_claimed), expected_result)

    def test_check_achievements_1_task_completed_empty_list(self):
        testachievementlist = []
        testtasks_completed = 1
        testhigh_priority_tasks_completed = 1
        testmedium_priority_tasks_completed = 0
        testlow_priority_tasks_completed = 0
        testrewards_claimed = 0
        testresultachievementlist = [Achievement("Completed 10 Tasks",False,2,"tasks_completed",10),
                                     Achievement("Completed 50 Tasks",False,10,"tasks_completed",50),
                                     Achievement("Completed 100 Tasks",False,20,"tasks_completed",100),
                                     Achievement("Completed 500 Tasks",False,100,"tasks_completed",500),
                                     Achievement("Completed 1000 Tasks",False,200,"tasks_completed",1000),
                                     Achievement("Completed 5000 Tasks",False,1000,"tasks_completed",5000),
                                     Achievement("Completed 10000 Tasks",False,2000,"tasks_completed",10000),
                                     Achievement("Completed 20 High Priority Tasks",False,2,"high_priority_tasks_completed",20),
                                     Achievement("Completed 100 High Priority Tasks",False,10,"high_priority_tasks_completed",100),
                                     Achievement("Completed 200 High Priority Tasks",False,20,"high_priority_tasks_completed",200),
                                     Achievement("Completed 1000 High Priority Tasks",False,100,"high_priority_tasks_completed",1000),
                                     Achievement("Completed 40 Medium Priority Tasks",False,2,"medium_priority_tasks_completed",40),
                                     Achievement("Completed 200 Medium Priority Tasks",False,10,"medium_priority_tasks_completed",200),
                                     Achievement("Completed 400 Medium Priority Tasks",False,20,"medium_priority_tasks_completed",400),
                                     Achievement("Completed 2000 Medium Priority Tasks",False,100,"medium_priority_tasks_completed",2000),
                                     Achievement("Completed 80 Low Priority Tasks",False,2,"low_priority_tasks_completed",80),
                                     Achievement("Completed 400 Low Priority Tasks",False,10,"low_priority_tasks_completed",400),
                                     Achievement("Completed 800 Low Priority Tasks",False,20,"low_priority_tasks_completed",800),
                                     Achievement("Completed 4000 Low Priority Tasks",False,100,"low_priority_tasks_completed",4000),
                                     Achievement("Claimed 5 Rewards",False,2,"rewards_claimed",5),
                                     Achievement("Claimed 25 Rewards",False,10,"rewards_claimed",25),
                                     Achievement("Claimed 50 Rewards",False,20,"rewards_claimed",50),
                                     Achievement("Claimed 250 Rewards",False,100,"rewards_claimed",250)]
        expected_result = {"credits_to_add": 0,
                           "achievementlist": testresultachievementlist}
        self.assertEqual(check_achievements(testachievementlist,testtasks_completed,testhigh_priority_tasks_completed,testmedium_priority_tasks_completed,testlow_priority_tasks_completed,testrewards_claimed), expected_result)

if __name__ == "__main__":
    unittest.main()