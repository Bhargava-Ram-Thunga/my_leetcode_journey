from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        main = Counter(words[0])
        for i in range(1,len(words)):
            main = main & Counter(words[i])
        res = []
        for key,value in main.items():
            res.extend([key]*value)
        return res

