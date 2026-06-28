class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        s = []
        for i in range(len(nums)-1):
            a = nums[i]
            b = max(nums[i+1:])
            if(b>a):
                s.append(b-a)
        if(s):
            return max(s)
        return -1
