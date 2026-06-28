class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0
        for j in range(len(grid[0])):
            li = []
            for i in range(len(grid)):
                li.append(max(grid[i]))
                grid[i].remove(max(grid[i]))
            res+= max(li)
        return res
            
            
