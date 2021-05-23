# Palindrome Permutation: Given a string, write a function to check if it is a
# permutation of a palindrome. A palindrome is a word or phrase that is the
# same forwards and backwards. A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.
# 
# Example:
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc.)

def is_pp(s):
    s = s.replace(' ', '')

    if len(s) <= 1:
        return False
    if len(s) == 2 and s[0] == s[2]:
        return True

    used_count = [0] * 256

    for c in s:
        used_count[ord(c)] = used_count[ord(c)] + 1

    odd_count = 0

    for element in used_count:
        if element % 2 > 0:
            odd_count += 1

    if odd_count > 1:
        return False
    return True


user_s = 'mom'
print(f'String is a permutation of a palindrome: {is_pp(user_s)}')
