# One Away: There are three types of edits that can be performed on strings:
# Insert a charecter, remove a charecter, or replace a charecter. Given two strings,
# write a function to check if they are one edit (or zero edits) away.
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

def one_away(s1, s2):
    if abs(len(s1) - len(s2)) >= 2:
        return False
    usage_count = [0] * 256

    for c in s1:
        usage_count[ord(c)] += 1

    for c in s2:
        usage_count[ord(c)] += 1

    count_odd = 0

    for c in usage_count:
        if c % 2 >= 1:
            count_odd += 1
    if count_odd > 2:
        return False
    return True


user_s1 = "pale"
user_s2 = "bake"
print(f"Strings are 1 or 0 edits away: {one_away(user_s1, user_s2)}")
