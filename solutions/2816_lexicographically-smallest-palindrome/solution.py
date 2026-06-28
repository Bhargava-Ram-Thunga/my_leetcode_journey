class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        res = list(s)
        if s[::-1] == s:
            return s
        else:
            for i in range(len(s)//2):
                if res[i] != res[-1-i]:
                    if res[i] > res[-1-i]:
                        res[i] = res[-1-i]
                    else:
                        res[-1-i] = res[i]
                if res[::-1] == res:
                    return "".join(res)
        return res
                    