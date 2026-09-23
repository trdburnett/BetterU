import datetime

#helper for daily reward
#checks if last_accessed day was yesterday to be used in the event that it had been less than 24 hours
def yesterday_check(last_accessed_day: str, access_day: str) -> bool:
    yesterday = False
    if last_accessed_day == "Monday":
        if access_day == "Tuesday":
            yesterday = True
    if last_accessed_day == "Tuesday":
        if access_day == "Wednesday":
            yesterday = True
    if last_accessed_day == "Wednesday":
        if access_day == "Thursday":
            yesterday = True
    if last_accessed_day == "Thursday":
        if access_day == "Friday":
            yesterday = True
    if last_accessed_day == "Friday":
        if access_day == "Saturday":
            yesterday = True
    if last_accessed_day == "Saturday":
        if access_day == "Sunday":
            yesterday = True
    if last_accessed_day == "Sunday":
        if access_day == "Monday":
            yesterday = True
    return yesterday

#helper for daily reward
#resets streak when not upheld
def streak_reset(streak: int)->int:
    return streak * -1

#called by complete task
#checks the last time a task was completed and if it is a new day displays a welcome message and applies a credit
def daily_reward(access_time: datetime, last_accessed: datetime, streak: int)->dict:
    credits_to_add = 0
    streak_to_add = 0
    access_day = access_time.strftime("%A")
    if last_accessed == None:
        credits_to_add += 1
        print("Looks like this your first time. You have been awarded a credit to help motivate you on your task completion journey!")
    elif last_accessed <= access_time - datetime.timedelta(days=1) and not yesterday_check(last_accessed.strftime("%A"),access_day):
        credits_to_add += 1
        streak_to_add = streak_reset(streak)
        print("Looks like its been more than a day. You have been awarded a credit to get you motivated!")
    elif yesterday_check(last_accessed.strftime("%A"),access_day):
        credits_to_add += 1
        streak_to_add += 1
        print(f"You are getting things done! Have a productive {access_day}. You have increased your streak to {streak+streak_to_add} day(s) and been awarded your daily credit!")
        if (streak+streak_to_add) % 7 == 0:
            streak_weeks = (streak+streak_to_add) / 7
            if streak_weeks % 4 == 0:
                streak_months = streak_weeks / 4
                if streak_months % 13 == 0:
                    credits_to_add += 99
                    streak_to_add = streak_reset(streak)
                    print(f"Amazing you have been getting tasks done for whole year! Your streak has now been reset and you have been awarded another 99 credits")
                else:
                    credits_to_add += 27
                    print(f"Congratulations on reaching a streak of {int(streak_months)} month(s)! You have awarded another 27 credits")
            else:    
                credits_to_add += 6
                print(f"Congratulations on reaching a streak of {int(streak_weeks)} week(s)! You have been awarded another 6 credits")
    elif last_accessed > access_time:
        print(f"Well that is naughty, how has modifiying the last accessed time to the future helped you get things done?")
    last_accessed = access_time
    return {"last_accessed": last_accessed,
            "credits_to_add": credits_to_add,
            "streak_to_add": streak_to_add}