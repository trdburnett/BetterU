import unittest
import datetime
from tasks import Task, add_task, remove_task, time_remaining, complete_task
from achievement import populate_achievement_list
from freezegun import freeze_time

@freeze_time("2000-01-01 08:30:00")
class TestTasks(unittest.TestCase):

    def test_task_class(self):
        task = Task("Test Task",1,1,datetime.datetime(2000,1,1,8,30),1)
        self.assertEqual(task.description, "Test Task")
        self.assertEqual(task.priority, 1)
        self.assertEqual(task.reward, 1)
        self.assertEqual(task.time, datetime.datetime(2000,1,1,8,30))
        self.assertEqual(task.id, 1)

    def test_add_task(self):
        testtasklist = [Task("Test Task",1,1,datetime.datetime.now(),1)]
        tasklist = add_task("Test Task",1,1,1,[])
        self.assertEqual(tasklist[0].description, testtasklist[0].description)
        self.assertEqual(tasklist[0].priority, testtasklist[0].priority)
        self.assertEqual(tasklist[0].reward, testtasklist[0].reward)
        self.assertEqual(tasklist[0].time, testtasklist[0].time)
        self.assertEqual(tasklist[0].id, testtasklist[0].id)

    def test_remove_task_successful_removal(self):
        testtasklist = [Task("Test Task",1,1,datetime.datetime.now(),1)]
        self.assertEqual(remove_task(1,testtasklist), [])

    def test_remove_task_unsuccessful_removal(self):
        testtasklist = [Task("Test Task",1,1,datetime.datetime.now(),1)]
        self.assertEqual(remove_task(2,testtasklist), testtasklist)
        
    def test_remove_task_successful_removal_called_by_complete_task(self):
        testtasklist = [Task("Test Task",1,1,datetime.datetime.now(),1)]
        expected_dict = {"description": "Test Task",
                         "priority": 1,
                         "reward": 1,
                         "task_time": datetime.datetime.now(),
                         "tasklist": testtasklist}
        self.assertEqual(remove_task(1,testtasklist,True), expected_dict)

    def test_remove_task_unsuccessful_removal_called_by_complete_task(self):
        testtasklist = [Task("Test Task",1,1,datetime.datetime.now(),1)]
        self.assertEqual(remove_task(2,testtasklist,True), None)

    def test_time_remaining_priority_1_in_range(self):
        expected_result = datetime.timedelta(days=2)
        self.assertEqual(time_remaining(1, datetime.datetime.now()), expected_result)

    def test_time_remaining_priority_1_not_in_range(self):
        expected_result = "Expired!"
        self.assertEqual(time_remaining(1, datetime.datetime(1999,12,30,8,30)), expected_result)

    def test_time_remaining_priority_2_in_range(self):
        expected_result = datetime.timedelta(days=7)
        self.assertEqual(time_remaining(2, datetime.datetime.now()), expected_result)

    def test_time_remaining_priority_2_not_in_range(self):
        expected_result = "Expired!"
        self.assertEqual(time_remaining(2, datetime.datetime(1999,12,25,8,30)), expected_result)

    def test_time_remaining_priority_3_in_range(self):
        expected_result = datetime.timedelta(days=28)
        self.assertEqual(time_remaining(3, datetime.datetime.now()), expected_result)

    def test_time_remaining_priority_3_not_in_range(self):
        expected_result = "Expired!"
        self.assertEqual(time_remaining(3, datetime.datetime(1999,12,3,8,30)), expected_result)

    def test_complete_task_success_priority_1_task_in_range_no_achievement_triggered_no_streak_triggered_no_repeat(self):
        testtask_id = 1
        testtasklist = [Task("Test Task",1,1,datetime.datetime.now(),1)]
        testachievementlist = populate_achievement_list([])
        testlast_accessed = datetime.datetime.now() - datetime.timedelta(hours=1)
        testtasks_completed = 0
        testhigh_priority_tasks_completed = 0
        testmedium_priority_tasks_completed = 0
        testlow_priority_tasks_completed = 0
        testrewards_claimed = 0
        teststreak = 0
        expected_result = {"credits_to_add": 1,
                           "tasks_completed_to_add": 1,
                           "high_priority_tasks_completed_to_add": 1,
                           "medium_priority_tasks_completed_to_add": 0,
                           "low_priority_tasks_completed_to_add": 0,
                           "streak_to_add": 0,
                           "last_accessed": testlast_accessed,
                           "tasklist": [],
                           "achievementlist": testachievementlist}
        self.assertEqual(complete_task(testtask_id,testtasklist,testachievementlist,testlast_accessed,testtasks_completed,testhigh_priority_tasks_completed,testmedium_priority_tasks_completed,testlow_priority_tasks_completed,testrewards_claimed,teststreak), expected_result)

if __name__ == "__main__":
    unittest.main()