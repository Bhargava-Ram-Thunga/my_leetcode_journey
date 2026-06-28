class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            temp = list(str(nums[i]))
            res.extend(temp)
        for i in range(len(res)):
            res[i] = int(res[i])
        return res