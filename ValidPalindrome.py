#  A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
#  Alphanumeric characters include letters and numbers.
#  Given a string s, return true if it is a palindrome, or false otherwise.
def isPalindrome(s: str) -> bool:
    # for each character in the characters of the string that are alphanumeric
    # join together without space, and make lowercase
    s = "".join(char for char in s if char.isalnum()).lower()
    # slice notation to reverse the string
    if s == s[::-1]:
        print("True")
        return True
    else:
        print("False")
        return False

isPalindrome("Test")
isPalindrome("A man, a plan, a canal: Panama")
