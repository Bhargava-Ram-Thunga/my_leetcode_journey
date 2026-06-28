class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = []
        ans = 0
        for word in words:
            res.append(set(word))
        temp = []
        for s in res:
            if s not in temp:
                c = res.count(s)
                ans += (c*(c-1))//2
                temp.append(s)
        return ans
            

