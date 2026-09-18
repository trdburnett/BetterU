import unittest
import datetime
from tasks import Task, add_task, remove_task
from freezegun import freeze_time

@freeze_time("2000-01-01")
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


if __name__ == "__main__":
    unittest.main()