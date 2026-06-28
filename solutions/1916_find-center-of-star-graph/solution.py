class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        res = []
        for li in edges :
            res.extend(li)
        someDict = Counter(res)
        someDict = dict(sorted(someDict.items(),key = lambda item: item[1],reverse = True))
        return list(someDict.keys())[0]