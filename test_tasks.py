import unittest
import datetime
from tasks import Task, add_task
from freezegun import freeze_time

class TestTasks(unittest.TestCase):

    def test_task_class(self):
        task = Task("Test Task",1,1,datetime.datetime(2000,1,1,8,30),1)
        self.assertEqual(task.description, "Test Task")
        self.assertEqual(task.priority, 1)
        self.assertEqual(task.reward, 1)
        self.assertEqual(task.time, datetime.datetime(2000,1,1,8,30))
        self.assertEqual(task.id, 1)

    @freeze_time("2000-01-01")
    def test_add_task(self):
        testtasklist = [Task("Test Task",1,1,datetime.datetime.now(),1)]
        self.assertEqual(add_task("Test Task",1,1,1,[])[0].description, testtasklist[0].description)
        self.assertEqual(add_task("Test Task",1,1,1,[])[0].priority, testtasklist[0].priority)
        self.assertEqual(add_task("Test Task",1,1,1,[])[0].reward, testtasklist[0].reward)
        self.assertEqual(add_task("Test Task",1,1,1,[])[0].time, testtasklist[0].time)
        self.assertEqual(add_task("Test Task",1,1,1,[])[0].id, testtasklist[0].id)

if __name__ == "__main__":
    unittest.main()