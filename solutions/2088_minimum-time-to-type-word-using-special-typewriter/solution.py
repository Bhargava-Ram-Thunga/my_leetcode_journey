class Solution:
    def minTimeToType(self, word: str) -> int:
        key = ".abcdefghijklmnopqrstuvwxyz"
        res = len(word)
        point = 1
        for c in word:
            pi = (key.index(c)-point)%26
            res+=min(pi,26-pi)
            point = key.index(c)
        return res