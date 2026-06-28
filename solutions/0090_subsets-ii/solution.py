from itertools import combinations
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        c = []
        for i in range(len(nums)+1):
            c.extend(list(map(list,list(combinations(nums,i)))))
        return sorted(map(list,set(map(tuple,c))))