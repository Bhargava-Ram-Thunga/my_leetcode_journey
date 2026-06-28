class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if len(nums) == 2:
                break
            if len(res)<2 and (nums[i] not in res) and nums.count(nums[i])==2:
                res.append(nums[i])

        return res
