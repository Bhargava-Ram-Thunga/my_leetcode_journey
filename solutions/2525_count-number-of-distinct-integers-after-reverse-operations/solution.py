class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        k = len(nums)
        for i in range(k):
            nums.append(int(str(nums[i])[::-1]))
        return len(set(nums))