# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures.

def is_unique_string(s: str):
    if not s and len(s) > 128:
        exit()

    chars_in_use_arry = [False] * 128

    for character in s:
        if chars_in_use_arry[ord(character)]:
            return False
        else:
            chars_in_use_arry[ord(character)] = True
    return True


user_input = "ajelsmShIW"
print(f'String has duplicate characters: {is_unique_string(user_input)}')
