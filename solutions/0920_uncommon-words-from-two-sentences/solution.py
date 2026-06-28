class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_li = s1.split()
        s2_li = s2.split()
        res = []
        for item in s1_li:
            if s1_li.count(item)==1 and item not in s2_li:
                res.append(item)
        for item in s2_li:
            if s2_li.count(item)==1 and item not in s1_li:
                res.append(item)
        return res