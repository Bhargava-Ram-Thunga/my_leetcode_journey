from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(1,len(nums)+1):
            comb = list(map(list,combinations(nums,i)))
            res.extend(comb)
        return res