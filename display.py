#returns a string of spaces based on the length of the description it is given
#helper method for display functions
def display_padding(description: str)->str:
    padding = ""
    padding_size = 50 - len(description)
    while padding_size > 0:
        padding = padding + " "
        padding_size -= 1
    return padding

#returns a string to be used as a banner at the top of displays
#helper method for display functions
def display_banner(string_to_banner: str, terminal_size: set)->str:
    #left_banner_padding = "==============================["
    #right_banner_padding = "]========================="
    #uniform_padding = ""
    #uniform_padding_size = 20 - len(string_to_banner)
    #while uniform_padding_size > 0:
    #    uniform_padding = uniform_padding + "="
    #    uniform_padding_size -= 1
    #banner = left_banner_padding + string_to_banner + right_banner_padding + uniform_padding
    columns = terminal_size[0]
    decorated_string = f"[{string_to_banner}]"
    space_to_pad = columns - len(decorated_string)
    left_side_padding = space_to_pad // 2
    right_side_padding = left_side_padding
    if space_to_pad % 2 != 0:
        right_side_padding += 1
    left_banner_padding = ""
    while left_side_padding > 0:
        left_banner_padding = left_banner_padding + "="
        left_side_padding -= 1
    right_banner_padding = ""
    while right_side_padding > 0:
        right_banner_padding = right_banner_padding + "="
        right_side_padding -= 1
    banner = left_banner_padding + decorated_string + right_banner_padding
    return banner

#shows available credits
def display_credits(credits: int):
    print(f"Available Credits: {credits}")

#displays statistics
def display_stats(tasks_completed: int, high_priority_tasks_completed: int, medium_priority_tasks_completed: int, low_priority_tasks_completed: int, rewards_claimed: int, streak: int, freeze: int):
    print(display_banner("Statistics"))
    print(f"Tasks Completed: {tasks_completed}")
    print(f"High Priority Tasks Completed: {high_priority_tasks_completed}")
    print(f"Medium Priority Tasks Completed: {medium_priority_tasks_completed}")
    print(f"Low Priority Tasks Completed: {low_priority_tasks_completed}")
    print(f"Rewards Claimed: {rewards_claimed}")
    print(f"Current Streak: {streak} day(s)")
    print(f"Current Streak Freezes: {freeze} ")