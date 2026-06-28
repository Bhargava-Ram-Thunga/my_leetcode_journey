class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        li = []
        res = []
        for i in range(len(grid)):
            li.extend(grid[i])
        for num in li:
            if (num not in res) and li.count(num)>1:
                res.append(num)
        for i in range(1,(len(grid)**2)+1):
            if (i not in li):
                res.append(i) 
        return res