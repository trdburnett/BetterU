import unittest
import datetime
from streak import streak_reset, yesterday_check, daily_reward
from freezegun import freeze_time

@freeze_time("2000-01-01 08:30:00")
class TestStreak(unittest.TestCase):

    def test_streak_reset_0(self):
        teststreak = 0
        testfreeze = 0
        testfreezes_required = 0
        expected_result = {"streak_to_add": 0,
                           "freeze_to_add": 0}
        self.assertEqual(streak_reset(teststreak,testfreeze,testfreezes_required), expected_result)

    def test_streak_reset_positive_streak_no_freeze(self):
        teststreak = 5
        testfreeze = 0
        testfreezes_required = 1
        expected_result = {"streak_to_add": -5,
                           "freeze_to_add": 0}
        self.assertEqual(streak_reset(teststreak,testfreeze,testfreezes_required), expected_result)

    def test_streak_reset_positive_streak_not_enough_freezes(self):
        teststreak = 5
        testfreeze = 2
        testfreezes_required = 5
        expected_result = {"streak_to_add": -5,
                           "freeze_to_add": -2}
        self.assertEqual(streak_reset(teststreak,testfreeze,testfreezes_required), expected_result)

    def test_streak_reset_positive_streak_saved(self):
        teststreak = 5
        testfreeze = 2
        testfreezes_required = 1
        expected_result = {"streak_to_add": 0,
                           "freeze_to_add": -1}
        self.assertEqual(streak_reset(teststreak,testfreeze,testfreezes_required), expected_result)    

    def test_yesterday_check_monday_true(self):
        testaccess_day = "Monday"
        testlast_access_day = "Sunday"
        expected_result = True
        self.assertEqual(yesterday_check(testlast_access_day,testaccess_day), expected_result)

    def test_yesterday_check_tuesday_true(self):
            testaccess_day = "Tuesday"
            testlast_access_day = "Monday"
            expected_result = True
            self.assertEqual(yesterday_check(testlast_access_day,testaccess_day), expected_result)

    def test_yesterday_check_wednesday_true(self):
            testaccess_day = "Wednesday"
            testlast_access_day = "Tuesday"
            expected_result = True
            self.assertEqual(yesterday_check(testlast_access_day,testaccess_day), expected_result)

    def test_yesterday_check_thursday_true(self):
            testaccess_day = "Thursday"
            testlast_access_day = "Wednesday"
            expected_result = True
            self.assertEqual(yesterday_check(testlast_access_day,testaccess_day), expected_result)

    def test_yesterday_check_friday_true(self):
            testaccess_day = "Friday"
            testlast_access_day = "Thursday"
            expected_result = True
            self.assertEqual(yesterday_check(testlast_access_day,testaccess_day), expected_result)

    def test_yesterday_check_saturday_true(self):
            testaccess_day = "Saturday"
            testlast_access_day = "Friday"
            expected_result = True
            self.assertEqual(yesterday_check(testlast_access_day,testaccess_day), expected_result)

    def test_yesterday_check_sunday_true(self):
            testaccess_day = "Sunday"
            testlast_access_day = "Saturday"
            expected_result = True
            self.assertEqual(yesterday_check(testlast_access_day,testaccess_day), expected_result)

    def test_yesterday_check_monday_false(self):
            testaccess_day = "Monday"
            testlast_access_day = "Saturday"
            expected_result = False
            self.assertEqual(yesterday_check(testlast_access_day,testaccess_day), expected_result)

    def test_yesterday_check_tuesday_false(self):
            testaccess_day = "Tuesday"
            testlast_access_day = "Sunday"
            expected_result = False
            self.assertEqual(yesterday_check(testlast_access_day,testaccess_day), expected_result)

    def test_yesterday_check_wednesday_false(self):
            testaccess_day = "Wednesday"
            testlast_access_day = "Monday"
            expected_result = False
            self.assertEqual(yesterday_check(testlast_access_day,testaccess_day), expected_result)

    def test_yesterday_check_thursday_false(self):
            testaccess_day = "Thursday"
            testlast_access_day = "Tuesday"
            expected_result = False
            self.assertEqual(yesterday_check(testlast_access_day,testaccess_day), expected_result)

    def test_yesterday_check_friday_false(self):
            testaccess_day = "Friday"
            testlast_access_day = "Wednesday"
            expected_result = False
            self.assertEqual(yesterday_check(testlast_access_day,testaccess_day), expected_result)

    def test_yesterday_check_saturday_false(self):
            testaccess_day = "Saturday"
            testlast_access_day = "Thursday"
            expected_result = False
            self.assertEqual(yesterday_check(testlast_access_day,testaccess_day), expected_result)

    def test_yesterday_check_sunday_false(self):
            testaccess_day = "Sunday"
            testlast_access_day = "Friday"
            expected_result = False
            self.assertEqual(yesterday_check(testlast_access_day,testaccess_day), expected_result)

    def test_daily_reward_first_time(self):
           testaccess_day = datetime.datetime.now()
           testlast_access_day = None
           teststreak = 0
           testfreeze = 0
           expected_result = {"last_accessed": datetime.datetime(2000,1,1,8,30),
                              "credits_to_add": 1,
                              "streak_to_add": 0,
                              "freeze_to_add": 0}
           self.assertEqual(daily_reward(testaccess_day,testlast_access_day,teststreak,testfreeze), expected_result)

    def test_daily_reward_last_accessed_yesterday_less_than_24_hours(self):
               testaccess_day = datetime.datetime.now()
               testlast_access_day = datetime.datetime(1999,12,31,22,30)
               teststreak = 0
               testfreeze = 0
               expected_result = {"last_accessed": datetime.datetime(2000,1,1,8,30),
                                  "credits_to_add": 1,
                                  "streak_to_add": 1,
                                  "freeze_to_add": 0}
               self.assertEqual(daily_reward(testaccess_day,testlast_access_day,teststreak,testfreeze), expected_result)

    def test_daily_reward_last_accessed_yesterday_more_than_24_hours(self):
                   testaccess_day = datetime.datetime.now()
                   testlast_access_day = datetime.datetime(1999,12,31,7,30)
                   teststreak = 0
                   testfreeze = 0
                   expected_result = {"last_accessed": datetime.datetime(2000,1,1,8,30),
                                      "credits_to_add": 1,
                                      "streak_to_add": 1,
                                      "freeze_to_add": 0}
                   self.assertEqual(daily_reward(testaccess_day,testlast_access_day,teststreak,testfreeze), expected_result)

    def test_daily_reward_last_accessed_sameday(self):
                   testaccess_day = datetime.datetime.now()
                   testlast_access_day = datetime.datetime(2000,1,1,7,30)
                   teststreak = 0
                   testfreeze = 0
                   expected_result = {"last_accessed": datetime.datetime(2000,1,1,8,30),
                                      "credits_to_add": 0,
                                      "streak_to_add": 0,
                                      "freeze_to_add": 0}
                   self.assertEqual(daily_reward(testaccess_day,testlast_access_day,teststreak,testfreeze), expected_result)

    def test_daily_reward_last_accessed_in_the_future(self):
                   testaccess_day = datetime.datetime.now()
                   testlast_access_day = datetime.datetime(2000,1,1,22,30)
                   teststreak = 0
                   testfreeze = 0
                   expected_result = {"last_accessed": datetime.datetime(2000,1,1,8,30),
                                      "credits_to_add": 0,
                                      "streak_to_add": 0,
                                      "freeze_to_add": 0}
                   self.assertEqual(daily_reward(testaccess_day,testlast_access_day,teststreak,testfreeze), expected_result)

    def test_daily_reward_last_accessed_not_yesterday_more_than_24_hours(self):
                   testaccess_day = datetime.datetime.now()
                   testlast_access_day = datetime.datetime(1999,12,28,22,30)
                   teststreak = 5
                   testfreeze = 0
                   expected_result = {"last_accessed": datetime.datetime(2000,1,1,8,30),
                                      "credits_to_add": 1,
                                      "streak_to_add": -5,
                                      "freeze_to_add": 0}
                   self.assertEqual(daily_reward(testaccess_day,testlast_access_day,teststreak,testfreeze), expected_result)

    def test_daily_reward_last_accessed_yesterday_less_than_24_hours_week_streak(self):
                   testaccess_day = datetime.datetime.now()
                   testlast_access_day = datetime.datetime(1999,12,31,22,30)
                   teststreak = 6
                   testfreeze = 0
                   expected_result = {"last_accessed": datetime.datetime(2000,1,1,8,30),
                                      "credits_to_add": 7,
                                      "streak_to_add": 1,
                                      "freeze_to_add": 0}
                   self.assertEqual(daily_reward(testaccess_day,testlast_access_day,teststreak,testfreeze), expected_result)

    def test_daily_reward_last_accessed_yesterday_less_than_24_hours_month_streak(self):
                   testaccess_day = datetime.datetime.now()
                   testlast_access_day = datetime.datetime(1999,12,31,22,30)
                   teststreak = 27
                   testfreeze = 0
                   expected_result = {"last_accessed": datetime.datetime(2000,1,1,8,30),
                                      "credits_to_add": 28,
                                      "streak_to_add": 1,
                                      "freeze_to_add": 0}
                   self.assertEqual(daily_reward(testaccess_day,testlast_access_day,teststreak,testfreeze), expected_result)

    def test_daily_reward_last_accessed_yesterday_less_than_24_hours_year_streak(self):
                   testaccess_day = datetime.datetime.now()
                   testlast_access_day = datetime.datetime(1999,12,31,22,30)
                   teststreak = 363
                   testfreeze = 0
                   expected_result = {"last_accessed": datetime.datetime(2000,1,1,8,30),
                                      "credits_to_add": 100,
                                      "streak_to_add": -363,
                                      "freeze_to_add": 0}
                   self.assertEqual(daily_reward(testaccess_day,testlast_access_day,teststreak,testfreeze), expected_result)