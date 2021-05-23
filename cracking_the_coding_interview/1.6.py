# String Compression: Implement a method to perform basic string compression
# using the counts of repeated characters. For example, the string aabcccccaaa
# would be a2b1c5a3. If the "compressed" string would not become smaller than 
# the original string, your method should return the original string. 
# You can assume the string has only uppercase and lowercase letters (a-z).

def compress_string(s):
    if len(s) <= 1:
        return s

    letter_count = 0
    prev_letter = s[0]
    result = ""
    for letter in s:
        if prev_letter == letter:
            letter_count += 1
        else:
            result += f"{prev_letter}{letter_count}"
            letter_count = 1
            prev_letter = letter
    result += f'{prev_letter}{letter_count}'
    return result


user_s = "aabcccccaaa"
print(f"{user_s}  ->  {compress_string(user_s)}")
