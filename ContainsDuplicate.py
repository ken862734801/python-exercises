# Given an integer array nums,
# return true if any value appears
# at least twice in the array
# return false if every element is distinct

def containsDuplicate(nums: list[int]) -> bool:

    num_count = {}

    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    for key, value in num_count.items():
        if value >= 2:
            return True
    
    return False