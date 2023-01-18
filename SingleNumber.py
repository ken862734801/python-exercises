# Given a non-empty array of integers nums, every element appears twice except for one. 
# Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber(nums:list[int]) -> int:
    # create hash table
    num_count = {}

    # iterate through the list
    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

   # iterate through hash table; returning key and value
    for key, count in num_count.items():
        # if value equals one
        if count == 1:
        # return associated key
            return key