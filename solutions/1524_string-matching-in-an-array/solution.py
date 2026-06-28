class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in words:
            for j in words:
                if j in i and i!=j:
                    res+=[j]
        return list(set(res))
                    
            