class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        res = []
        temp = ""
        temp+= "".join(c for c in licensePlate.lower() if c.isalpha())
        temp = Counter(temp)
        for i in range(len(words)):
            if not (temp - Counter(words[i])):
                res.append(words[i])
        res = sorted(res,key = lambda x : (-len(x),-words.index(x)))
        return res[-1]
        