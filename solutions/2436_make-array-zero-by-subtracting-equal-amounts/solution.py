class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        while (nums):
            for i in range(nums.count(0)):
                nums.remove(0)
            if not nums:
                return count
            mini = min(nums)
            for i in range(len(nums)):
                nums[i] -= mini
            count += 1
        return count