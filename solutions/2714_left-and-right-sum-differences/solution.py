class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        sum = 0
        left = [0]
        right = [0]
        res = []
        for i in range(len(nums)-1):
            sum += nums[i]
            left.append(sum)
        sum = 0
        for i in range(len(nums)-1,0,-1):
            sum += nums[i]
            right.insert(0,sum)
        for i in range(len(left)):
            res.append(abs(left[i]-right[i]))
        return res