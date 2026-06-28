class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        sort_grid = sorted(grid,key = lambda x : (-sum(x)))
        return grid.index(sort_grid[0])