# Check Permutation: Given teo strings, write a method to decide if one
# is a permutation of the other.

def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    if s1_sorted == s2_sorted:
        return True
    return False


user_s1 = "aaaefscffc"
user_s2 = "ccsfffeaaa"

print(f"Strings are permutations: {is_permutation(user_s1, user_s2)}")
