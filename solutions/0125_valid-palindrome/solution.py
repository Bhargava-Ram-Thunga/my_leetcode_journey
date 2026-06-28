class Solution(object):
    def isPalindrome(self, s):
        res = "".join(c.lower() if c.isalnum() else "" for c in s)
        if res ==  res[::-1]:
            return True
        return False
        