class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concval = 0
        while(nums):
            if(len(nums)>1):
                concval += int(str(nums[0])+str(nums[-1]))
                # print(concval)
                nums.pop(0)
                nums.pop(-1)
            else:
                concval += nums[0]
                nums.pop()
        return concval