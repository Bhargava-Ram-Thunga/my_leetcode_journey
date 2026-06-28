class Solution:
    def sortSentence(self, s: str) -> str:
        res = [0]*len(s.split())
        for word in s.split():
            res[int(word[-1])-1] = word[:-1]
        return " ".join(res)

