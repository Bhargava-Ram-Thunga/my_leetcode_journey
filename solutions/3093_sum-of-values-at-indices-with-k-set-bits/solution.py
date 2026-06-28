class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sum1 = 0
        for i in range(len(nums)):
            if (bin(i)[2:]).count("1")==k:
                sum1+=nums[i]
        return sum1