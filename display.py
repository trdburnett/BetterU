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

def display_box_top(id: int, caller: str, terminal_size: set)->str:
    columns = terminal_size[0]
    decorated_string = f"[{caller} ID: {id}]"
    space_to_pad = columns - len(decorated_string)
    left_side_padding = space_to_pad // 2
    right_side_padding = left_side_padding
    if space_to_pad %2 != 0:
        right_side_padding += 1
    left_box_padding = ""
    while left_side_padding > 0:
        left_box_padding = left_box_padding + "_"
        left_side_padding -= 1
    right_box_padding = ""
    while right_side_padding > 0:
        right_box_padding = right_box_padding + "_"
        right_side_padding -= 1
    box_top = left_box_padding + decorated_string + right_box_padding
    return box_top

def description_padding(description: str, terminal_size: set)->str:
    columns = terminal_size[0]
    truncated_description = ""
    truncated_padding = "|"
    result_string = ""
    if len(description) > (columns - 2):
        truncated_description = truncated_description + description[0:(columns - 5)] + "..."
    if truncated_description == "":
        space_to_pad = columns - len(description) - 2
        left_side_padding = space_to_pad // 2
        right_side_padding = left_side_padding
        if space_to_pad % 2 != 0:
            right_side_padding += 1
        left_space_padding = "|"
        while left_side_padding > 0:
            left_space_padding = left_space_padding + " "
            left_side_padding -= 1
        right_space_padding = ""
        while right_side_padding > 0:
            right_space_padding = right_space_padding + " "
            right_side_padding -= 1
        right_space_padding = right_space_padding + "|"
        result_string = result_string + left_space_padding + description + right_space_padding
    else:
        result_string = result_string + truncated_padding + truncated_description + truncated_padding
    return result_string

def reward_and_time_remaining_padding(reward: str, time_remaining: str, terminal_size: set)->str:
    result_string = ""
    columns = terminal_size[0]
    space_for_reward = columns // 2
    space_for_time_remaining = space_for_reward
    if columns % 2 != 0:
        space_for_time_remaining += 1
    space_to_pad_for_reward = space_for_reward - len(reward) -1
    left_side_padding_reward = space_to_pad_for_reward // 2
    right_side_padding_reward = left_side_padding_reward
    if space_to_pad_for_reward % 2 != 0:
        right_side_padding_reward += 1
    left_space_padding_reward = "|"
    while left_side_padding_reward > 0:
        left_space_padding_reward = left_space_padding_reward + " "
        left_side_padding_reward -= 1
    right_space_padding_reward = ""
    while right_side_padding_reward > 0:
        right_space_padding_reward = right_space_padding_reward + " "
        right_side_padding_reward -= 1
    space_to_pad_for_time_remaining = space_for_time_remaining - len(time_remaining) -1
    left_side_padding_time_remaining = space_to_pad_for_time_remaining // 2
    right_side_padding_time_remaining = left_side_padding_time_remaining
    if space_to_pad_for_time_remaining % 2 != 0:
        right_side_padding_time_remaining += 1
    left_space_padding_time_remaining = ""
    while left_side_padding_time_remaining > 0:
        left_space_padding_time_remaining = left_space_padding_time_remaining + " "
        left_side_padding_time_remaining -= 1
    right_space_padding_time_remaining = ""
    while right_side_padding_time_remaining > 0:
        right_space_padding_time_remaining = right_space_padding_time_remaining + " "
        right_side_padding_time_remaining -= 1
    right_space_padding_time_remaining = right_space_padding_time_remaining + "|"
    result_string = result_string + left_space_padding_reward + reward + right_space_padding_reward + left_space_padding_time_remaining + time_remaining + right_space_padding_time_remaining
    return result_string

def display_box_bottom(terminal_size: set)->str:
    box_bottom = ""
    padding_size = terminal_size[0]
    while padding_size > 0:
        box_bottom = box_bottom + ' \u0305'
        padding_size -= 1
    return box_bottom

def string_strikethrough(string_to_strikethorugh: str)->str:
    result = ""
    for character in string_to_strikethorugh:
        result = result + character + '\u0336'
    return result

#shows available credits
def display_credits(credits: int):
    print(f"Available Credits: {credits}")

#displays statistics
def display_stats(tasks_completed: int, high_priority_tasks_completed: int, medium_priority_tasks_completed: int, low_priority_tasks_completed: int, rewards_claimed: int, streak: int, freeze: int, terminal_size: set):
    print(display_banner("Statistics",terminal_size))
    print(f"Tasks Completed: {tasks_completed}")
    print(f"High Priority Tasks Completed: {high_priority_tasks_completed}")
    print(f"Medium Priority Tasks Completed: {medium_priority_tasks_completed}")
    print(f"Low Priority Tasks Completed: {low_priority_tasks_completed}")
    print(f"Rewards Claimed: {rewards_claimed}")
    print(f"Current Streak: {streak} day(s)")
    print(f"Current Streak Freezes: {freeze} ")