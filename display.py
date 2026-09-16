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
def display_banner(string_to_banner: str)->str:
    left_banner_padding = "==============================["
    right_banner_padding = "]========================="
    uniform_padding = ""
    uniform_padding_size = 20 - len(string_to_banner)
    while uniform_padding_size > 0:
        uniform_padding = uniform_padding + "="
        uniform_padding_size -= 1
    banner = left_banner_padding + string_to_banner + right_banner_padding + uniform_padding
    return banner