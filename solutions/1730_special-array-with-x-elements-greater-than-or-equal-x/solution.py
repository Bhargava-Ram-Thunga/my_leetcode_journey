class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)+1):
            nums.append(i)
            nums = sorted(nums)
            ind = nums.index(i)
            if len(nums[ind+1:]) == i:
                return i
            nums.pop(ind)
        return -1