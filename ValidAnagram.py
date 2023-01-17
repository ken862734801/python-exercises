# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

def isAnagram(s: str, t: str) -> bool:
    # if lengths are different they can not be anagrams
    if len(s) != len(t):
        return False
    # create hash table to record the frequency of each character
    char_count = {}
    # iterate through the first string
    for char in s:
        # if first string character is a key in the hash table, add one to the value
        if char in char_count:
            char_count[char] += 1
        # if first string character is not a key in hash table, make the value 1
        else:
            char_count[char] = 1

    for char in s:
        # if second string character is already present,
        if char in char_count:
            # subtrac the value (frequency) by one
            char_count[char] -= 1
            # if second string is already present, and the value has been lowered to negative
            # that means the character is present more times in the second string
            # so they cannot be anagrams
            if char_count[char] < 0:
                return False
        else:
            return False
            
    return True