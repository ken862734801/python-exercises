
def romanToInt(s:str) -> int:
    # dictionary containing symbol and integer
    symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    # int variable for the ans
    ans = 0
    # iterate through the length of the s with range method
    for i in range(len(s)):
        # current letter in the str
        curr = symbols[s[i]]
        # check if i is still less than string length
        # check if the next char value is larger than current
        if i+1 < len(s) and symbols[s[i+1]] > curr:
            # if so subtract curr
            ans -= curr
        else:
            # if not, add curr
            ans += curr

    return ans