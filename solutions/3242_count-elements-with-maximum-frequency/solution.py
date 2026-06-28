class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        li = []
        for i in range(len(nums)):
            li.append(nums.count(nums[i]))
        return li.count(max(li))