import unittest
import datetime
from tasks import Task

class TestTasks(unittest.TestCase):

    def test_task_class(self):
        task = Task("Test Task",1,1,datetime.datetime(2000,1,1,8,30),1)
        self.assertEqual(task.description, "Test Task")
        self.assertEqual(task.priority, 1)
        self.assertEqual(task.reward, 1)
        self.assertEqual(task.time, datetime.datetime(2000,1,1,8,30))
        self.assertEqual(task.id, 1)

if __name__ == "__main__":
    unittest.main()