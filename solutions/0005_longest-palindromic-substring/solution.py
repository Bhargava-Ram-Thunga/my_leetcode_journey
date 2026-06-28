class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                if s[i:j] == s[i:j][::-1] and len(s[i:j])>len(res):
                    res = s[i:j]
        return res