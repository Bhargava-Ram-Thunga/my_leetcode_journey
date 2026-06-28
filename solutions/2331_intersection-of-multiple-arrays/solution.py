class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        numSet = set(nums[0])
        for i in range(1,len(nums)):
            numSet = numSet & set(nums[i])
        return sorted(numSet)