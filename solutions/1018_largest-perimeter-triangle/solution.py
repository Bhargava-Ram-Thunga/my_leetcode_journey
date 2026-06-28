class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums,reverse =True)
        for i in range(len(nums)-2):
            a,b,c = nums[i:i+3]
            if(a+b > c and b+c > a and a+c > b):
                return a+b+c
        return 0

