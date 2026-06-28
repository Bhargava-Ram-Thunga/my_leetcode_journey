class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) ==1 :
            return nums[0]
        s = [0]
        t=0
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                t += nums[i-1]
            else:
                s.append(t+nums[i-1])
                t = 0
        if nums[-2] <nums[-1]:
            t+=nums[-1]
            s.append(t)
        else:
            s.append(t)
            s.append(nums[-1])
        return max(s)