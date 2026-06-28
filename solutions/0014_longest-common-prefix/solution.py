class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        word = strs[0]
        for i in range(1,len(word)+2):
            for string in strs:
                if not string.startswith(word[:i]):
                    return res
                res = word[:i-1]
        return res