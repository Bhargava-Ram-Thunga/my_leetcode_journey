class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        else:
            res = []
            for num in nums:
                if num%2:
                    res.append(num)
                else:
                    res.insert(0,num)
            return res