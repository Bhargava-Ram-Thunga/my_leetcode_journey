class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            mini = nums.index(min(nums))
            nums[mini] = multiplier*nums[mini]
        return nums